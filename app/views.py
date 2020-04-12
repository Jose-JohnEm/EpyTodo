from app import app
from flask import Flask, render_template, url_for, redirect, request
import pymysql as sql
from config import connection
from .register import add_user
from .signin import check_user
from .task import create_task
from .task import get_task
from app import user_id

@app.route('/', methods=['GET'])
@app.route('/index/', methods=['GET'])
def home():
        return render_template("index.html", user_id=user_id)

@app.route('/register/', methods=['GET', 'POST'])
def register():
    global user_id
    if request.method == 'POST':
        user_id = add_user((request.form['username']), request.form['password'])
        if user_id != 0:
            return redirect('/user/task/')
    return render_template("register.html", user_id=user_id)

@app.route('/signin/', methods=['GET', 'POST'])
def signin():
    global user_id
    if request.method == 'POST':
        user_id = check_user(request.form['username'], request.form['password'])
        if user_id != 0:
            return redirect('/user/task/')
    return render_template("signin.html", user_id=user_id)

@app.route('/contact/', methods=['GET', 'POST'])
def contact():
        return render_template("contact.html", user_id=user_id)

@app.route('/user/task/', methods=['GET', 'POST'])
def todo():
    if request.method == 'POST':
        create_task(user_id, request.form['title'], request.form['begin'], request.form['end'], int(request.form['status']))
    return render_template("todo.html", usertasks=get_task(user_id), lenght=len(get_task(user_id)), user_id=user_id)

@app.route('/user/', methods=['GET', 'POST'])
def user():
        return render_template("user.html", user_id=user_id)
