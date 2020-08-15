import sqlite3

def Create_Sqlite_Table():
    try:
        # Create Database
        conn = sqlite3.connect('Digital-Test.sqlite')
        cur = conn.cursor()

        # Create Table
        cur.execute('''CREATE TABLE IF NOT EXISTS Teacher
                    (Ques_No INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
                    Questions TEXT,
                    Options_1 TEXT, Options_2 TEXT, Options_3 TEXT, Options_4 TEXT,
                    Answers TEXT)''')

        n = 0
        while True:
            n += 1

            choice = input("What do you want to do ('INSERT, UPDATE, DROP, QUIT'): ")

            if choice == 'INSERT' or choice  == 'Insert' or choice == 'insert':
                Ques = input('Enter the {} question: '.format(n))
                Options_1 = input('Enter the {} Option: '.format(n))
                Options_2 = input('Enter the {} Option: '.format(n + 1))
                Options_3 = input('Enter the {} Option: '.format(n + 2))
                Options_4 = input('Enter the {} Option: '.format(n + 3))  
                Ans = input('Enter the correct answer: '.format(n))


                cur.execute('''INSERT INTO Teacher (Questions, Options_1, Options_2, Options_3, Options_4, Answers)
                            VALUES (?, ?, ?, ?, ?, ?)''', (Ques, Options_1, Options_2, Options_3, Options_4, Ans))

                conn.commit()

                check = input('Do you want to continue or not (Y/N): ')
                if check == 'Y' or check == 'y':
                    continue
                else:
                    break

    except sqlite3.Error as error:
        print('Failed to insert data into sqlite table', error)
    finally:
        if conn:
            conn.close()
            print('The SQLite connection is closed')


if __name__ == '__main__':
    Insert_Sqlite_Table()