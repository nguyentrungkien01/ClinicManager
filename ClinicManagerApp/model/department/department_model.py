from sqlalchemy import Column, String, Integer, Text
from sqlalchemy.orm import backref, relationship
from ClinicManagerApp import db


class DepartmentModel(db.Model):
    __tablename__ = 'department_model'

    # primary keys
    department_id = Column(Integer, primary_key=True, autoincrement=True)

    # attributes
    name = Column(String(50), unique=True, default='')
    capacity = Column(Integer, default=1)
    description = Column(Text, default='')

    # relationships
    staff_list = relationship('StaffModel', backref=backref('contained_department', uselist=False),
                              foreign_keys='[StaffModel.contained_department_id]', lazy=True)
    manager = relationship('DoctorModel', secondary='department_manager_detail_model',uselist=False,
                           backref=backref('managed_department', lazy=True), lazy=True)

    def __str__(self):
        return '{}'.format(self.name)
