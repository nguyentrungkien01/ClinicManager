from _datetime import datetime

from sqlalchemy import String, Column, DECIMAL, Text, Integer, DateTime, ForeignKey
from sqlalchemy.orm import declared_attr

from ClinicManagerApp import db


class MedicineModel(db.Model):
    __tablename__ = 'medicine_model'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), unique=True, default='', nullable=False)
    amount = Column(Integer, default=0)
    unit = Column(String(5), default='')
    unit_price = Column(DECIMAL, default=0.0)
    import_date = Column(DateTime, default=datetime.now())
    expiration_date = Column(DateTime, default=datetime.now())
    dosage = Column(String(50), default='')
    manufacturer = Column(String(100), default='')
    description = Column(Text, default='')

    @declared_attr
    def modify_fk(self):
        return Column('category_id', Integer, ForeignKey('category_model.id'))

