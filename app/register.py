from app import app
from flask import Flask, render_template, url_for, redirect, request
import pymysql as sql
from forms import SignUpForm
from config import connection
from string import lower

def add_user():
    username = lower(request.form['username'])
    userpass = request.form['password']
    base = user_in_base(username)
    if base == False:
        try:
            with connection.cursor() as cursor:
                sql = "INSERT INTO user (username, password) VALUES (%s, %s)"
                cursor.execute(sql, (username, userpass))
            connection.commit()
            return render_template("index.html")
        finally:
            cursor.close()
    else:
        return render_template("index.html")

def user_in_base(username):
    try:
        with connection.cursor() as cursor:
            sql = "SELECT COUNT(username) FROM user WHERE username =%s"
            cursor.execute(sql, username)
            result = cursor.fetchone()
            if result[0] == 0:
                return False
            else:
                return True
    finally:
            cursor.close()
