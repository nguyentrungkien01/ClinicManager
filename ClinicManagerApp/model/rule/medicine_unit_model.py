from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from ClinicManagerApp import db


class MedicineUnitModel(db.Model):
    __tablename__ = 'medicine_unit_model'

    # primary key
    medicine_unit_id = Column(Integer, primary_key=True, autoincrement=True)


    # attribute
    name = Column(String(30), nullable=False, unique=True, default='')

    # relationship
    medicine_list = relationship('MedicineModel', backref='medicine_unit', lazy=True,
                                 foreign_keys='[MedicineModel.medicine_unit_id]')

    def __str__(self):
        return '{}'.format(self.name)
