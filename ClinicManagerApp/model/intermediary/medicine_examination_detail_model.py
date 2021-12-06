from sqlalchemy import Column, ForeignKey, Integer, Text, String

from ClinicManagerApp import db


medicine_examination_detail_model = db.Table('medicine_examination_detail_model',
                                             Column('medicine_id', Integer,
                                                    ForeignKey('medicine_model.medicine_id'),
                                                    primary_key=True),
                                             Column('medical_examination_code', String(10),
                                                    ForeignKey('medical_examination_model.document_code'),
                                                    primary_key=True),
                                             Column('amount', Integer, default=0),
                                             Column('dosage', Text, default=''),
                                             Column('using_method', Text, default=''))
