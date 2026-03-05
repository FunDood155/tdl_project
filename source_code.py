import mysql.connector 

con=mysql.connector.connect(host="localhost",user="root",passwd="root155",database="tdldb")
cursor=con.cursor()

cursor.execute("use tdldb;")

#table creation
a="create table if not exists tdl_table (num int auto_increment primary key , work varchar(99), date timestamp default current_timestamp,status varchar(99));"
cursor.execute(a)


#add_activity
a="insert into tdl_table (work,status) values (%s,%s);"
cursor.execute(a,("gym","no"))
con.commit()

#display_activity
a="select * from tdl_table;"
cursor.execute(a)
z=cursor.fetchall()
print(z)



#saving changes...
con.commit()
cursor.close()


def add_activity():
    pass
def remove_activity():
    pass
def display_activity():
    pass
def table_clear():
    #clear table
    cursor.execute("drop table tdl_table")