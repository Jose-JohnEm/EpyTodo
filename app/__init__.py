from flask import Flask

app = Flask(__name__)
app.config.from_object('config')

user_id = 0

from app import views
from app import register
from app import signin
