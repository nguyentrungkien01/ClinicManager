from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import backref, relationship

from ClinicManagerApp import db


class CustomerModel(db.Model):
    __tablename__ = 'customer_model'
    person_id = Column(Integer, ForeignKey('person_model.id'), primary_key=True, nullable=False)

    medical_examination_list = relationship('MedicalExaminationModel',
                                            backref=backref('customer', lazy=True), lazy=True)
    medical_bill_list = relationship('MedicalBillModel',
                                     backref=backref('customer', lazy=True), lazy=True)
