from app import app
from flask import jsonify
import pymysql as sql

@app.route('/', methods=['GET'])
@app.route('/index', methods=['GET'])
def route_home():
        return "Hello World\n"