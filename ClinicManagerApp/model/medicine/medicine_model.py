from _datetime import datetime

from sqlalchemy import String, Column, DECIMAL, Text, Integer, DateTime, ForeignKey, Enum

from ClinicManagerApp import db


class MedicineModel(db.Model):
    __tablename__ = 'medicine_model'

    # primary keys
    medicine_id = Column(Integer, primary_key=True, autoincrement=True)

    # attributes
    name = Column(String(50), unique=True, default='', nullable=False)
    amount = Column(Integer, default=0)
    unit_price = Column(DECIMAL, default=0.0)
    import_date = Column(DateTime, default=datetime.now())
    expiration_date = Column(DateTime, default=datetime.now())
    dosage = Column(String(100), default='')
    manufacturer = Column(String(100), default='')
    description = Column(Text, default='')

    # foreign keys
    category_id = Column(Integer, ForeignKey('category_model.category_id'))
    medicine_unit_id = Column(Integer, ForeignKey('medicine_unit_model.medicine_unit_id'))

    def __str__(self):
        return '{}'.format(self.name)
