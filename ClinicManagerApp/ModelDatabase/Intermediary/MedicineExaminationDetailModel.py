from sqlalchemy import Column, ForeignKey, Integer, Text, String

from ClinicManagerApp import db


# class MedicineExaminationDetailModel(db.Model):
#     __tablename__ = 'medicine_examination_detail_model'
#     medicine_id = Column('medicine_id', Integer, ForeignKey('medicine_model.id'), primary_key=True)
#     medical_examination_id = Column('medical_examination_id',
#                                     ForeignKey('medical_examination_model.document_code'), primary_key=True)
#     amount = Column(Integer, default=0)
#     dosage = Column(Text, default='')
#     using_method = Column(Text, default='')

medicine_examination_detail_model = db.Table('medicine_examination_detail_model',
                                             Column('medicine_id', Integer,
                                                    ForeignKey('medicine_model.id'), primary_key=True),
                                             Column('medical_examination_id', String(10),
                                                    ForeignKey('medical_examination_model.document_code'),
                                                    primary_key=True),
                                             Column('amount', Integer, default=0),
                                             Column('dosage', Text, default=''),
                                             Column('using_method', Text, default=''))
