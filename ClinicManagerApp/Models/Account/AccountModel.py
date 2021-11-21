from datetime import datetime

from sqlalchemy import Column, Text, String, Boolean, Integer, DateTime
from sqlalchemy.orm import relationship, backref

from ClinicManagerApp import db


class AccountModel(db.Model):
    __tablename__ = 'account_model'
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(20), nullable=False, default='')
    password = Column(String(20), nullable=False, default='')
    avatar = Column(Text, default='')
    is_active = Column(Boolean, default=True)
    role = Column(Integer, default=0)
    last_access = Column(DateTime, default=datetime.now())
    staff = relationship('StaffModel', backref=backref('account', uselist=False, lazy=True), uselist=False, lazy=True)
