from flask import Flask
from flask_admin import Admin
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
USERNAME_DB = 'root'
PASSWORD_DB = '12345678'
NAME_DB = 'ClinicManager'
IP_DB = 'localhost'

app.config["SQLALCHEMY_DATABASE_URI"] = \
    str.format(f"mysql+pymysql://{USERNAME_DB}:{PASSWORD_DB}@{IP_DB}/{NAME_DB}?charset=utf8mb4")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
app.secret_key= '21137afa59a4dd08b708dcf106c724f9'
db = SQLAlchemy(app)
admin = Admin(app=app, name="Quản lý phòng mạch tư", template_mode="bootstrap4")



