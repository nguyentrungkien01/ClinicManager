from datetime import datetime

from sqlalchemy import Column, String, DateTime
from ClinicManagerApp import db


class DocumentModel(db.Model):
    __tablename__ = 'document_model'
    code = Column(String(10), primary_key=True)
    name = Column(String(50), default='')
    date_created = Column(DateTime, default=datetime.now())
