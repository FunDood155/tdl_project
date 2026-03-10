import sqlite3

con = sqlite3.connect("tasks.db", check_same_thread=False)
cursor = con.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS tdl_table (
    num INTEGER PRIMARY KEY AUTOINCREMENT,
    work TEXT,
    date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    status TEXT
)
""")

con.commit()

# ---------- FUNCTIONS ----------

def add_activity(work):
    query = "INSERT INTO tdl_table (work,status) VALUES (?,?)"
    cursor.execute(query,(work,"no"))
    con.commit()

def remove_activity(num):
    query = "DELETE FROM tdl_table WHERE num=?"
    cursor.execute(query,(num,))
    con.commit()

def display_activity():
    query = "SELECT * FROM tdl_table"
    cursor.execute(query)
    return cursor.fetchall()

def table_clear():
    cursor.execute("TRUNCATE TABLE tdl_table")
    con.commit()

def mark_done(num):
    a = "update tdl_table set status='done' where num=?"
    cursor.execute(a,(num,))
    con.commit()

# ---------- MAIN ----------
if __name__=="__main__":
    while True:

        print("\n1.Add  2.Remove  3.Display  4.Clear  5.Exit")
        ch = int(input("Enter choice: "))

        if ch == 1:
            work = input("Enter activity: ")
            add_activity(work)

        elif ch == 2:
            num = int(input("Enter activity number: "))
            remove_activity(num)

        elif ch == 3:
            rows = display_activity()
            for r in rows:
                print(r)

        elif ch == 4:
            table_clear()

        elif ch == 5:
            print("Exited successfully")
            break


#old sql code


# import mysql.connector

# # ---------- DATABASE CONNECTION ----------
# def get_connection():
#     return mysql.connector.connect(
#         host="localhost",
#         user="root",
#         password="root155",
#         database="tdldb"
#     )

# con = get_connection()
# cursor = con.cursor()

# ---------- CREATE TABLE ----------
# cursor.execute("""
# CREATE TABLE IF NOT EXISTS tdl_table (
#     num INT AUTO_INCREMENT PRIMARY KEY,
#     work VARCHAR(99),
#     date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
#     status VARCHAR(99)
# )
# """)
