from sqlalchemy import Column, String, Integer, Text
from sqlalchemy.orm import backref, relation

from ClinicManagerApp import db


class DepartmentModel(db.Model):
    __tablename__ = 'department_model'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), unique=True, default='')
    capacity = Column(Integer, default=1)
    description = Column(Text, default='')
    staff_list = relation('StaffModel', backref='contained_department', lazy=True)
    manager = relation('DoctorModel', backref=backref('managed_department', uselist=False, lazy=True),
                       uselist=False, lazy=True)
