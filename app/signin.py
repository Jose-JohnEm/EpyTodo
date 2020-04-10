from app import app
from flask import Flask, render_template, url_for, redirect, request
import pymysql as sql
from config import connection

def check_user(username, userpass):
    try:
        with connection.cursor() as cursor:
            sql = "SELECT user_id FROM user WHERE username =%s and password =%s"
            cursor.execute(sql, (username, userpass))
            result = cursor.fetchall()
            print("{0}".format(result[0]))
    finally:
            cursor.close()
