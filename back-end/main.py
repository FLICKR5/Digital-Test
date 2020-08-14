import sqlite3

# Create Database
conn = sqlite3.connect('Digital-Test.sqlite')
cur = conn.cursor()

# Create Table
cur.execute('''CREATE TABLE IF NOT EXISTS Teacher
            (Id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
             Questions TEXT,
             Options TEXT,
             Answers TEXT)''')

cur.execute('''CREATE TABLE IF NOT EXISTS Student
            (Id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE, 
             Questions TEXT,
             Options TEXT)''')
conn.commit()
