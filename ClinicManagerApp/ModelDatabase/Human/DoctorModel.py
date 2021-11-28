from sqlalchemy import Column, String, ForeignKey

from ClinicManagerApp import StaffModel


class DoctorModel(StaffModel):
    __tablename__ = 'doctor_model'

    # primary keys
    staff_code = Column(String(6), ForeignKey('staff_model.staff_code'), primary_key=True)

    # attributes
    major = Column(String(20), default='')
