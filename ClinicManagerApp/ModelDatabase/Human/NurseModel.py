from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import backref, relationship

from ClinicManagerApp import db


class NurseModel(db.Model):
    __tablename__ = 'nurse_model'
    staff_code = Column(String(6), ForeignKey('staff_model.code'), primary_key=True)

    medical_bill_list = relationship('MedicalBillModel', backref=backref('nurse', lazy=True), lazy=True)