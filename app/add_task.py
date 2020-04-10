from app import app
from flask import Flask, render_template, url_for, redirect, request
import pymysql as sql
from config import connection

def add_task(task, begin ,end):
    try:
        print(task + begin + end)
        with connection.cursor() as cursor:
            cursor.execute(sql, (task, begin, end))
        connection.commit()
        return
    finally:
        cursor.close()