import sqlite3

conn = sqlite3.connect('Quiz.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Teachers')
cur.execute('CREATE TABLE Teachers (Questions TEXT, Options TEXT, Answer TEXT)')

conn.close()