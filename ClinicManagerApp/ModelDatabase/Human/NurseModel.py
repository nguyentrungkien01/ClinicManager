from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import backref, relationship

from ClinicManagerApp import StaffModel


class NurseModel(StaffModel):
    __tablename__ = 'nurse_model'

    # primary key
    staff_code = Column(String(6), ForeignKey('staff_model.staff_code'), primary_key=True)

    # relationship
    medical_bill_list = relationship('MedicalBillModel', backref=backref('nurse', lazy=True),
                                     foreign_keys='[MedicalBillModel.nurse_code]', lazy=True)

    # mapper
    __mapper_args__ = {
        'polymorphic_identity': 'nurse',
    }
