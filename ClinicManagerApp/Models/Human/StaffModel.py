from sqlalchemy import String, Column, DateTime, ForeignKey
from sqlalchemy.orm import declared_attr

from ClinicManagerApp.Models.Human.PersonModel import PersonModel


class StaffModel(PersonModel):
    __tablename__ = 'staff_model'
    __abstract__ = True
    code = Column(String(6), primary_key=True)
    date_of_work = Column(DateTime())

    @declared_attr
    def modified_fk(self):
        return Column('account', String(20), ForeignKey('account_model.username'))
