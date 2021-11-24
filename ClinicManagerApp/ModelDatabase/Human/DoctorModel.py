from sqlalchemy import Column, String, Float, Integer, ForeignKey

from ClinicManagerApp import StaffModel


class DoctorModel(StaffModel):
    __tablename__ = 'doctor_model'

    # primary keys
    staff_code = Column(String(6), ForeignKey('staff_model.staff_code'), primary_key=True)

    # attributes
    major = Column(String(20), default='')
    exp_year = Column(Float, default=1.0)

    # foreign keys
    managed_department_id = Column(Integer, ForeignKey('department_model.department_id'))

    # mapper
    __mapper_args__ = {
        'polymorphic_identity': 'doctor',
    }