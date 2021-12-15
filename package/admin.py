import sqlite3
from flask import Flask,request,url_for,session,render_template,make_response,flash,redirect
from werkzeug.security import generate_password_hash, check_password_hash
from os import path

ROOT = path.dirname(path.realpath(__file__))

print(ROOT)

def login(username,password):
    con=sqlite3.connect("package/db/todolist.db")
    cur=con.cursor()
    sql="SELECT *  FROM user where username=?"
    cur.execute(sql,(username,))
    record=cur.fetchone()
    if not record:
        return False
    else:
        password_hash=record[2]
        print(password_hash)
        password=check_password_hash(password_hash,password)
        print(password)
        user_id=record[0]
        con.close()
        if password :
            return user_id
        else:
            return False

def new_user(username,password,email=0):
    #con = sqlite3.connect(path.join(ROOT, "todolist.db"))
    con=sqlite3.connect("package/db/todolist.db")
    print(con)
    cur=con.cursor()
    user_checked=check_user(username)

    if user_checked:
        return False
    else :
        password=generate_password_hash(password)
        cur.execute("INSERT INTO user(username,password,email) VALUES (?,?,?)",(username,password,email))
        con.commit()
        con.close()
        return True

def check_user(username):
    con=sqlite3.connect("package/db/todolist.db")
    cur=con.cursor()
    sql="SELECT username from user where username=?"
    cur.execute(sql,(username,))
    record=cur.fetchone()
    con.close()
    if record:
        return True
    else:
        return False

