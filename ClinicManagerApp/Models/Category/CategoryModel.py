from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relation

from ClinicManagerApp import db


class CategoryModel(db.Model):
    __tablename__ = 'category_model'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), unique=True, default='')
    medicine_list = relation('MedicineModel', backref='category', lazy=True)
