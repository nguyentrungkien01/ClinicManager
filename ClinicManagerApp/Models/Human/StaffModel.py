from sqlalchemy import String, Column, Date
from ClinicManagerApp.Models.Human.PersonModel import PersonModel


class StaffModel(PersonModel):
    __tablename__ = 'staff_model'
    code = Column(String(6), primary_key=True)
    date_of_work = Column(Date)
g