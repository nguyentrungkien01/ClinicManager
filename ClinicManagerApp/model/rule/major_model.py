from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from ClinicManagerApp import db


class MajorModel(db.Model):
    __tablename__ = 'major_model'

    # attribute
    major_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(30), nullable=False, unique=True, default='')

    # relationship
    doctor_list = relationship('DoctorModel', backref='major', lazy=True,
                               foreign_keys='[DoctorModel.major_id]')

    def __str__(self):
        return '{}'.format(self.name)
