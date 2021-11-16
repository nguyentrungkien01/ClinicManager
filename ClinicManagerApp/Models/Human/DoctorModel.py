from sqlalchemy import Column, String, Float
from ClinicManagerApp.Models.Human.StaffModel import StaffModel


class DoctorModel(StaffModel):
    __tablename__ = 'doctor_model'
    major = Column(String(20), defaul='')
    exp_year = Column(Float, default=1)
