from sqlalchemy.orm import relation, backref

from ClinicManagerApp.Models.Human.StaffModel import StaffModel


class NurseModel(StaffModel):
    __tablename__ = 'nurse_model'
    medical_bill_list = relation('MedicalBillModel', backref=backref('nurse', lazy=True), lazy=True)
