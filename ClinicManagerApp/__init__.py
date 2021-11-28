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
app.secret_key = '21137afa59a4dd08b708dcf106c724f9'
db = SQLAlchemy(app)
admin = Admin(app=app, name="Quản lý phòng mạch tư", template_mode="bootstrap4")

from ClinicManagerApp.ModelDatabase.Account.AccountModel import AccountModel
from ClinicManagerApp.ModelDatabase.Category.CategoryModel import CategoryModel
from ClinicManagerApp.ModelDatabase.Department.DepartmentModel import DepartmentModel
from ClinicManagerApp.ModelDatabase.Document.DocumentModel import DocumentModel
from ClinicManagerApp.ModelDatabase.Document.MedicalBillModel import MedicalBillModel
from ClinicManagerApp.ModelDatabase.Document.MedicalExaminationModel import MedicalExaminationModel
from ClinicManagerApp.ModelDatabase.Human.PersonModel import PersonModel
from ClinicManagerApp.ModelDatabase.Human.StaffModel import StaffModel
from ClinicManagerApp.ModelDatabase.Human.CustomerModel import CustomerModel
from ClinicManagerApp.ModelDatabase.Human.DoctorModel import DoctorModel
from ClinicManagerApp.ModelDatabase.Human.NurseModel import NurseModel
from ClinicManagerApp.ModelDatabase.Medicine.MedicineModel import MedicineModel
from ClinicManagerApp.ModelDatabase.Intermediary.MedicineExaminationDetailModel import \
    medicine_examination_detail_model
from ClinicManagerApp.ModelDatabase.Intermediary.DepartmentManagerDetailModel import department_manager_detail_model

from ClinicManagerApp.ModelView.Account.AccountModelView import AccountModelView
from ClinicManagerApp.ModelView.Category.CategoryModelView import CategoryModelView
from ClinicManagerApp.ModelView.Department.DepartmentModelView import DepartmentModelView
from ClinicManagerApp.ModelView.Document.MedicalBillModelView import MedicalBillModelView
from ClinicManagerApp.ModelView.Document.MedicalExaminationModelView import MedicalExaminationModelView
from ClinicManagerApp.ModelView.Human.CustomerModelView import CustomerModelView
from ClinicManagerApp.ModelView.Human.DoctorModelView import DoctorModelView
from ClinicManagerApp.ModelView.Human.NurseModelView import NurseModelView
from ClinicManagerApp.ModelView.Medicine.MedicineModelView import MedicineModelView


def initTables():
    try:
        db.create_all()
    except:
        db.session.rollback()


def initAdmin():
    admin.add_view(AccountModelView(AccountModel, db.session, name='Tài khoản'))
    admin.add_view(DoctorModelView(DoctorModel, db.session, category='Nhân viên', name='Bác sĩ'))
    admin.add_view(NurseModelView(NurseModel, db.session, category='Nhân viên', name='Y tá'))
    admin.add_view(CustomerModelView(CustomerModel, db.session, name='Khách hàng'))
    admin.add_view(DepartmentModelView(DepartmentModel, db.session, name='Khoa khám'))
    admin.add_view(MedicineModelView(MedicineModel, db.session, name='Thuốc', category='Sản phẩm'))
    admin.add_view(CategoryModelView(CategoryModel, db.session, name='Kho thuốc', category='Sản phẩm'))
    admin.add_view(MedicalBillModelView(MedicalBillModel, db.session, category='Tài liệu', name='Hóa đơn'))
    admin.add_view(MedicalExaminationModelView(MedicalExaminationModel, db.session,
                                               category='Tài liệu', name='Phiếu khám'))
