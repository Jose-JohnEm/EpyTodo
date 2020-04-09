from app import app
from flask import Flask, render_template, url_for
import pymysql as sql

@app.route('/', methods=['GET'])
@app.route('/index', methods=['GET'])
def home():
        return render_template("index.html")

@app.route('/register/', methods=['GET', 'POST'])
def register():
        return render_template("register.html")

@app.route('/signin', methods=['GET', 'POST'])
def signin():
        return render_template("signin.html")
