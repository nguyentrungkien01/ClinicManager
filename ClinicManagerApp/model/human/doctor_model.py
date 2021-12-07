from sqlalchemy import Column, String, ForeignKey, Integer

from ClinicManagerApp.model.human.staff_model import StaffModel


class DoctorModel(StaffModel):
    __tablename__ = 'doctor_model'

    # primary keys
    staff_id = Column(Integer, ForeignKey('staff_model.staff_id'), primary_key=True)

    # attributes
    major = Column(String(20), default='')

    # mapper
    __mapper_args__ = {
        'polymorphic_identity': 'doctor'
    }