# Natural Language SQL Assistant using LangChain & Groq

##  About the Project

This project is an AI-powered SQL Assistant that allows users to interact with a SQLite database using natural language. Instead of writing SQL queries manually, users can ask questions in plain English, and the application automatically generates and executes SQL queries using a Large Language Model (LLM).

##  Features

- Chat with a SQLite database using natural language.
- Automatically converts English questions into SQL queries.
- Interactive Streamlit interface.
- Maintains chat history.
- Powered by LangChain SQL Agent and Groq LLM.

##  Tech Stack

- Python
- LangChain
- Groq (Llama)
- SQLite
- SQLAlchemy
- Streamlit

##  How to Run

1. Clone the repository.
2. Install the required dependencies.
3. Add your `GROQ_API_KEY` to a `.env` file.
4. Run the application:

```bash
streamlit run app.py
```

##  Sample Questions

- Show all students.
- List students from Data Science.
- Who scored the highest marks?
- Show students in Section A.

##  Learning Outcomes

- Built an AI-powered SQL assistant using LangChain.
- Integrated Groq LLM with a SQLite database.
- Learned Agent-based workflows and natural language to SQL conversion.
