from sqlalchemy import String, Column, DECIMAL, Text, Integer, DateTime
from sqlalchemy.orm import relation

from ClinicManagerApp import db


class MedicineModel(db.Model):
    __tablename__ = 'medicine_model'
    code = Column(String(10), primary_key=True)
    name = Column(String(50), default='')
    amount = Column(Integer, default=0)
    unit = Column(String(5), default='')
    unit_price = Column(DECIMAL, default=0.0)
    import_date = Column(DateTime())
    expiration_date = Column(DateTime())
    dosage = Column(String(50), default='')
    manufacturer = Column(String(100), default='')
    description = Column(Text, default='')
    #category = relation('CategoryModel', backref='medicine_list', lazy=True)
