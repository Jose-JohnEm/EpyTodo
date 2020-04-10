from app import app
from flask import Flask, render_template, url_for, redirect, request
import pymysql as sql
from config import connection
from .register import add_user
from .signin import check_user
from .task import create_task
from .task import get_task

user_id = 0

@app.route('/', methods=['GET'])
@app.route('/index', methods=['GET'])
def home():
        return render_template("index.html")

@app.route('/register/', methods=['GET', 'POST'])
def register():
        if request.method == 'POST':
            user_id = add_user((request.form['username']), request.form['password'])
            return redirect('/task')
        return render_template("register.html")

@app.route('/signin/', methods=['GET', 'POST'])
def signin():
        if request.method == 'POST':
            user_id = check_user(request.form['username'], request.form['password'])
            if user_id != None:
                redirect('/task')
        return render_template("signin.html")

@app.route('/contact', methods=['GET', 'POST'])
def contact():
        return render_template("contact.html")

@app.route('/task/', methods=['GET', 'POST'])
def todo():
    print("USER ID ==>", user_id)
    if request.method == 'POST':
        create_task(user_id, request.form['title'], request.form['begin'], request.form['end'])
    return render_template("todo.html", usertasks=get_task(user_id), lenght=len(get_task(user_id)))

@app.route('/user', methods=['GET', 'POST'])
def user():
        return render_template("user.html")
