
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import runpy

app = Flask(__name__)
USERNAME_DB = 'root'
PASSWORD_DB = '12345678'
NAME_DB = 'ClinicManager'
IP_DB = 'localhost'

app.config["SQLALCHEMY_DATABASE_URI"] = \
    str.format(f"mysql+pymysql://{USERNAME_DB}:{PASSWORD_DB}@{IP_DB}/{NAME_DB}?charset=utf8mb4")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True

db = SQLAlchemy(app)


runpy.run_path(path_name='./Models/Account/AccountModel.py')
runpy.run_path(path_name='./Models/Category/CategoryModel.py')
runpy.run_path(path_name='./Models/Department/DepartmentModel.py')
runpy.run_path(path_name='./Models/Document/DocumentModel.py')
runpy.run_path(path_name='./Models/Document/MedicalBillModel.py')
runpy.run_path(path_name='./Models/Document/MedicalExaminationModel.py')
runpy.run_path(path_name='./Models/Human/PersonModel.py')
runpy.run_path(path_name='./Models/Human/StaffModel.py')
runpy.run_path(path_name='./Models/Human/CustomerModel.py')
runpy.run_path(path_name='./Models/Human/DoctorModel.py')
runpy.run_path(path_name='./Models/Human/NurseModel.py')
runpy.run_path(path_name='./Models/Medicine/MedicineModel.py')
runpy.run_path(path_name='./Models/Intermediary/MedicineExaminationDetailModel.py')
