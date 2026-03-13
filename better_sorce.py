import sqlite3

con = sqlite3.connect("tasks.db", check_same_thread=False)
cursor = con.cursor()

# ---------- CREATE TABLE ----------

cursor.execute("""
CREATE TABLE IF NOT EXISTS tdl_table (
    num INTEGER PRIMARY KEY AUTOINCREMENT,
    work TEXT,
    date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    status TEXT,
    user_id INTEGER
)
""")

con.commit()


# ---------- FUNCTIONS ----------

def add_activity(work, user_id):
    query = "INSERT INTO tdl_table (work,status,user_id) VALUES (?,?,?)"
    cursor.execute(query,(work,"no",user_id))
    con.commit()


def remove_activity(num):
    query = "DELETE FROM tdl_table WHERE num=?"
    cursor.execute(query,(num,))
    con.commit()


def display_activity(user_id):
    query = "SELECT * FROM tdl_table WHERE user_id=?"
    cursor.execute(query,(user_id,))
    return cursor.fetchall()


def table_clear(user_id):
    cursor.execute("DELETE FROM tdl_table WHERE user_id=?", (user_id,))
    con.commit()


def mark_done(num):
    query = "UPDATE tdl_table SET status='done' WHERE num=?"
    cursor.execute(query,(num,))
    con.commit()


# ---------- MAIN (for terminal testing only) ----------

if __name__=="__main__":

    user_id = 1   # test user

    while True:

        print("\n1.Add  2.Remove  3.Display  4.Clear  5.Mark Done  6.Exit")
        ch = int(input("Enter choice: "))

        if ch == 1:
            work = input("Enter activity: ")
            add_activity(work, user_id)

        elif ch == 2:
            num = int(input("Enter activity number: "))
            remove_activity(num)

        elif ch == 3:
            rows = display_activity(user_id)
            for r in rows:
                print(r)

        elif ch == 4:
            table_clear(user_id)

        elif ch == 5:
            num = int(input("Enter activity number: "))
            mark_done(num)

        elif ch == 6:
            print("Exited successfully")
            break