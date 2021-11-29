from datetime import datetime

from sqlalchemy import Column, Text, String, Boolean, Integer, DateTime, ForeignKey, Enum
from ClinicManagerApp import db
from ClinicManagerApp.Model.ModelDatabase.Utils import UserRole
from flask_login import UserMixin


class AccountModel(db.Model, UserMixin):
    __tablename__ = 'account_model'

    # primary keys
    account_id = Column(Integer, primary_key=True, autoincrement=True)

    # attributes
    username = Column(String(20), unique=True, nullable=False, default='')
    password = Column(String(40), nullable=False, default='')
    avatar = Column(Text, default='')
    is_active = Column(Boolean, default=True)
    last_access = Column(DateTime, default=datetime.now())
    role = Column(Enum(UserRole), default=UserRole.DOCTOR)

    # foreign keys
    staff_code = Column(String(6), ForeignKey('staff_model.staff_code'))

    def __str__(self):
        return '{}'.format(self.username)
