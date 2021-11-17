from sqlalchemy import Column, String

from ClinicManagerApp import db


class CategoryModel(db.Model):
    __tablename__ = 'category_model'
    code = Column(String(6), primary_key=True)
    name = Column(String(50), default='')
