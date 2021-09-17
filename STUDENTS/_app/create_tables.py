import sqlite3

connection = sqlite3.connect('Mydatabasefile.db')
cursor = connection.cursor()

Usertable = "CREATE TABLE IF NOT EXISTS Users(id INTEGER PRIMARY KEY, Username text, Password text)"
cursor.execute(Usertable)

Student_table = "CREATE TABLE IF NOT EXISTS Students(Name text, FamilyName text, Age int, CollegeName text, Student_id text, Stream text, ClassSection text)"
cursor.execute(Student_table)

connection.commit()
connection.close()

