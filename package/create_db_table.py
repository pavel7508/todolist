import sqlite3

#create table
def create_table_tasks():
    con=sqlite3.connect("package/db/todolist.db")
    cur=con.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS tasks(id INTEGER PRIMARY KEY AUTOINCREMENT ,task TEXT,execdate NUMERIC,ok INTEGER,user_id NUMERIC)''')
    con.commit()
    con.close()

# create 2nd table user
def create_table_user():
    con=sqlite3.connect("package/db/todolist.db")
    cur=con.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS user(id INTEGER PRIMARY KEY AUTOINCREMENT ,username TEXT,password TEXT,email TEXT)''')
    con.commit()
    con.close()

#insert record into table
def insert_record(*record_list):
    con=sqlite3.connect("package/db/todolist.db")
    cur=con.cursor()
    cur.execute("INSERT INTO tasks(task,execdate,ok,user_id) VALUES(?,?,?,?)",(record_list))
    con.commit()
    con.close()

def insert_record1(*record_list):
    con=sqlite3.connect("package/db/todolist.db")
    cur=con.cursor()
    cur.execute("INSERT INTO user(username,password,email) VALUES(?,?,?)",(record_list))
    con.commit()
    con.close()

insert_record1("pavzym","pppooo","zyma.p@seznam.cz")