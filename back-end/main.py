import sqlite3
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# Create Database
conn = sqlite3.connect('Quiz.sqlite')
cur = conn.cursor()

# Create Table
cur.execute('''CREATE TABLE IF NOT EXISTS Teacher
            (Questions TEXT, Options TEXT, Answers TEXT)''')

conn.close()
