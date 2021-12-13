from flask import Flask,request,url_for,session,render_template,flash,redirect
import os
from package import create_db
from package import admin

app=Flask(__name__)

#get session id
def get_sessid():
    return os.urandom(16)

#set env variable
app.config['SECRET_KEY']="xyz"
app.config['JSON_AS_ASCII'] = False

#index page
@app.route("/")
def home():
    user=session.get("user",None)
    if user:
        return redirect(url_for("todolist"))
    return render_template("index.html",success=False)
    #identify=request.cookies.get('sessid',None)
    #send cookie
    # if identify:
    #    return render_template('index.html',identify=identify,records=records)
    #resp=make_response(render_template("index.html",records=records))
    #resp.set_cookie('sessid',get_sessid(),time.time()+2000)
    #return resp
@app.route("/todolist", methods=["POST","GET"])
def todolist():
    user_id=session["user_id"]
    user=session["user"]
    records=create_db.get_data(user_id,"execdate")
    if request.args.get("submit")=="Savedate":
        records=create_db.get_data(user_id,"savedate")

    elif request.args.get("submit")=="History":
        records=create_db.get_data(user_id,"ok")
    elif request.args.get("submit")=="All":
        records=create_db.get_data(user_id)

    if user:
        print(user)
        return render_template("index.html",user=user,records=records,success=True)
    return render_template("index.html",success=False)
#add task
@app.route("/add")
def add_task():
    user_id=session["user_id"]
    if request.args.get("submit")=="Save":
        task=request.args.get("task")
        execdate=request.args.get("date")
        create_db.insert_record(task,execdate,0,user_id)

        return redirect(url_for("todolist"))
    return render_template("add.html")

#delete task
@app.route("/del")
def delete():
    id=request.args.get("id")
    create_db.del_record(id)
    return redirect(url_for("todolist"))

#edit task
@app.route("/edit")
def edit():
    if request.args.get("submit") == "Save":
        id = request.args.get("id")
        task = request.args.get("task")
        execdate =  request.args.get("date")
        done = request.args.get("done")

        if done !="1":
            done=0

        create_db.update_record(id,task,execdate,done)
        return redirect(url_for("todolist"))
    else:
        id=request.args.get("id")
        record=create_db.get_one_record(id)
        return render_template("edit.html",record=record)

@app.route("/login", methods=["POST","GET"])
def login():

    if request.method =="POST":
        username=request.form["username"]
        password=request.form["password"]
        user_id=admin.login(username,password)

        if user_id:
            session["user_id"]=user_id
            session["user"]=username
            return redirect(url_for("todolist"))
           # return render_template("index.html",userid=user_id,success=True,username=username)
        else:
            flash("Username or password is incorrect")
            return render_template("index.html",success=False)
    return render_template("login.html")

@app.route("/logout")
def logout():
    user=session.get("user",None)
    if user:
        session.pop("user")
        session.pop("user_id")
        return redirect(url_for("home"))
    return render_template("index.html",success=False)
@app.route("/register",methods=["POST","GET"])
def register():
    if request.method =="POST":
        username=request.form["username"]
        password=request.form["password"]
        email=request.form["email"]
        check=admin.new_user(username,password,email)
        if check:
            flash("Registration was successfully")
            return render_template("index.html")
        else :
            flash("Username already exists")
            return render_template("index.html")
    return render_template("registr.html")

if __name__== "__main__":
    app.run()