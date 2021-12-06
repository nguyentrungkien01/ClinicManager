from datetime import datetime

from sqlalchemy import Column, String, DateTime, Integer, ForeignKey

from ClinicManagerApp import db


class DocumentModel(db.Model):
    __tablename__ = 'document_model'

    # primary keys
    document_code = Column(String(10), primary_key=True)

    # attributes
    date_created = Column(DateTime, default=datetime.now())

    # foreign key
    customer_id = Column(Integer, ForeignKey('customer_model.customer_id'))

    def __str__(self):
        return '{}'.format(self.document_code)