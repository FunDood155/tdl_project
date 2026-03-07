import mysql.connector 

con=mysql.connector.connect(host="localhost",user="root",passwd="root155",database="tdldb")
cursor=con.cursor()

cursor.execute("use tdldb;")

#table creation
a="create table if not exists tdl_table (num int auto_increment primary key , work varchar(99), date timestamp default current_timestamp,status varchar(99));"
cursor.execute(a)

def add_activity():
    #add_activity
    a="insert into tdl_table (work,status) values (%s,%s);"
    t=input("Enter activity to add : ")
    cursor.execute(a,(t,"no"))
    con.commit()

def remove_activity():
    #remove an activity
    a="delete from tdl_table where num= (%s);"
    t=int(input("Enter activity to remove(num) : "))
    cursor.execute(a,(t,))
    con.commit()

def display_activity():
    #display_activity
    a="select * from tdl_table;"
    cursor.execute(a)
    z=cursor.fetchall()
    for i in z:
        print(i)
    
def table_clear():
    #clear table
    cursor.execute("truncate table tdl_table")

    ###     MAIN    ###

ch=1
print("1.Add, 2.Remove, 3.Display, 4.Clear")
while(ch in [1,2,3,4]):
    ch=int(input("Enter ur choice : "))
    match ch:
        case 1:
            add_activity()
        case 2:
            remove_activity()
        case 3:
            display_activity()
        case 4:
            table_clear()
        case _:
            print("Successfully EXITED...")
            break
    print("\n* * *  over  * * *\n")
#saving changes...
con.commit()
cursor.close()


