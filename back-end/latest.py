import sqlite3


def physics_table():
    try:
        conn = sqlite3.connect('Teacher.sqlite')
        cur = conn.cursor()

        cur.execute('''CREATE TABLE IF NOT EXISTS Single_Correct
                        (Ques_No INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
                        Questions TEXT UNIQUE,
                        Option_1 TEXT, Option_2 TEXT, Option_3 TEXT, Option_4 TEXT, 
                        Answers TEXT)''')

        cur.execute('''CREATE TABLE IF NOT EXISTS Multi_Correct
                        (Ques_No INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
                        Questions TEXT UNIQUE,
                        Option_1 TEXT, Option_2 TEXT, Option_3 TEXT, Option_4 TEXT,
                        Answers TEXT)''')

        cur.execute('''CREATE TABLE IF NOT EXISTS Integral_Correct
                        (Ques_No INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
                        Questions TEXT UNIQUE,
                        Option_1 TEXT, Option_2 TEXT, Option_3 TEXT, Option_4 TEXT,
                        Answers TEXT)''')

        cur.execute('''CREATE TABLE IF NOT EXISTS Physics
                        (Single_ID INTEGER NOT NULL,
                        Multi_ID INTEGER NOT NULL,
                        Integral_ID INTEGER NOT NULL,
                        FOREIGN KEY (Single_ID) REFERENCES Single_Correct (Ques_No),
                        FOREIGN KEY (Multi_ID) REFERENCES Multi_Correct (Ques_No),
                        FOREIGN KEY (Integral_ID) REFERENCES Integral_Correct (Ques_No))''')

        conn.commit()
        cur.close()

    except sqlite3.Error as error:
        print('Failed to insert data _____ SQLite Table', error)
    finally:
        if conn:
            conn.close()
            print('The SQLite connection is closed')


def single_insert_physics(ques, opt1, opt2, opt3, opt4, ans):
    try:
        physics_table()

        conn = sqlite3.connect('Teacher.sqlite')
        cur = conn.cursor()

        cur.execute('''INSERT INTO Single_Correct (Questions, Option_1, Option_2, Option_3, Option_4, Answers)
                        VALUES (?, ?, ?, ?, ?, ?)''', (ques, opt1, opt2, opt3, opt4, ans))

        last_id = cur.lastrowid

        cur.execute('''INSERT INTO Physics (Single_ID, Multi_ID, Integral_ID)
                        VALUES (?, ?, ?)''', (last_id, last_id, last_id))

        print("Record inserted successfully into Single Correct table ", cur.rowcount)

        conn.commit()
        cur.close()

    except sqlite3.Error as error:
        print('Failed to insert data into Single Correct Table', error)
    finally:
        if conn:
            conn.close()
            print('The SQLite connection is closed')


def multi_insert_physics(ques, opt1, opt2, opt3, opt4, ans):
    try:
        physics_table()

        conn = sqlite3.connect('Teacher.sqlite')
        cur = conn.cursor()

        cur.execute('''INSERT INTO Multi_Correct (Questions, Option_1, Option_2, Option_3, Option_4, Answers)
                        VALUES (?, ?, ?, ?, ?, ?)''', (ques, opt1, opt2, opt3, opt4, ans))

        last_id = cur.lastrowid

        cur.execute('''INSERT INTO Physics (Single_ID, Multi_ID, Integral_ID)
                        VALUES (?, ?, ?)''', (last_id, last_id, last_id))

        print("Record inserted successfully into Multi Correct table ", cur.rowcount)

        conn.commit()
        cur.close()

    except sqlite3.Error as error:
        print('Failed to insert data into Multi_Correct Table', error)
    finally:
        if conn:
            conn.close()
            print('The SQLite connection is closed')

def integral_insert_physics(ques, opt1, opt2, opt3, opt4, ans):
    try:
        physics_table()

        conn = sqlite3.connect('Teacher.sqlite')
        cur = conn.cursor()

        cur.execute('''INSERT INTO Integral_Correct (Questions, Option_1, Option_2, Option_3, Option_4, Answers)
                        VALUES (?, ?, ?, ?, ?, ?)''', (ques, opt1, opt2, opt3, opt4, ans))

        last_id = cur.lastrowid

        cur.execute('''INSERT INTO Physics (Single_ID, Multi_ID, Integral_ID)
                        VALUES (?, ?, ?)''', (last_id, last_id, last_id))

        print("Record inserted successfully into Integral Correct table ", cur.rowcount)

        conn.commit()
        cur.close()

    except sqlite3.Error as error:
        print('Failed to insert data into Integral Correct Table', error)
    finally:
        if conn:
            conn.close()
            print('The SQLite connection is closed')


def fetch_physics_table(ques):
    conn = sqlite3.connect('Teacher.sqlite')
    cur = conn.cursor()

    cur.execute('''SELECT Ques_No, Questions, Option_1, Option_2, Option_3, Option_4, Answers
                    FROM Single_Correct, Physics
                    WHERE Single_Correct.? = Physics.Single_ID''', (ques, ))

    records = cur.fetchall()

    for row in records:
        print(list(row))


if __name__ == '__main__':
    print("\n ***** Welcome Teachers ***** \n")
    print("1. Physics")
    print("2. Chemistry")
    print("3. Mathematics")
    print("4. Exit \n")

    val = input("Select any one subject: ")

    if val == '1':
        print("\n ***** Menu ***** \n")
        print("1. Single Correct")
        print("2. Multi Correct")
        print("3. Integral Correct")

        stuff = input("Select any one of it: ")

        if stuff == '1':
            print("\n ***** Menu ***** \n")
            print("1. Insert question")
            print("2. Fetch Data")
            print("3. Update question")
            print("4. Delete question")
            print("5. Delete data")
            print("6. Exit \n")

            choice = input("Enter your choice: ")

            if choice == '1':
                for i in range(0, 4):

                    ques = input('Enter the {} question: '.format(i + 1))
                    opt1 = input('Enter the {} Option: '.format(1))
                    opt2 = input('Enter the {} Option: '.format(2))
                    opt3 = input('Enter the {} Option: '.format(3))
                    opt4 = input('Enter the {} Option: '.format(4))
                    ans = input('Enter the correct answer: ')

                    single_insert_physics(ques, opt1, opt2, opt3, opt4, ans)

        if stuff == '2':
            print("\n ***** Menu ***** \n")
            print("1. Insert question")
            print("2. Fetch Data")
            print("3. Update question")
            print("4. Delete question")
            print("5. Delete data")
            print("6. Exit \n")

            choice = input("Enter your choice: ")

            if choice == '1':
                for i in range(0, 4):

                    ques = input('Enter the {} question: '.format(i + 1))
                    opt1 = input('Enter the {} Option: '.format(1))
                    opt2 = input('Enter the {} Option: '.format(2))
                    opt3 = input('Enter the {} Option: '.format(3))
                    opt4 = input('Enter the {} Option: '.format(4))
                    ans = input('Enter the correct answer: ')

                    multi_insert_physics(ques, opt1, opt2, opt3, opt4, ans)

        if stuff == '3':
            print("\n ***** Menu ***** \n")
            print("1. Insert question")
            print("2. Fetch Data")
            print("3. Update question")
            print("4. Delete question")
            print("5. Delete data")
            print("6. Exit \n")

            choice = input("Enter your choice: ")

            if choice == '1':
                for i in range(0, 4):

                    ques = input('Enter the {} question: '.format(i + 1))
                    opt1 = input('Enter the {} Option: '.format(1))
                    opt2 = input('Enter the {} Option: '.format(2))
                    opt3 = input('Enter the {} Option: '.format(3))
                    opt4 = input('Enter the {} Option: '.format(4))
                    ans = input('Enter the correct answer: ')

                    integral_insert_physics(ques, opt1, opt2, opt3, opt4, ans)

        if stuff == '4':
            print('Thanks for visiting')
            quit()

        # Right now it not working properly
        if choice == '2':
            ques = input('Enter the question number: ')

            fetch_physics_table(ques)