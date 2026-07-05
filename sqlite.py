import sqlite3

## connect to sqlite
connection = sqlite3.connect("student.db")

## create a cursor objetc to insert record, create table
cursor = connection.cursor()

## create the table
table_info='''
create table STUDENT(NAME VARCHAR(25),
CLASS VARCHAR(25),
SECTION VARCHAR(25),
MARKS INT)
'''

cursor.execute(table_info)

## insert some more records
cursor.execute('''INSERT INTO STUDENT VALUES("Krish", "Data Science", "A", 90)''')
cursor.execute('''Insert into STUDENT values('john', 'Data Science', 'B', 100)''')
cursor.execute('''Insert into STUDENT values('Mukesh', 'Data Science', 'A', 86)''')
cursor.execute('''Insert into STUDENT values('Jacob', 'Devops', 'A', 50)''')
cursor.execute('''Insert into STUDENT values('Dipesh', 'Devops', 'A', 35)''')

## Display all the records
print("The inserted records are")
data= cursor.execute('''SELECT * FROM STUDENT''')
for row in data:
    print(row)

## commmit the changes in database
connection.commit()
connection.close()