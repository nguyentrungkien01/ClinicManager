from sqlalchemy import Column, Integer
from sqlalchemy.orm import backref, relationship

from ClinicManagerApp import PersonModel, db


class CustomerModel(PersonModel, db.Model):
    __tablename__ = 'customer_model'

    # attribute
    customer_id = Column(Integer, primary_key=True, autoincrement=True)

    def __str__(self):
        return '{} {} {}'.format(self.last_name, self.middle_name, self.first_name)

    # relationship
    document_list = relationship('DocumentModel', backref=backref('customer', lazy=True),
                                 foreign_keys='[DocumentModel.customer_id]', lazy=True)

