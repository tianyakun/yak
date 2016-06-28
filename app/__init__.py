# encoding: utf-8
# __author__ = 'kkk'

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from pymongo import MongoClient

app = Flask(__name__)           # The WSGI compliant web application object
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
db = SQLAlchemy(app)            # Setup Flask-SQLAlchemy
client = MongoClient('mongodb://localhost:27017/')
mongo = client['yak']

from create_app import *
from views import *
from users import *
from models import *
