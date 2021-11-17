from sqlalchemy import Column, String, Date, DateTime

from ClinicManagerApp import db


class DocumentModel(db.Model):
    __tablename_ = 'document_model'
    __abstract__ = True 
    code = Column(String(10), primary_key=True)
    name = Column(String(50), default='')
    date_created = Column(DateTime())


