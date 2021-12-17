from datetime import datetime

from sqlalchemy import Column, String, DateTime, Integer, ForeignKey

from ClinicManagerApp import db


class DocumentModel(db.Model):
    __tablename__ = 'document_model'

    # primary keys
    document_id = Column(Integer, primary_key=True, autoincrement=True)

    # attributes
    date_created = Column(DateTime, default=datetime.now())
    type = Column(String(100))

    # foreign key
    customer_id = Column(Integer, ForeignKey('customer_model.customer_id'))

    # mapper
    __mapper_args__ = {
        'polymorphic_on': type
    }

    def __str__(self):
        return '{}'.format(self.document_id)
