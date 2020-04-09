from app import app
from flask import Flask, render_template
import pymysql as sql

@app.route('/', methods=['GET'])
@app.route('/index', methods=['GET'])
def route_home():
        return render_template("index.html")