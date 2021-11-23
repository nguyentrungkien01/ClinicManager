from flask_admin.contrib.sqla import ModelView

from ClinicManagerApp import app, db, admin

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

from ClinicManagerApp.ModelView.Account.AccountModelView import AccountModelView
from ClinicManagerApp.ModelView.Category.CategoryModelView import CategoryModelView
from ClinicManagerApp.ModelView.Department.DepartmentModelView import DepartmentModelView
from ClinicManagerApp.ModelView.Document.MedicalBillModelView import MedicalBillModelView
from ClinicManagerApp.ModelView.Document.MedicalExaminationModelView import MedicalExaminationModelView
from ClinicManagerApp.ModelView.Human.CustomerModelView import CustomerModelView
from ClinicManagerApp.ModelView.Human.DoctorModelView import DoctorModelView
from ClinicManagerApp.ModelView.Human.NurseModelView import NurseModelView
from ClinicManagerApp.ModelView.Medicine.MedicineModelView import MedicineModelView


@app.route('/')
def homePage():
    return "Hello"


if __name__ == '__main__':
    db.create_all()
    admin.add_view(AccountModelView(AccountModel, db.session))
    admin.add_view(CustomerModelView(CustomerModel, db.session))
    admin.add_view(DoctorModelView(DoctorModel, db.session))
    admin.add_view(NurseModelView(NurseModel, db.session))
    admin.add_view(DepartmentModelView(DepartmentModel, db.session))
    admin.add_view(CategoryModelView(CategoryModel, db.session))
    admin.add_view(MedicineModelView(MedicineModel, db.session))
    admin.add_view(MedicalBillModelView(MedicalBillModel, db.session))
    admin.add_view(MedicalExaminationModelView(MedicalExaminationModel, db.session))
    app.run(debug=True)
