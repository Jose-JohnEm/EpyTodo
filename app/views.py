from app import app
from flask import Flask, render_template, url_for, redirect, request
import pymysql as sql
from forms import SignUpForm
from config import connection
from register import add_user
from signin import check_user

@app.route('/', methods=['GET'])
@app.route('/index', methods=['GET'])
def home():
        return render_template("index.html")

@app.route('/register/', methods=['GET', 'POST'])
def register():
        form = SignUpForm()
        if form.is_submitted():
            add_user()
        return render_template("register.html", form=form)

@app.route('/signin', methods=['GET', 'POST'])
def signin():
        form = SignUpForm()
        if form.is_submitted():
                check_user()
        return render_template("signin.html", form=form)
