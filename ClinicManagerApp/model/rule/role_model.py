from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from ClinicManagerApp import db


class RoleModel(db.Model):
    __tablename__ = 'role_model'

    # primary key
    role_id = Column(Integer, primary_key=True, autoincrement=True)

    # attribute
    name = Column(String(30), nullable=False, unique=True, default='')

    # relationship
    account_list = relationship('AccountModel', backref='role', lazy=True,
                                foreign_keys='[AccountModel.role_id]')

    def __str__(self):
        return '{}'.format(self.name)
