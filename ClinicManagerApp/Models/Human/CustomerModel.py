from sqlalchemy import Column, Integer
from sqlalchemy.orm import relation, backref

from ClinicManagerApp.Models.Human.PersonModel import PersonModel


class CustomerModel(PersonModel):
    __tablename__ = 'customer_model'
    code = Column(Integer, primary_key=True, autoincrement=True)
    medical_examination_list = relation('MedicalExaminationModel', backref=backref('customer', lazy=True), lazy=True)
    medical_bill_list = relation('MedicalBillModel', backref=backref('customer', lazy=True), lazy=True)
