from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.orm import backref, relationship

from ClinicManagerApp.model.human.staff_model import StaffModel


class NurseModel(StaffModel):
    __tablename__ = 'nurse_model'

    # primary key
    staff_id = Column(Integer, ForeignKey('staff_model.staff_id'), primary_key=True)

    # relationship
    medical_bill_list = relationship('MedicalBillModel', backref=backref('nurse', lazy=True),
                                     foreign_keys='[MedicalBillModel.nurse_id]', lazy=True)

    # mapper
    __mapper_args__ = {
        'polymorphic_identity': 'nurse'
    }
