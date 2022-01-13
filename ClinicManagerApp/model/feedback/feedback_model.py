import datetime

from sqlalchemy import Column, Integer, String, Text, DateTime, Boolean

from ClinicManagerApp import db


class FeedbackModel(db.Model):
    __tablename__ = 'feedback_model'

    # primary key
    feedback_id = Column(Integer, primary_key=True, autoincrement=True)

    # attribute
    subject = Column(String(200), default='')
    customer_name = Column(String(200), default='')
    content = Column(Text, default='')
    gmail = Column(String(100), default='')
    date_created = Column(DateTime, default=datetime.datetime.now())
    status = Column(Boolean, default=False)

    def __str__(self):
        return '{}'.format(self.subject)

    def __init__(self, **kwargs):
        self.customer_name = kwargs.get('customer_name')
        self.content = kwargs.get('content')
        self.subject = kwargs.get('subject')
        self.gmail = kwargs.get('gmail')