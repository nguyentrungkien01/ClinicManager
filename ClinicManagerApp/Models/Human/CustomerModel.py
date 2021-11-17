from sqlalchemy import Column, String

from ClinicManagerApp.Models.Human.PersonModel import PersonModel


class CustomerModel(PersonModel):
    __tablename__ = 'customer_model'
    code = Column(String(6), primary_key=True)