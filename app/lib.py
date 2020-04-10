from app import app
from flask import Flask, render_template, url_for, redirect, request
import pymysql as sql
from forms import SignUpForm
from config import connection
from register import add_user
from signin import check_user
from string import lower