# Import required modules
import csv
import sqlite3
 
# Connecting to the geeks database
connection = sqlite3.connect('db.sqlite3')
 
# Creating a cursor object to execute
# SQL queries on a database table
cursor = connection.cursor()
 
# Table Definition
create_table = '''CREATE TABLE Company(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                environment INTEGER NOT NULL,
                social INTEGER NOT NULL,
                governance INTEGER NOT NULL,
                rating TEXT NOT NULL);
                '''
 
# Creating the table into our
# database
cursor.execute(create_table)
 
# Opening the person-records.csv file
file = open('data1.csv')
 
# Reading the contents of the
# person-records.csv file
contents = csv.reader(file)
 
# SQL query to insert data into the
# person table
insert_records = "INSERT INTO company (name,environment,social,governance,rating) VALUES(?,?,?,?,?)"
 
# Importing the contents of the file
# into our person table
cursor.executemany(insert_records, contents)
 
# SQL query to retrieve all data from
# the person table To verify that the
# data of the csv file has been successfully
# inserted into the table
select_all = "SELECT * FROM company"
rows = cursor.execute(select_all).fetchall()
 
# Output to the console screen
for r in rows:
    print(r)
 
# Committing the changes
connection.commit()
 
# closing the database connection
connection.close()