from flask import Flask
from flask_admin import Admin
from flask_sqlalchemy import SQLAlchemy

from flask_login import LoginManager

from ClinicManagerApp.view.home_view import HomeView

app = Flask(__name__)
USERNAME_DB = 'root'
PASSWORD_DB = '12345678'
NAME_DB = 'ClinicManager'
IP_DB = 'localhost'

app.config["SQLALCHEMY_DATABASE_URI"] = \
    str.format(f"mysql+pymysql://{USERNAME_DB}:{PASSWORD_DB}@{IP_DB}/{NAME_DB}?charset=utf8mb4")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
app.config["FLASK_ADMIN_FLUID_LAYOUT"] = True
#app.config["SQLALCHEMY_ECHO"] = True
app.secret_key = b'21137afa59a4dd08b708dcf106c724f9'
db = SQLAlchemy(app=app)
admin = Admin(app=app, name="Quản lý phòng mạch tư", template_mode="bootstrap4",
              index_view=HomeView(name='Trang chủ'))
login = LoginManager(app=app)

from ClinicManagerApp.model.account.account_model import AccountModel
from ClinicManagerApp.model.category.category_model import CategoryModel
from ClinicManagerApp.model.department.department_model import DepartmentModel
from ClinicManagerApp.model.document.medical_bill_model import MedicalBillModel
from ClinicManagerApp.model.document.medical_examination_model import MedicalExaminationModel
from ClinicManagerApp.model.human.customer_model import CustomerModel
from ClinicManagerApp.model.human.doctor_model import DoctorModel
from ClinicManagerApp.model.human.nurse_model import NurseModel
from ClinicManagerApp.model.medicine.medicine_model import MedicineModel
from ClinicManagerApp.model.intermediary.department_manager_detail_model import department_manager_detail_model
from ClinicManagerApp.model.intermediary.medicine_examination_detail_model import medicine_examination_detail_model
from ClinicManagerApp.model.rule.medicine_unit_model import MedicineUnitModel
from ClinicManagerApp.model.rule.role_model import RoleModel
from ClinicManagerApp.model.rule.rule_model import RuleModel

from ClinicManagerApp.view.admin.account.account_view import AccountView
from ClinicManagerApp.view.admin.category.category_view import CategoryView
from ClinicManagerApp.view.admin.department.department_view import DepartmentView
from ClinicManagerApp.view.admin.document.medical_bill_view import MedicalBillView
from ClinicManagerApp.view.admin.document.medical_examination_view import MedicalExaminationView
from ClinicManagerApp.view.admin.human.customer_view import CustomerView
from ClinicManagerApp.view.admin.human.doctor_view import DoctorView
from ClinicManagerApp.view.admin.human.nurse_view import NurseView
from ClinicManagerApp.view.log_out_view import LogoutView
from ClinicManagerApp.view.admin.medicine.medicine_view import MedicineView
from ClinicManagerApp.view.admin.statistic.statistic_view import StatisticView
from ClinicManagerApp.view.admin.report.report_view import ReportView
from ClinicManagerApp.view.admin.rule.rule_view import RuleView
from ClinicManagerApp.view.doctor.medical_examination_creation_view import MedicalExaminationCreationView
from ClinicManagerApp.view.nurse.ofline_registration_view import OfflineRegistrationView
from ClinicManagerApp.view.nurse.payment_view import PaymentView
from ClinicManagerApp.view.change_password_view import ChangePasswordView


def initTables():
    try:
        db.create_all()
    except:
        db.session.rollback()


def initAdmin():
    admin.add_view(AccountView(AccountModel, db.session, name='Tài khoản'))
    admin.add_view(DoctorView(DoctorModel, db.session, category='Nhân viên', name='Bác sĩ'))
    admin.add_view(NurseView(NurseModel, db.session, category='Nhân viên', name='Y tá'))
    admin.add_view(CustomerView(CustomerModel, db.session, name='Khách hàng'))
    admin.add_view(DepartmentView(DepartmentModel, db.session, name='Khoa khám'))
    admin.add_view(MedicineView(MedicineModel, db.session, name='Thuốc'))
    admin.add_view(CategoryView(CategoryModel, db.session, name='Kho thuốc'))
    admin.add_view(MedicalBillView(MedicalBillModel, db.session, category='Tài liệu', name='Hóa đơn'))
    admin.add_view(MedicalExaminationView(MedicalExaminationModel, db.session,
                                          category='Tài liệu', name='Phiếu khám'))
    admin.add_view(StatisticView(name='Thống kê', category='Dữ liệu'))
    admin.add_view(ReportView(name='Báo cáo', category='Dữ liệu'))
    admin.add_view(RuleView(name='Quy định phòng khám'))
    admin.add_view(MedicalExaminationCreationView(name='Tạo phiếu khám'))
    admin.add_view(OfflineRegistrationView(name='Đăng ký trực tiếp'))
    admin.add_view(PaymentView(name='Thanh toán'))
    admin.add_view(ChangePasswordView(name = 'Đổi mật khẩu'))
    admin.add_view(LogoutView(name='Đăng xuất'))
