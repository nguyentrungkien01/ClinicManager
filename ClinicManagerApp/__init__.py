from flask import Flask
from flask_admin import Admin
from flask_sqlalchemy import SQLAlchemy
# from flask_login import LoginManager

app = Flask(__name__)
USERNAME_DB = 'root'
PASSWORD_DB = '12345678'
NAME_DB = 'ClinicManager'
IP_DB = 'localhost'

app.config["SQLALCHEMY_DATABASE_URI"] = \
    str.format(f"mysql+pymysql://{USERNAME_DB}:{PASSWORD_DB}@{IP_DB}/{NAME_DB}?charset=utf8mb4")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
app.config["FLASK_ADMIN_FLUID_LAYOUT"] = True
app.secret_key = '21137afa59a4dd08b708dcf106c724f9'
db = SQLAlchemy(app=app)
admin = Admin(app=app, name="Quản lý phòng mạch tư", template_mode="bootstrap4")
# login = LoginManager(app=app)

from ClinicManagerApp.Model.ModelDatabase.Account.AccountModel import AccountModel
from ClinicManagerApp.Model.ModelDatabase.Category.CategoryModel import CategoryModel
from ClinicManagerApp.Model.ModelDatabase.Department.DepartmentModel import DepartmentModel
from ClinicManagerApp.Model.ModelDatabase.Document.MedicalBillModel import MedicalBillModel
from ClinicManagerApp.Model.ModelDatabase.Document.MedicalExaminationModel import MedicalExaminationModel
from ClinicManagerApp.Model.ModelDatabase.Human.CustomerModel import CustomerModel
from ClinicManagerApp.Model.ModelDatabase.Human.DoctorModel import DoctorModel
from ClinicManagerApp.Model.ModelDatabase.Human.NurseModel import NurseModel
from ClinicManagerApp.Model.ModelDatabase.Medicine.MedicineModel import MedicineModel
from ClinicManagerApp.Model.ModelDatabase.Intermediary.DepartmentManagerDetailModel import \
    department_manager_detail_model
from ClinicManagerApp.Model.ModelDatabase.Intermediary.MedicineExaminationDetailModel import \
    medicine_examination_detail_model

from ClinicManagerApp.Model.ModelView.Account.AccountModelView import AccountModelView
from ClinicManagerApp.Model.ModelView.Category.CategoryModelView import CategoryModelView
from ClinicManagerApp.Model.ModelView.Department.DepartmentModelView import DepartmentModelView
from ClinicManagerApp.Model.ModelView.Document.MedicalBillModelView import MedicalBillModelView
from ClinicManagerApp.Model.ModelView.Document.MedicalExaminationModelView import MedicalExaminationModelView
from ClinicManagerApp.Model.ModelView.Human.CustomerModelView import CustomerModelView
from ClinicManagerApp.Model.ModelView.Human.DoctorModelView import DoctorModelView
from ClinicManagerApp.Model.ModelView.Human.NurseModelView import NurseModelView
from ClinicManagerApp.Model.ModelView.Medicine.MedicineModelView import MedicineModelView
from ClinicManagerApp.Model.ModelView.Analysis.AnalysisModelView import AnalysisModelView


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
    admin.add_view(AnalysisModelView(name='Thống kê báo cáo'))
