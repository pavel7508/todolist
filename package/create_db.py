import sqlite3
import datetime

print("Připojení do databáze ok")

#create table task
def create_table_task():
    con=sqlite3.connect("db/todolist.db")
    cur=con.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS tasks(id INTEGER PRIMARY KEY AUTOINCREMENT ,task TEXT,execdate NUMERIC,ok INTEGER)''')
    con.commit()
    con.close() 
#create table note
def create_table_note():
    con=sqlite3.connect("db/todolist.db")
    cur=con.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS note(id INTEGER PRIMARY KEY AUTOINCREMENT,email TEXT,note TEXT)''')
    con.commit()
    con.close()

#insert record into table    
def insert_record(*record_list):
    con=sqlite3.connect("package/db/todolist.db")
    cur=con.cursor()
    cur.execute("INSERT INTO tasks(task,execdate,ok,user_id) VALUES(?,?,?,?)",(record_list))
    con.commit()
    con.close()
    
#load data from database
def get_data(user,col="id"):
    con=sqlite3.connect("package/db/todolist.db")
    cur=con.cursor()
    if col=="savedate":
        sql="SELECT * FROM tasks WHERE user_id=? and ok=0 ORDER BY id"
        cur.execute(sql,(user,))
    elif col=="execdate":
        sql="SELECT * FROM tasks WHERE user_id=? and ok=0 ORDER BY execdate DESC"
        cur.execute(sql,(user,))
    elif col=="id":
        sql="SELECT * FROM tasks WHERE user_id=?"
        cur.execute(sql,(user,))
    elif col =="ok":
        sql="SELECT * FROM tasks WHERE user_id=? and ok=1 ORDER BY execdate DESC"
        cur.execute(sql,(user,))
    records=cur.fetchall()
    con.close()
    return records
def get_one_record(a):
    con=sqlite3.connect("package/db/todolist.db")
    cur=con.cursor()
    sql="SELECT * FROM tasks WHERE id=?"
    cur.execute(sql,(a,))
    record=cur.fetchone()
    con.close()
    return record
    
#update_database
def set_data(column,value,expression):
    con=sqlite3.connect("package/db/todolist.db")
    cur=con.cursor()
    if column=="task":
        sql="UPDATE tasks SET task=? where id=?"
        cur.execute(sql,(value,expression))
    elif column=="execdate":
        sql="UPDATE tasks SET task=? where id=?"
        cur.execute(sql,(value,expression))
    elif column=="ok":
        if value==1 or value==0:
            sql="UPDATE tasks SET ok=? where id=?"
            cur.execute(sql,(value,expression))
        else:
            print("Neplatný údaj")
    con.commit()
    con.close()
def update_record(idd,task,execdate,ok):
    con=sqlite3.connect("package/db/todolist.db")
    cur=con.cursor()
    sql="UPDATE tasks SET task=?,execdate=?,ok=?  WHERE id=?"
    cur.execute(sql,(task,execdate,ok,idd))
    con.commit()
    con.close()
#delete record
def del_record(expression):
    con=sqlite3.connect("package/db/todolist.db")
    cur=con.cursor()
    sql="DELETE FROM tasks WHERE id=?"
    cur.execute(sql,(expression,))
    con.commit()
    con.close() 
    
#insert comment into the table
def insert_note(email,note):
    con=sqlite3.connect("package/db/todolist.db")
    cur=con.cursor()
    cur.execute("INSERT INTO note(email,note) VALUES(?,?)",(email,note))
    con.commit()
    con.close()

#select five last comment
def comments():
    con=sqlite3.connect("package/db/todolist.db")
    cur=con.cursor()
    cur.execute("SELECT * FROM note order by id desc LIMIT 3")
    note_record=cur.fetchall()
    con.close()
    return note_record
