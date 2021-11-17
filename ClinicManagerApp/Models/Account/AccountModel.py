from sqlalchemy import Column, Text, String, Boolean, Integer, DateTime
from sqlalchemy.orm import relationship, backref

from ClinicManagerApp import db


class AccountModel(db.Model):
    __tablename__ = 'account_model'
    username = Column(String(20), primary_key=True)
    password = Column(String(20), nullable=False)
    avatar = Column(Text, default='')
    isActive = Column(Boolean, default=True)
    role = Column(Integer, default=0)
    last_access = Column(DateTime())
    staff = relationship('StaffModel', backref=backref('account', uselist=False, lazy=True), lazy=True)
