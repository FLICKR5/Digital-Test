import sqlite3
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

conn = sqlite3.connect('Quiz.sqlite')
cur = conn.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS Teacher
            (Id INTEGER PRIMARY KEY, Questions TEXT, Options TEXT, Answers TEXT)''')
cur.execute('''CREATE TABLE IF NOT EXISTS Student
            (Id INTEGER PRIMARY KEY, Questions TEXT, Options TEXT)''')

conn.close()