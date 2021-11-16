from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
USERNAME_DB = 'root'
PASSWORD_DB = '12345678'
NAME_DB = 'ClinicManager'
IP_DB = 'localhost'

app.config["SQLALCHEMY_DATABASE_URI"] = \
    str.format(f"mysql+pymysql://{USERNAME_DB}:{PASSWORD_DB}@{IP_DB}/{NAME_DB}?charset=utf8mb4")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True

db = SQLAlchemy(app)
