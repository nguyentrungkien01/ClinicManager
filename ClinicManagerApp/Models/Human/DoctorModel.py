from sqlalchemy import Column, String, Float, Integer, ForeignKey
from sqlalchemy.orm import backref, relation

from ClinicManagerApp.Models.Human.StaffModel import StaffModel


class DoctorModel(StaffModel):
    __tablename__ = 'doctor_model'
    major = Column(String(20), default='')
    exp_year = Column(Float, default=1.0)
    managed_department_id = Column(Integer, ForeignKey('department_model.id'), nullable=False)
    staff_list = relation('StaffModel', backref=backref('manager', lazy=True), lazy=True)
