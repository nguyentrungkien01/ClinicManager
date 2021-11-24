from datetime import datetime

from sqlalchemy import Column, String, DateTime, Integer, ForeignKey

from ClinicManagerApp import db


class DocumentModel(db.Model):
    __tablename__ = 'document_model'

    # primary keys
    document_code = Column(String(10), primary_key=True)

    # attributes
    name = Column(String(50), default='')
    date_created = Column(DateTime, default=datetime.now())
    document_type = Column(String(20))

    # foreign key
    customer_id = Column(Integer, ForeignKey('customer_model.customer_id'))

    # mapper
    __mapper_args__ = {
        'polymorphic_on': document_type
    }
