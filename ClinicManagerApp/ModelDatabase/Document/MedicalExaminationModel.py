from sqlalchemy import Column, Text, String, ForeignKey, Integer
from sqlalchemy.orm import backref, relationship

from ClinicManagerApp import db
from ClinicManagerApp.ModelDatabase.Document.DocumentModel import DocumentModel


class MedicalExaminationModel(DocumentModel, db.Model):
    __tablename__ = 'medical_examination_model'
    document_code = Column(String(10), ForeignKey('document_model.code'),
                           primary_key=True, nullable=False)
    symptom = Column(Text, default='')
    predicted_disease = Column(Text, default='')

    doctor_code = Column(String(6), ForeignKey('doctor_model.staff_code'), nullable=False)
    customer_id = Column(Integer, ForeignKey('customer_model.person_id'), nullable=False)
    medical_bill = relationship('MedicalBillModel',
                                backref=backref('medical_examination', uselist=False, lazy=True),
                                lazy=True)
    medicine_list = relationship('MedicineModel', secondary='medicine_examination_detail_model',
                                 backref=backref('medical_examination_list', lazy=True), lazy=True)
