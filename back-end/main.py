import sqlite3

conn = sqlite3.connect('Quiz.sqlite')
cur = conn.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS Teacher
            (Questions TEXT, Options TEXT, Answers TEXT)''')

cur.close()
conn.close()
