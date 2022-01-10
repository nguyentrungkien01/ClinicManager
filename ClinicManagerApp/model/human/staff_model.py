from datetime import datetime

from sqlalchemy import String, Column, DateTime, ForeignKey, Integer, Float, Text
from sqlalchemy.orm import relationship, backref

from ClinicManagerApp import db
from ClinicManagerApp.model.human.person_model import PersonModel


class StaffModel(PersonModel, db.Model):
    __tablename__ = 'staff_model'

    # primary keys
    staff_id = Column(Integer, primary_key=True, autoincrement=True)

    # attributes
    date_of_work = Column(DateTime, default=datetime.now())
    exp_year = Column(Float, default=0.0)
    type = Column(String(50))
    avatar = Column(Text, default='')
    facebook_link = Column(Text, default='')
    twitter_link = Column(Text, default='')

    # foreign keys
    contained_department_id = Column('contained_department_id', Integer,
                                     ForeignKey('department_model.department_id'))
    manager_id = Column('manager_id', Integer, ForeignKey('staff_model.staff_id'))

    # relationships
    account = relationship('AccountModel', backref=backref('staff', uselist=False, lazy=True),
                           foreign_keys='[AccountModel.staff_id]', uselist=False, lazy=True)
    staff_list = relationship('StaffModel', backref=backref('manager', remote_side=[staff_id], lazy=True),
                              foreign_keys='[StaffModel.manager_id]', lazy=True)

    # mapper
    __mapper_args__ = {
        'polymorphic_on': type
    }

    def __str__(self):
        return '{} {}'.format(self.last_name, self.first_name)

    def set_avatar(self, url):
        self.avatar = url
