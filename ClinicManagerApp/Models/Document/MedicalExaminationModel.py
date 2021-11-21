from sqlalchemy import Column, Text, String, ForeignKey, Integer
from sqlalchemy.orm import relation, backref

from ClinicManagerApp.Models.Document.DocumentModel import DocumentModel


class MedicalExaminationModel(DocumentModel):
    __tablename_ = 'medical_examination_model'
    symptom = Column(Text, default='')
    predicted_disease = Column(Text, default='')
    doctor_code = Column(String(6), ForeignKey('doctor_model.code'), nullable=False)
    customer_id = Column(Integer, ForeignKey('customer_model.id'), nullable=False)
    medical_bill = relation('MedicalBillModel', backref=backref('medical_examination', uselist=False, lazy=True),
                            uselist=False, lazy=True)
