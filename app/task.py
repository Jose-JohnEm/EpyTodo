from app import app
from flask import Flask, render_template, url_for, redirect, request
import pymysql as sql
from config import connection

def create_task(user_id, title, begin, end):
    try:
        with connection.cursor() as cursor:
            sql = "INSERT INTO task (title, begin, end) VALUES (%s, %s, %s)"
            cursor.execute(sql, (title, begin, end))
        connection.commit()
        with connection.cursor() as cursor:
            sql = "SELECT MAX(task_id) FROM task"
            cursor.execute(sql)
            connection.commit()
            task_id = cursor.fetchone()
            task_id = task_id[0]
            sql = "INSERT INTO user_has_task (fk_user_id, fk_task_id) VALUES (%s, %s)"
            cursor.execute(sql, (user_id, task_id))
            connection.commit()
    finally:
        cursor.close()

def get_task(user_id):
    try:
        with connection.cursor() as cursor:
            sql = "SELECT * FROM task INNER JOIN user_has_task WHERE user_has_task.fk_user_id = %s and task.task_id = user_has_task.fk_task_id"
            cursor.execute(sql, (user_id))
            result = cursor.fetchall()
            print(result)
            return(result)
    finally:
        cursor.close()
