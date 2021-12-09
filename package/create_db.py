import sqlite3
import datetime

print("Připojení do databáze ok")

#create table
def create_table():
    con=sqlite3.connect("db/todolist.db")
    cur=con.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS tasks(id INTEGER PRIMARY KEY AUTOINCREMENT ,task TEXT,execdate NUMERIC,ok INTEGER)''')
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
def get_data(user_id,col="id"):
    con=sqlite3.connect("package/db/todolist.db")
    cur=con.cursor()
    print(user_id)
    if col=="savedate":
        cur.execute("SELECT * FROM tasks WHERE user_id=user_id and ok=0 ORDER BY id")
    elif col=="execdate":
        cur.execute("SELECT * FROM tasks WHERE user_id and ok=0 ORDER BY execdate DESC")
    elif col=="id":
        cur.execute("SELECT * FROM tasks WHERE user_id=user_id")
    elif col =="ok":
        cur.execute("SELECT * FROM tasks WHERE user_id=user_id and ok=1 ORDER BY execdate DESC")
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
    

#insert_record("inventura","2021-11-11",0,now)
#set_data("hhhhhhhhhhh","konec",4)
#del_record(10)
#set_data("ok",1,12)
  

    
