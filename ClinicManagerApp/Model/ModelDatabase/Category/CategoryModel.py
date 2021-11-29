from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from ClinicManagerApp import db


class CategoryModel(db.Model):
    __tablename__ = 'category_model'

    # primary keys
    category_id = Column(Integer, primary_key=True, autoincrement=True)

    # attributes
    name = Column(String(50), unique=True, default='')

    # relationships
    medicine_list = relationship('MedicineModel', backref='category',
                                 foreign_keys='[MedicineModel.category_id]', lazy=True)

    def __str__(self):
        return '{}'.format(self.name)