import enum
from datetime import datetime

from sqlalchemy import Column, String, DateTime, Enum


class Sex(enum.Enum):
    MALE = 0,
    FEMALE = 1


class PersonModel(object):

    # attributes
    first_name = Column(String(20), default='')
    last_name = Column(String(50), default='')
    date_of_birth = Column(DateTime, default=datetime.now())
    address = Column(String(100), default='')
    email = Column(String(50), default='')
    phone_number = Column(String(12), default='')
    sex = Column(Enum(Sex), default=Sex.MALE)
