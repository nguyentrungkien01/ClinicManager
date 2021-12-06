from sqlalchemy import Column, Integer
from sqlalchemy.orm import backref, relationship

from ClinicManagerApp import db
from ClinicManagerApp.model.human.person_model import PersonModel


class CustomerModel(PersonModel, db.Model):
    __tablename__ = 'customer_model'

    # attribute
    customer_id = Column(Integer, primary_key=True, autoincrement=True)

    def __str__(self):
        return '{} {} {}'.format(self.last_name, self.middle_name, self.first_name)

    # relationship
    document_list = relationship('DocumentModel', backref=backref('customer', lazy=True),
                                 foreign_keys='[DocumentModel.customer_id]', lazy=True)

