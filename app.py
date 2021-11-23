from flask import Flask,request,url_for,session,render_template,make_response,flash,redirect
import os,time
from package import create_db
import datetime
app=Flask(__name__)

#get session id 
def get_sessid():
    return os.urandom(16)

#set env variable
app.config['SECRET_KEY']=os.urandom(16)
app.config['JSON_AS_ASCII'] = False

#index page
@app.route("/")
def home():   
    identify=request.cookies.get('sessid',None)
    records=create_db.get_data("execdate")
    if request.args.get("submit")=="Savedate":
        records=create_db.get_data("savedate")
    elif request.args.get("submit")=="History":
        records=create_db.get_data("ok")
    elif request.args.get("submit")=="All":
        records=create_db.get_data()
    #send cookie
    if identify:        
        return render_template('index.html',identify=identify,records=records)
    resp=make_response(render_template("index.html",records=records))
    resp.set_cookie('sessid',get_sessid(),time.time()+2000)
    return resp
    
        
#add task   
@app.route("/add")
def add_task():
    if request.args.get("submit")=="Save":
        task=request.args.get("task")
        execdate=request.args.get("date")
        create_db.insert_record(task,execdate,0)
    
        return redirect(url_for("home"))
    return render_template("add.html")

#delete task
@app.route("/del")
def delete():
    id=request.args.get("id")
    create_db.del_record(id)
    return redirect(url_for("home"))

#edit task
@app.route("/edit")
def edit():
    if request.args.get("submit") == "Save":
        id = request.args.get("id")
        task = request.args.get("task")
        execdate =  request.args.get("date")
        done = request.args.get("done")
        print(done)
        if done !="1":
            done=0
        print(done)
        create_db.update_record(id,task,execdate,done)
        return redirect(url_for("home"))
    else:
        id=request.args.get("id")
        record=create_db.get_one_record(id)
        return render_template("edit.html",record=record)
@app.route("/login")
def login():
   return render_template("login.html") 


app.run(debug=True,port=3000)