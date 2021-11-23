from sqlalchemy import Column, String, Integer, Text
from sqlalchemy.orm import backref, relationship
from ClinicManagerApp import db


class DepartmentModel(db.Model):
    __tablename__ = 'department_model'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), unique=True, default='')
    capacity = Column(Integer, default=1)
    description = Column(Text, default='')
    staff_list = relationship('StaffModel', backref='contained_department', lazy=True)
    manager = relationship('DoctorModel', backref=backref('managed_department', uselist=False, lazy=True), lazy=True)
