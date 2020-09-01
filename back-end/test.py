import sqlite3



# *************************************************************************************************************
# *********************************************** Physics Table ***********************************************
# *************************************************************************************************************

def physics_table():
    try:
        conn = sqlite3.connect('Teacher.sqlite')
        cur = conn.cursor()

        cur.execute('''CREATE TABLE IF NOT EXISTS Physics_Single_Correct
                        (Ques_No INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
                        Questions TEXT UNIQUE,
                        Option_1 TEXT, Option_2 TEXT, Option_3 TEXT, Option_4 TEXT, 
                        Answers TEXT)''')

        cur.execute('''CREATE TABLE IF NOT EXISTS Physics_Multi_Correct
                        (Ques_No INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
                        Questions TEXT UNIQUE,
                        Option_1 TEXT, Option_2 TEXT, Option_3 TEXT, Option_4 TEXT,
                        Answers TEXT)''')

        cur.execute('''CREATE TABLE IF NOT EXISTS Physics_Integral_Correct
                        (Ques_No INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
                        Questions TEXT UNIQUE,
                        Option_1 TEXT, Option_2 TEXT, Option_3 TEXT, Option_4 TEXT,
                        Answers TEXT)''')

        conn.commit()
        cur.close()

    except sqlite3.Error as error:
        print('Failed to create Physics SQLite Table', error)
    finally:
        if conn:
            conn.close()
            print('The SQLite connection is closed')


# ******************************************* Insert into Physics Table *******************************************

def insert_physics_single(ques, opt1, opt2, opt3, opt4, ans):
    try:
        physics_table()

        conn = sqlite3.connect('Teacher.sqlite')
        cur = conn.cursor()

        cur.execute('''INSERT INTO Physics_Single_Correct (Questions, Option_1, Option_2, Option_3, Option_4, Answers)
                        VALUES (?, ?, ?, ?, ?, ?)''', (ques, opt1, opt2, opt3, opt4, ans))

        print("Record inserted successfully into Single Correct Physics Table ", cur.rowcount)

        conn.commit()
        cur.close()

    except sqlite3.Error as error:
        print('Failed to insert data into Single Correct Physics Table', error)
    finally:
        if conn:
            conn.close()
            print('The SQLite connection is closed')


def insert_physics_multi(ques, opt1, opt2, opt3, opt4, ans):
    try:
        physics_table()

        conn = sqlite3.connect('Teacher.sqlite')
        cur = conn.cursor()

        cur.execute('''INSERT INTO Physics_Multi_Correct (Questions, Option_1, Option_2, Option_3, Option_4, Answers)
                        VALUES (?, ?, ?, ?, ?, ?)''', (ques, opt1, opt2, opt3, opt4, ans))

        print("Record inserted successfully into Multi Correct Physics table ", cur.rowcount)

        conn.commit()
        cur.close()

    except sqlite3.Error as error:
        print('Failed to insert data into Multi Correct Physics Table', error)
    finally:
        if conn:
            conn.close()
            print('The SQLite connection is closed')


def insert_physics_integral(ques, opt1, opt2, opt3, opt4, ans):
    try:
        physics_table()

        conn = sqlite3.connect('Teacher.sqlite')
        cur = conn.cursor()

        cur.execute('''INSERT INTO Physics_Integral_Correct (Questions, Option_1, Option_2, Option_3, Option_4, Answers)
                        VALUES (?, ?, ?, ?, ?, ?)''', (ques, opt1, opt2, opt3, opt4, ans))

        print("Record inserted successfully into Integral Correct Physics table ", cur.rowcount)

        conn.commit()
        cur.close()

    except sqlite3.Error as error:
        print('Failed to insert data into Integral Correct Physics Table', error)
    finally:
        if conn:
            conn.close()
            print('The SQLite connection is closed')


# ******************************************* Update into Physics Table *******************************************

def update_physics_single(ques_value, ques, opt1, opt2, opt3, opt4, ans):
    try:
        conn = sqlite3.connect('Teacher.sqlite')
        cur = conn.cursor()
        print("Connected to SQLite")

        cur.execute('''SELECT * FROM Physics_Single_Correct WHERE Ques_No = ?''', (ques_value, ))
        print("Reading single row")

        
        cur.fetchone()
        cur.execute('''UPDATE Physics_Single_Correct SET Questions = ?, Option_1 = ?, Option_2 = ?, Option_3 = ?, Option_4 = ?, Answers = ?
                        WHERE Ques_NO = ?''', (ques, opt1, opt2, opt3, opt4, ans, ques_value))

        print("Total", cur.rowcount, "Records updated successfully")

        conn.commit()
        cur.close()

    except sqlite3.Error as error:
        print("Failed to update records of Physics Single Correct SQLite Table", error)
    finally:
        if (conn):
            conn.close()
            print("The SQLite connection is closed")


def update_physics_multi(ques_value, ques, opt1, opt2, opt3, opt4, ans):
    try:
        conn = sqlite3.connect('Teacher.sqlite')
        cur = conn.cursor()
        print("Connected to SQLite")

        cur.execute('''SELECT * FROM Physics_Multi_Correct WHERE Ques_No = ?''', (ques_value, ))
        print("Reading single row")

        
        cur.fetchone()
        cur.execute('''UPDATE Physics_Multi_Correct SET Questions = ?, Option_1 = ?, Option_2 = ?, Option_3 = ?, Option_4 = ?, Answers = ?
                        WHERE Ques_NO = ?''', (ques, opt1, opt2, opt3, opt4, ans, ques_value))

        print("Total", cur.rowcount, "Records updated successfully")

        conn.commit()
        cur.close()

    except sqlite3.Error as error:
        print("Failed to update records of Physics Multi Correct SQLite Table", error)
    finally:
        if (conn):
            conn.close()
            print("The SQLite connection is closed")


def update_physics_integral(ques_value, ques, opt1, opt2, opt3, opt4, ans):
    try:
        conn = sqlite3.connect('Teacher.sqlite')
        cur = conn.cursor()
        print("Connected to SQLite")

        cur.execute('''SELECT * FROM Physics_Integral_Correct WHERE Ques_No = ?''', (ques_value, ))
        print("Reading single row")

        
        cur.fetchone()
        cur.execute('''UPDATE Physics_Integral_Correct SET Questions = ?, Option_1 = ?, Option_2 = ?, Option_3 = ?, Option_4 = ?, Answers = ?
                        WHERE Ques_NO = ?''', (ques, opt1, opt2, opt3, opt4, ans, ques_value))

        print("Total", cur.rowcount, "Records updated successfully")

        conn.commit()
        cur.close()

    except sqlite3.Error as error:
        print("Failed to update records of Physics Integral Correct SQLite Table", error)
    finally:
        if (conn):
            conn.close()
            print("The SQLite connection is closed")


# ******************************************** Main function of Physics ********************************************

def physics(stuff, data, ques, opt1, opt2, opt3, opt4, ans):
    if stuff == '1':
        if data == '1':
            insert_physics_single(ques, opt1, opt2, opt3, opt4, ans)
        elif data == '3':
            ques_value = input('\nEnter the question number where you want to update: ')
            update_physics_single(ques_value, ques, opt1, opt2, opt3, opt4, ans)

    elif stuff == '2':
        if data == '1':
            insert_physics_multi(ques, opt1, opt2, opt3, opt4, ans)
        elif data == '3':
            ques_value = input('\nEnter the question number where you want to update: ')
            update_physics_multi(ques_value, ques, opt1, opt2, opt3, opt4, ans)

    elif stuff == '3':
        if data == '1':
            insert_physics_integral(ques, opt1, opt2, opt3, opt4, ans)
        elif data == '3':
            ques_value = input('\nEnter the question number where you want to update: ')
            update_physics_integral(ques_value, ques, opt1, opt2, opt3, opt4, ans)



# ***************************************************************************************************************
# *********************************************** Chemistry Table ***********************************************
# ***************************************************************************************************************

def chemistry_table():
    try:
        conn = sqlite3.connect('Teacher.sqlite')
        cur = conn.cursor()

        cur.execute('''CREATE TABLE IF NOT EXISTS Chemistry_Single_Correct
                        (Ques_No INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
                        Questions TEXT UNIQUE,
                        Option_1 TEXT, Option_2 TEXT, Option_3 TEXT, Option_4 TEXT, 
                        Answers TEXT)''')

        cur.execute('''CREATE TABLE IF NOT EXISTS Chemistry_Multi_Correct
                        (Ques_No INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
                        Questions TEXT UNIQUE,
                        Option_1 TEXT, Option_2 TEXT, Option_3 TEXT, Option_4 TEXT,
                        Answers TEXT)''')

        cur.execute('''CREATE TABLE IF NOT EXISTS Chemistry_Integral_Correct
                        (Ques_No INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
                        Questions TEXT UNIQUE,
                        Option_1 TEXT, Option_2 TEXT, Option_3 TEXT, Option_4 TEXT,
                        Answers TEXT)''')

        conn.commit()
        cur.close()

    except sqlite3.Error as error:
        print('Failed to create Chemistry SQLite Table', error)
    finally:
        if conn:
            conn.close()
            print('The SQLite connection is closed')


# ******************************************* Insert into Chemistry Table *******************************************

def insert_chemistry_single(ques, opt1, opt2, opt3, opt4, ans):
    try:
        chemistry_table()

        conn = sqlite3.connect('Teacher.sqlite')
        cur = conn.cursor()

        cur.execute('''INSERT INTO Chemistry_Single_Correct (Questions, Option_1, Option_2, Option_3, Option_4, Answers)
                        VALUES (?, ?, ?, ?, ?, ?)''', (ques, opt1, opt2, opt3, opt4, ans))

        print("Record inserted successfully into Single Correct Chemistry table ", cur.rowcount)

        conn.commit()
        cur.close()

    except sqlite3.Error as error:
        print('Failed to insert data into Single Correct Chemistry Table', error)
    finally:
        if conn:
            conn.close()
            print('The SQLite connection is closed')


def insert_chemistry_multi(ques, opt1, opt2, opt3, opt4, ans):
    try:
        chemistry_table()

        conn = sqlite3.connect('Teacher.sqlite')
        cur = conn.cursor()

        cur.execute('''INSERT INTO Chemistry_Multi_Correct (Questions, Option_1, Option_2, Option_3, Option_4, Answers)
                        VALUES (?, ?, ?, ?, ?, ?)''', (ques, opt1, opt2, opt3, opt4, ans))

        print("Record inserted successfully into Multi Correct Chemistry table ", cur.rowcount)

        conn.commit()
        cur.close()

    except sqlite3.Error as error:
        print('Failed to insert data into Multi Correct Chemistry Table', error)
    finally:
        if conn:
            conn.close()
            print('The SQLite connection is closed')


def insert_chemistry_integral(ques, opt1, opt2, opt3, opt4, ans):
    try:
        chemistry_table()

        conn = sqlite3.connect('Teacher.sqlite')
        cur = conn.cursor()

        cur.execute('''INSERT INTO Chemistry_Integral_Correct (Questions, Option_1, Option_2, Option_3, Option_4, Answers)
                        VALUES (?, ?, ?, ?, ?, ?)''', (ques, opt1, opt2, opt3, opt4, ans))

        print("Record inserted successfully into Integral Correct Chemistry table ", cur.rowcount)

        conn.commit()
        cur.close()

    except sqlite3.Error as error:
        print('Failed to insert data into Integral Correct Chemistry Table', error)
    finally:
        if conn:
            conn.close()
            print('The SQLite connection is closed')


# ******************************************* Update into Chemistry Table *******************************************

def update_chemistry_single(ques_value, ques, opt1, opt2, opt3, opt4, ans):
    try:
        conn = sqlite3.connect('Teacher.sqlite')
        cur = conn.cursor()
        print("Connected to SQLite")

        cur.execute('''SELECT * FROM Chemistry_Single_Correct WHERE Ques_No = ?''', (ques_value, ))
        print("Reading single row")

        
        cur.fetchone()
        cur.execute('''UPDATE Chemistry_Single_Correct SET Questions = ?, Option_1 = ?, Option_2 = ?, Option_3 = ?, Option_4 = ?, Answers = ?
                        WHERE Ques_NO = ?''', (ques, opt1, opt2, opt3, opt4, ans, ques_value))

        print("Total", cur.rowcount, "Records updated successfully")

        conn.commit()
        cur.close()

    except sqlite3.Error as error:
        print("Failed to update records of Chemistry Single Correct SQLite Table", error)
    finally:
        if (conn):
            conn.close()
            print("The SQLite connection is closed")


def update_chemistry_multi(ques_value, ques, opt1, opt2, opt3, opt4, ans):
    try:
        conn = sqlite3.connect('Teacher.sqlite')
        cur = conn.cursor()
        print("Connected to SQLite")

        cur.execute('''SELECT * FROM Chemistry_Multi_Correct WHERE Ques_No = ?''', (ques_value, ))
        print("Reading single row")

        
        cur.fetchone()
        cur.execute('''UPDATE Chemistry_Multi_Correct SET Questions = ?, Option_1 = ?, Option_2 = ?, Option_3 = ?, Option_4 = ?, Answers = ?
                        WHERE Ques_NO = ?''', (ques, opt1, opt2, opt3, opt4, ans, ques_value))

        print("Total", cur.rowcount, "Records updated successfully")

        conn.commit()
        cur.close()

    except sqlite3.Error as error:
        print("Failed to update records of Chemistry Multi Correct SQLite Table", error)
    finally:
        if (conn):
            conn.close()
            print("The SQLite connection is closed")


def update_chemistry_integral(ques_value, ques, opt1, opt2, opt3, opt4, ans):
    try:
        conn = sqlite3.connect('Teacher.sqlite')
        cur = conn.cursor()
        print("Connected to SQLite")

        cur.execute('''SELECT * FROM Chemistry_Integral_Correct WHERE Ques_No = ?''', (ques_value, ))
        print("Reading single row")

        
        cur.fetchone()
        cur.execute('''UPDATE Chemistry_Integral_Correct SET Questions = ?, Option_1 = ?, Option_2 = ?, Option_3 = ?, Option_4 = ?, Answers = ?
                        WHERE Ques_NO = ?''', (ques, opt1, opt2, opt3, opt4, ans, ques_value))

        print("Total", cur.rowcount, "Records updated successfully")

        conn.commit()
        cur.close()

    except sqlite3.Error as error:
        print("Failed to update records of Chemistry Integral Correct SQLite Table", error)
    finally:
        if (conn):
            conn.close()
            print("The SQLite connection is closed")


# ******************************************* Main function of Chemistry *******************************************

def chemistry(stuff, data, ques, opt1, opt2, opt3, opt4, ans):
    if stuff == '1':
        if data == '1':
            insert_chemistry_single(ques, opt1, opt2, opt3, opt4, ans)
        elif data == '3':
            ques_value = input('\nEnter the question number where you want to update: ')
            update_chemistry_single(ques_value, ques, opt1, opt2, opt3, opt4, ans)

    elif stuff == '2':
        if data == '1':
            insert_chemistry_multi(ques, opt1, opt2, opt3, opt4, ans)
        elif data == '3':
            ques_value = input('\nEnter the question number where you want to update: ')
            update_chemistry_multi(ques_value, ques, opt1, opt2, opt3, opt4, ans)

    elif stuff == '3':
        if data == '1':
            insert_chemistry_integral(ques, opt1, opt2, opt3, opt4, ans)
        elif data == '3':
            ques_value = input('\nEnter the question number where you want to update: ')
            update_chemistry_integral(ques_value, ques, opt1, opt2, opt3, opt4, ans)



# **********************************************************************************************************
# *********************************************** Math Table ***********************************************
# **********************************************************************************************************

def math_table():
    try:
        conn = sqlite3.connect('Teacher.sqlite')
        cur = conn.cursor()

        cur.execute('''CREATE TABLE IF NOT EXISTS Math_Single_Correct
                        (Ques_No INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
                        Questions TEXT UNIQUE,
                        Option_1 TEXT, Option_2 TEXT, Option_3 TEXT, Option_4 TEXT, 
                        Answers TEXT)''')

        cur.execute('''CREATE TABLE IF NOT EXISTS Math_Multi_Correct
                        (Ques_No INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
                        Questions TEXT UNIQUE,
                        Option_1 TEXT, Option_2 TEXT, Option_3 TEXT, Option_4 TEXT,
                        Answers TEXT)''')

        cur.execute('''CREATE TABLE IF NOT EXISTS Math_Integral_Correct
                        (Ques_No INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
                        Questions TEXT UNIQUE,
                        Option_1 TEXT, Option_2 TEXT, Option_3 TEXT, Option_4 TEXT,
                        Answers TEXT)''')

        conn.commit()
        cur.close()

    except sqlite3.Error as error:
        print('Failed to create Math SQLite Table', error)
    finally:
        if conn:
            conn.close()
            print('The SQLite connection is closed')


# ******************************************* Insert into Math Table *******************************************

def insert_math_single(ques, opt1, opt2, opt3, opt4, ans):
    try:
        math_table()

        conn = sqlite3.connect('Teacher.sqlite')
        cur = conn.cursor()

        cur.execute('''INSERT INTO Math_Single_Correct (Questions, Option_1, Option_2, Option_3, Option_4, Answers)
                        VALUES (?, ?, ?, ?, ?, ?)''', (ques, opt1, opt2, opt3, opt4, ans))

        print("Record inserted successfully into Single Correct Math table ", cur.rowcount)

        conn.commit()
        cur.close()

    except sqlite3.Error as error:
        print('Failed to insert data into Single Correct Math Table', error)
    finally:
        if conn:
            conn.close()
            print('The SQLite connection is closed')


def insert_math_multi(ques, opt1, opt2, opt3, opt4, ans):
    try:
        math_table()

        conn = sqlite3.connect('Teacher.sqlite')
        cur = conn.cursor()

        cur.execute('''INSERT INTO Math_Multi_Correct (Questions, Option_1, Option_2, Option_3, Option_4, Answers)
                        VALUES (?, ?, ?, ?, ?, ?)''', (ques, opt1, opt2, opt3, opt4, ans))

        print("Record inserted successfully into Multi Correct Math table ", cur.rowcount)

        conn.commit()
        cur.close()

    except sqlite3.Error as error:
        print('Failed to insert data into Multi Correct Math Table', error)
    finally:
        if conn:
            conn.close()
            print('The SQLite connection is closed')


def insert_math_integral(ques, opt1, opt2, opt3, opt4, ans):
    try:
        math_table()

        conn = sqlite3.connect('Teacher.sqlite')
        cur = conn.cursor()

        cur.execute('''INSERT INTO Math_Integral_Correct (Questions, Option_1, Option_2, Option_3, Option_4, Answers)
                        VALUES (?, ?, ?, ?, ?, ?)''', (ques, opt1, opt2, opt3, opt4, ans))

        print("Record inserted successfully into Integral Correct Math table ", cur.rowcount)

        conn.commit()
        cur.close()

    except sqlite3.Error as error:
        print('Failed to insert data into Integral Correct Math Table', error)
    finally:
        if conn:
            conn.close()
            print('The SQLite connection is closed')


# ******************************************* Update into Math Table *******************************************

def update_math_single(ques_value, ques, opt1, opt2, opt3, opt4, ans):
    try:
        conn = sqlite3.connect('Teacher.sqlite')
        cur = conn.cursor()
        print("Connected to SQLite")

        cur.execute('''SELECT * FROM Math_Single_Correct WHERE Ques_No = ?''', (ques_value, ))
        print("Reading single row")

        
        cur.fetchone()
        cur.execute('''UPDATE Math_Single_Correct SET Questions = ?, Option_1 = ?, Option_2 = ?, Option_3 = ?, Option_4 = ?, Answers = ?
                        WHERE Ques_NO = ?''', (ques, opt1, opt2, opt3, opt4, ans, ques_value))

        print("Total", cur.rowcount, "Records updated successfully")

        conn.commit()
        cur.close()

    except sqlite3.Error as error:
        print("Failed to update records of Math Single Correct SQLite Table", error)
    finally:
        if (conn):
            conn.close()
            print("The SQLite connection is closed")


def update_math_multi(ques_value, ques, opt1, opt2, opt3, opt4, ans):
    try:
        conn = sqlite3.connect('Teacher.sqlite')
        cur = conn.cursor()
        print("Connected to SQLite")

        cur.execute('''SELECT * FROM Math_Multi_Correct WHERE Ques_No = ?''', (ques_value, ))
        print("Reading single row")

        
        cur.fetchone()
        cur.execute('''UPDATE Math_Multi_Correct SET Questions = ?, Option_1 = ?, Option_2 = ?, Option_3 = ?, Option_4 = ?, Answers = ?
                        WHERE Ques_NO = ?''', (ques, opt1, opt2, opt3, opt4, ans, ques_value))

        print("Total", cur.rowcount, "Records updated successfully")

        conn.commit()
        cur.close()

    except sqlite3.Error as error:
        print("Failed to update records of Math Multi Correct SQLite Table", error)
    finally:
        if (conn):
            conn.close()
            print("The SQLite connection is closed")


def update_math_integral(ques_value, ques, opt1, opt2, opt3, opt4, ans):
    try:
        conn = sqlite3.connect('Teacher.sqlite')
        cur = conn.cursor()
        print("Connected to SQLite")

        cur.execute('''SELECT * FROM Math_Integral_Correct WHERE Ques_No = ?''', (ques_value, ))
        print("Reading single row")

        
        cur.fetchone()
        cur.execute('''UPDATE Math_Integral_Correct SET Questions = ?, Option_1 = ?, Option_2 = ?, Option_3 = ?, Option_4 = ?, Answers = ?
                        WHERE Ques_NO = ?''', (ques, opt1, opt2, opt3, opt4, ans, ques_value))

        print("Total", cur.rowcount, "Records updated successfully")

        conn.commit()
        cur.close()

    except sqlite3.Error as error:
        print("Failed to update records of Math Integral Correct SQLite Table", error)
    finally:
        if (conn):
            conn.close()
            print("The SQLite connection is closed")


# ******************************************** Main function of Math ********************************************

def math(stuff, data, ques, opt1, opt2, opt3, opt4, ans):
    if stuff == '1':
        if data == '1':
            insert_math_single(ques, opt1, opt2, opt3, opt4, ans)
        elif data == '3':
            ques_value = input('\nEnter the question number where you want to update: ')
            update_math_single(ques_value, ques, opt1, opt2, opt3, opt4, ans)

    elif stuff == '2':
        if data == '1':
            insert_math_multi(ques, opt1, opt2, opt3, opt4, ans)
        elif data == '3':
            ques_value = input('\nEnter the question number where you want to update: ')
            update_math_multi(ques_value, ques, opt1, opt2, opt3, opt4, ans)

    elif stuff == '3':
        if data == '1':
            insert_math_integral(ques, opt1, opt2, opt3, opt4, ans)
        elif data == '3':
            ques_value = input('\nEnter the question number where you want to update: ')
            update_math_integral(ques_value, ques, opt1, opt2, opt3, opt4, ans)



# ********************************************************************************************************
# *********************************************** Fetching ***********************************************
# ********************************************************************************************************


# **************************************** Fetching Physics Table ****************************************

def fetch_physics_single(ques_value):
    try:
        conn = sqlite3.connect('Teacher.sqlite')
        cur = conn.cursor()
        print("Connected to SQLite")

        cur.execute('''SELECT * FROM Physics_Single_Correct WHERE Ques_No = ?''', (ques_value))

        records = cur.fetchall()

        for row in records:
            print('Question Number {} is Fetched'.format(ques_value))
            return list(row)

        cur.close()

    except sqlite3.Error as error:
        print("Failed to Fetch Record of SQLite Physics Single Table", error)
    finally:
        if (conn):
            conn.close()
            print("SQLite connection is closed")


def fetch_physics_multi(ques_value):
    try:
        conn = sqlite3.connect('Teacher.sqlite')
        cur = conn.cursor()
        print("Connected to SQLite")

        cur.execute('''SELECT * FROM Physics_Multi_Correct WHERE Ques_No = ?''', (ques_value))

        records = cur.fetchall()

        for row in records:
            print('Question Number {} is Fetched'.format(ques_value))
            return list(row)

        cur.close()

    except sqlite3.Error as error:
        print("Failed to Fetch Record of SQLite Physics Multi Table", error)
    finally:
        if (conn):
            conn.close()
            print("SQLite connection is closed")


def fetch_physics_integral(ques_value):
    try:
        conn = sqlite3.connect('Teacher.sqlite')
        cur = conn.cursor()
        print("Connected to SQLite")

        cur.execute('''SELECT * FROM Physics_Integral_Correct WHERE Ques_No = ?''', (ques_value))

        records = cur.fetchall()

        for row in records:
            print('Question Number {} is Fetched'.format(ques_value))
            return list(row)

        cur.close()

    except sqlite3.Error as error:
        print("Failed to Fetch Record of SQLite Physics Integral Table", error)
    finally:
        if (conn):
            conn.close()
            print("SQLite connection is closed")


# *************************************** Fetching Chemistry Table ***************************************

def fetch_chemistry_single(ques_value):
    try:
        conn = sqlite3.connect('Teacher.sqlite')
        cur = conn.cursor()
        print("Connected to SQLite")

        cur.execute('''SELECT * FROM Chemistry_Single_Correct WHERE Ques_No = ?''', (ques_value))

        records = cur.fetchall()

        for row in records:
            print('Question Number {} is Fetched'.format(ques_value))
            return list(row)

        cur.close()

    except sqlite3.Error as error:
        print("Failed to Fetch Record of SQLite Chemistry Single Table", error)
    finally:
        if (conn):
            conn.close()
            print("SQLite connection is closed")


def fetch_chemistry_multi(ques_value):
    try:
        conn = sqlite3.connect('Teacher.sqlite')
        cur = conn.cursor()
        print("Connected to SQLite")

        cur.execute('''SELECT * FROM Chemistry_Multi_Correct WHERE Ques_No = ?''', (ques_value))

        records = cur.fetchall()

        for row in records:
            print('Question Number {} is Fetched'.format(ques_value))
            return list(row)

        cur.close()

    except sqlite3.Error as error:
        print("Failed to Fetch Record of SQLite Chemistry Multi Table", error)
    finally:
        if (conn):
            conn.close()
            print("SQLite connection is closed")


def fetch_chemistry_integral(ques_value):
    try:
        conn = sqlite3.connect('Teacher.sqlite')
        cur = conn.cursor()
        print("Connected to SQLite")

        cur.execute('''SELECT * FROM Chemistry_Integral_Correct WHERE Ques_No = ?''', (ques_value))

        records = cur.fetchall()

        for row in records:
            print('Question Number {} is Fetched'.format(ques_value))
            return list(row)

        cur.close()

    except sqlite3.Error as error:
        print("Failed to Fetch Record of SQLite Chemistry Integral Table", error)
    finally:
        if (conn):
            conn.close()
            print("SQLite connection is closed")


# ***************************************** Fetching Math Table *****************************************

def fetch_math_single(ques_value):
    try:
        conn = sqlite3.connect('Teacher.sqlite')
        cur = conn.cursor()
        print("Connected to SQLite")

        cur.execute('''SELECT * FROM Math_Single_Correct WHERE Ques_No = ?''', (ques_value))

        records = cur.fetchall()

        for row in records:
            print('Question Number {} is Fetched'.format(ques_value))
            return list(row)

        cur.close()

    except sqlite3.Error as error:
        print("Failed to Fetch Record of SQLite Math Single Table", error)
    finally:
        if (conn):
            conn.close()
            print("SQLite connection is closed")


def fetch_math_multi(ques_value):
    try:
        conn = sqlite3.connect('Teacher.sqlite')
        cur = conn.cursor()
        print("Connected to SQLite")

        cur.execute('''SELECT * FROM Math_Multi_Correct WHERE Ques_No = ?''', (ques_value))

        records = cur.fetchall()

        for row in records:
            print('Question Number {} is Fetched'.format(ques_value))
            return list(row)

        cur.close()

    except sqlite3.Error as error:
        print("Failed to Fetch Record of SQLite Math Multi Table", error)
    finally:
        if (conn):
            conn.close()
            print("SQLite connection is closed")


def fetch_math_integral(ques_value):
    try:
        conn = sqlite3.connect('Teacher.sqlite')
        cur = conn.cursor()
        print("Connected to SQLite")

        cur.execute('''SELECT * FROM Math_Integral_Correct WHERE Ques_No = ?''', (ques_value))

        records = cur.fetchall()

        for row in records:
            print('Question Number {} is Fetched'.format(ques_value))
            return list(row)

        cur.close()

    except sqlite3.Error as error:
        print("Failed to Fetch Record of SQLite Math Integral Table", error)
    finally:
        if (conn):
            conn.close()
            print("SQLite connection is closed")


# *********************************** Main function of Fetching Tables ***********************************

def fetch_table(sub, stuff, ques_value):
    if sub == '1':
        if stuff == '1':
            return fetch_physics_single(ques_value)
        elif stuff == '2':
            return fetch_physics_multi(ques_value)
        elif stuff == '3':
            return fetch_physics_integral(ques_value)

    elif sub == '2':
        if stuff == '1':
            return fetch_chemistry_single(ques_value)
        elif stuff == '2':
            return fetch_chemistry_multi(ques_value)
        elif stuff == '3':
            return fetch_chemistry_integral(ques_value)
    
    elif sub == '3':
        if stuff == '1':
            return fetch_math_single(ques_value)
        elif stuff == '2':
            return fetch_math_multi(ques_value)
        elif stuff == '3':
            return fetch_math_integral(ques_value)


if __name__ == '__main__':
    print("\n ***** Welcome Teachers ***** \n")
    print("1. Physics")
    print("2. Chemistry")
    print("3. Mathematics \n")

    sub = input('Please select the subject: ')

    print("\n ***** Menu ***** \n")
    print("1. Single Correct")
    print("2. Multi Correct")
    print("3. Integral Correct \n")

    stuff = input("Select any one of it: ")

    print("\n ***** Menu ***** \n")
    print("1. Insert question")
    print("2. Fetch Data")
    print("3. Update question")
    print("4. Delete question")
    print("5. Delete data \n")

    data = input('Enter your choice: ')

    if data == '1' or data == '3':
        n = 1
        ques = input('\nEnter the {} question: '.format(n))
        opt1 = input('Enter the {} Option: '.format(1))
        opt2 = input('Enter the {} Option: '.format(2))
        opt3 = input('Enter the {} Option: '.format(3))
        opt4 = input('Enter the {} Option: '.format(4))
        ans = input('Enter the correct answer: ')

        if sub == '1':
            physics(stuff, data, ques, opt1, opt2, opt3, opt4, ans)

        elif sub == '2':
            chemistry(stuff, data, ques, opt1, opt2, opt3, opt4, ans)

        elif sub == '3':
            math(stuff, data, ques, opt1, opt2, opt3, opt4, ans)

    elif data == '2':
        ques_value = input('\nEnter the question no. you want to fetch: ')
        
        print(fetch_table(sub, stuff, ques_value))