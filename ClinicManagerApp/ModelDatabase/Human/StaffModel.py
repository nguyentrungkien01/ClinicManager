from datetime import datetime

from sqlalchemy import String, Column, DateTime, ForeignKey, Integer, Boolean
from sqlalchemy.orm import relationship, backref

from ClinicManagerApp import db


class StaffModel(db.Model):
    __tablename__ = 'staff_model'
    code = Column(String(6), primary_key=True)
    date_of_work = Column(DateTime, default=datetime.now())
    is_admin = Column(Boolean, default=True)
    person_id = Column(Integer, ForeignKey('person_model.id'), nullable=False)

    account = relationship('AccountModel',
                           backref=backref('staff', uselist=False, lazy=True),
                           lazy=True)
    contained_department_id = Column(Integer, ForeignKey('department_model.id'), nullable=False)
    manager_code = Column(String(6), ForeignKey('staff_model.code'), nullable=False)
    staff_list = relationship('StaffModel', backref=backref('manager', lazy=True), remote_side=[code], lazy=True)
