from app import app
from flask import Flask, render_template, url_for, redirect, request
import pymysql as sql
from forms import SignUpForm
from config import connection

def add_user():
    username = request.form['username']
    userpass = request.form['password']
    try:
        with connection.cursor() as cursor:
            sql = "INSERT INTO user (username, password) VALUES (%s, %s)"
            cursor.execute(sql, (username, userpass))
        connection.commit()
        return render_template("index.html")
    finally:
        connection.close()
