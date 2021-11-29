from datetime import datetime

from sqlalchemy import String, Column, DateTime, ForeignKey, Integer, Float
from sqlalchemy.orm import relationship, backref

from ClinicManagerApp import db
from ClinicManagerApp.Model.ModelDatabase.Human.PersonModel import PersonModel


class StaffModel(PersonModel, db.Model):
    __tablename__ = 'staff_model'

    # primary keys
    staff_code = Column(String(6), primary_key=True)

    # attributes
    date_of_work = Column(DateTime, default=datetime.now())
    exp_year = Column(Float, default=0.0)

    # foreign keys
    contained_department_id = Column('contained_department_id', Integer,
                                     ForeignKey('department_model.department_id'))
    manager_code = Column('manager_code', String(6), ForeignKey('staff_model.staff_code'))

    # relationships
    account = relationship('AccountModel', backref=backref('staff', uselist=False, lazy=True),
                           foreign_keys='[AccountModel.staff_code]', lazy=True)
    staff_list = relationship('StaffModel', backref=backref('manager', lazy=True),
                              foreign_keys='[StaffModel.manager_code]',
                              remote_side='[StaffModel.staff_code]', lazy=True)

    def __str__(self):
        return '{} {} {}'.format(self.last_name, self.middle_name, self.first_name)

