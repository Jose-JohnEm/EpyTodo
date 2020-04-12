from app import app
from flask import Flask, render_template, url_for, redirect, request
import pymysql as sql
from config import connection
from signin import check_user

def add_user(username, userpass):
    base = user_in_base(username)
    if base == False:
        try:
            with connection.cursor() as cursor:
                sql = "INSERT INTO user (username, password) VALUES (%s, %s)"
                cursor.execute(sql, (username, userpass))
            connection.commit()
            return (check_user(username, userpass)[0])
        finally:
            cursor.close()
    else:
        return (0)

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
