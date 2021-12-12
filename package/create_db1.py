import mysql.connector

print("Připojení do databáze ok")

#create table
def create_table():
    con=mysql.connector.connect(host="pavzym.mysql.pythonanywhere-services.com",user="pavzym",passwd="",database="pavzym$todolist")
    cur=con.cursor()
    cur.execute('''CREATE TABLE tasks(id INT(20) PRIMARY KEY AUTOINCREMENT ,task VARCHAR(100),execdate DATE,ok INT(2),user_id INT(5))''')
    con.commit()
    con.close() 
    
#insert record into table    
def insert_record(*record_list):
    con=mysql.connector.connect(host="pavzym.mysql.pythonanywhere-services.com",user="pavzym",passwd="",database="pavzym$todolist")
    cur=con.cursor()
    cur.execute("INSERT INTO tasks(task,execdate,ok,user_id) VALUES(?,?,?,?)",(record_list))
    con.commit()
    con.close()
    
#load data from database
def get_data(user,col="id"):
    con=mysql.connector.connect(host="pavzym.mysql.pythonanywhere-services.com",user="pavzym",passwd="",database="pavzym$todolist")
    cur=con.cursor()
    print(user)
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
    con=mysql.connector.connect(host="pavzym.mysql.pythonanywhere-services.com",user="pavzym",passwd="",database="pavzym$todolist")
    cur=con.cursor()
    sql="SELECT * FROM tasks WHERE id=?"
    cur.execute(sql,(a,))
    record=cur.fetchone()
    con.close()
    return record
    
#update_database
def set_data(column,value,expression):
    con=mysql.connector.connect(host="pavzym.mysql.pythonanywhere-services.com",user="pavzym",passwd="",database="pavzym$todolist")
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
    con=mysql.connector.connect(host="pavzym.mysql.pythonanywhere-services.com",user="pavzym",passwd="",database="pavzym$todolist")
    cur=con.cursor()
    sql="UPDATE tasks SET task=?,execdate=?,ok=?  WHERE id=?"
    cur.execute(sql,(task,execdate,ok,idd))
    con.commit()
    con.close()
#delete record
def del_record(expression):
    con=mysql.connector.connect(host="pavzym.mysql.pythonanywhere-services.com",user="pavzym",passwd="",database="pavzym$todolist")
    cur=con.cursor()
    sql="DELETE FROM tasks WHERE id=?"
    cur.execute(sql,(expression,))
    con.commit()
    con.close() 
    

#insert_record("inventura","2021-11-11",0,now)
#set_data("hhhhhhhhhhh","konec",4)
#del_record(10)
#set_data("ok",1,12)
  