import streamlit as st
from pathlib import Path
from langchain_community.agent_toolkits import create_sql_agent
from langchain_community.utilities.sql_database import SQLDatabase
from langchain_classic.agents.agent_types import AgentType
from langchain_community.callbacks import StreamlitCallbackHandler
from langchain_community.agent_toolkits import SQLDatabaseToolkit
from sqlalchemy import create_engine
import sqlite3
from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os

st.set_page_config(page_title="Langchain: Chat with SQL DB", page_icon='🦜')
st.title("🦜 Langchain: Chat with SQL DB")

LOCALDB= "USE_LOCALDB"

load_dotenv()
api_key = os.getenv("GROQ_API_KEY")

radio_opt = ["Use SQLite3 Database- Student.db"]
selected_option = st.sidebar.radio(label="choose the DB which you want to chat", options=radio_opt)

if radio_opt.index(selected_option)==0:
    db_uri = LOCALDB

if not db_uri:
    st.info("Please enter the database information and uri")

## LLM model
llm = ChatGroq(groq_api_key = api_key, model_name='meta-llama/llama-4-scout-17b-16e-instruct')

@st.cache_resource(ttl="2h")
def configure_db(db_uri):
    dbfilePath = (Path(__file__).parent/"student.db").absolute()
    creator = lambda:sqlite3.connect(f"file:{dbfilePath}?mode=ro", uri=True)
    return SQLDatabase(create_engine("sqlite:///", creator=creator))

db = configure_db(db_uri)
## toolkit
toolkit = SQLDatabaseToolkit(db=db, llm = llm)

agent = create_sql_agent(
    llm = llm,
    toolkit = toolkit,
    verbose= True,
    agent_type = AgentType.ZERO_SHOT_REACT_DESCRIPTION
)

if "messages" not in st.session_state or st.sidebar.button('Clear Message history'):
    st.session_state["messages"] = [{"role": "assistant", "content" : "How can I help you?"}]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

user_query = st.chat_input(placeholder="Ask Anything from the database")

if user_query:
    st.session_state.messages.append({"role": "User", "content": user_query})
    st.chat_message("User").write(user_query)

    with st.chat_message("assistant"):
        streamlit_callback = StreamlitCallbackHandler(st.container())
        response = agent.run(user_query, callbacks=[streamlit_callback])
        st.session_state.messages.append({"role":"assistant", "content" : response})
        st.write(response)

