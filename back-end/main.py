import sqlite3

    
def Insert_Sqlite_Table(ques, opt1, opt2, opt3, opt4, ans):
    try:
        # Create Database
        conn = sqlite3.connect('Digital-Test.sqlite')
        cur = conn.cursor()

        # Create Table
        cur.execute('''CREATE TABLE IF NOT EXISTS Teacher
                    (Ques_No INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
                    ques TEXT,
                    opt1 TEXT, opt2 TEXT, opt3 TEXT, opt4 TEXT,
                    ans TEXT)''')

        cur.execute('''INSERT INTO Teacher (Questions, Options_1, Options_2, Options_3, Options_4, Answers)
                    VALUES (?, ?, ?, ?, ?, ?)''', (ques, opt1, opt2, opt3, opt4, ans))

        conn.commit()


    except sqlite3.Error as error:
        print('Failed to insert data into sqlite table', error)
    finally:
        if conn:
            conn.close()
            print('The SQLite connection is closed')


if __name__ == '__main__':
    for i in range(0, 6):

        n = 1
        ques = input('Enter the {} question: '.format(i + 1))
        opt1 = input('Enter the {} Option: '.format(n))
        opt2 = input('Enter the {} Option: '.format(n + 1))
        opt3 = input('Enter the {} Option: '.format(n + 2))
        opt4 = input('Enter the {} Option: '.format(n + 3))  
        ans = input('Enter the correct answer: '.format(n))

        Insert_Sqlite_Table(ques, opt1, opt2, opt3, opt4, ans)