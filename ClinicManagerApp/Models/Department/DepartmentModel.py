from sqlalchemy import Column, String, Integer, Text

from ClinicManagerApp import db


class DepartmentModel(db.Model):
    __tablename__ = 'department_model'
    code = Column(String(6), primary_key=True)
    name = Column(String(50), default='')
    capacity = Column(Integer, default=1)
    description = Column(Text, default='')
