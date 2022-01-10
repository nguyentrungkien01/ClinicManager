from sqlalchemy import Column, ForeignKey, Integer

from ClinicManagerApp.model.human.staff_model import StaffModel


class DoctorModel(StaffModel):
    __tablename__ = 'doctor_model'

    # primary keys
    staff_id = Column(Integer, ForeignKey('staff_model.staff_id'), primary_key=True)

    # foreign key
    major_id = Column(Integer, ForeignKey('major_model.major_id'))

    # mapper
    __mapper_args__ = {
        'polymorphic_identity': 'doctor'
    }