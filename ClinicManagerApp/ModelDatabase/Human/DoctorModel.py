from sqlalchemy import Column, String, Float, Integer, ForeignKey

from ClinicManagerApp import db


class DoctorModel(db.Model):
    __tablename__ = 'doctor_model'
    staff_code = Column(String(6), ForeignKey('staff_model.code'), primary_key=True)
    major = Column(String(20), default='')
    exp_year = Column(Float, default=1.0)
    managed_department_id = Column(Integer, ForeignKey('department_model.id'), nullable=False)
