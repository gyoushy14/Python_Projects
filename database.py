# CURSOR => All Operation in SQL Done by it 
# Commit => save all changes
import sqlite3
First_db=sqlite3.connect("use.db") # Create database and connect
First_db.execute("create table if not exists students (id integer , name text)") # Create a table in the database with columns name,grade,id
li=["Ali","Ahmed","Jo",'John'] # List of names
Cur= First_db.cursor() #
for key,user in enumerate(li):
    Cur.execute(f"insert into students( id ,name) values({key + 1} , '{user}')") # Insert data to table
First_db.commit()
First_db.close()
# First_db.close() # close Database

