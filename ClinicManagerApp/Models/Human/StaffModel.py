from datetime import  datetime

from sqlalchemy import String, Column, DateTime, ForeignKey, Integer, Boolean
from sqlalchemy.orm import declared_attr

from ClinicManagerApp.Models.Human.PersonModel import PersonModel


class StaffModel(PersonModel):
    __tablename__ = 'staff_model'
    __abstract__ = True
    code = Column(String(6), primary_key=True)
    date_of_work = Column(DateTime, default=datetime.now())
    is_admin = Column(Boolean, default=True)

    @declared_attr
    def modify_fk_1(self):
        return Column('account_id', Integer, ForeignKey('account_model.id'), nullable=False)

    @declared_attr
    def modify_fk_2(self):
        return Column('contained_department_id', Integer, ForeignKey('department_model.id'), nullable=False)

    @declared_attr
    def modify_fk_3(self):
        return Column('manager_code', String(6), ForeignKey('doctor_model.code'))
