from sqlalchemy import Column, Integer
from sqlalchemy.orm import backref, relationship

from ClinicManagerApp import db
from ClinicManagerApp.model.human.person_model import PersonModel


class CustomerModel(PersonModel, db.Model):
    __tablename__ = 'customer_model'

    # attribute
    customer_id = Column(Integer, primary_key=True, autoincrement=True)

    def __str__(self):
        return '{} {}'.format(self.last_name, self.first_name)

    def __init__(self, **kwargs):
        self.id_card = kwargs.get('id_card')
        self.first_name = kwargs.get('first_name')
        self.last_name = kwargs.get('last_name')
        self.sex = kwargs.get('sex')
        self.address = kwargs.get('address')
        self.phone_number = kwargs.get('phone_number')
        self.email = kwargs.get('email')

    # relationship
    document_list = relationship('DocumentModel', backref=backref('customer', uselist=False, lazy=True),
                                 foreign_keys='[DocumentModel.customer_id]', lazy=True)
