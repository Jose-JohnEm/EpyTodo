from app import app
from flask import Flask, render_template
import pymysql as sql

@app.route('/', methods=['GET'])
@app.route('/index', methods=['GET'])
def home():
        return render_template("index.html")
@app.route('/register/', methods=['GET'])
def register():
        return render_template("register.html")
@app.route('/signin', methods=['GET'])
def signin():
        return render_template("register.html")