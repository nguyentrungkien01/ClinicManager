from sqlalchemy import Column, Text, String, ForeignKey
from sqlalchemy.orm import backref, relationship

from ClinicManagerApp.ModelDatabase.Document.DocumentModel import DocumentModel


class MedicalExaminationModel(DocumentModel):
    __tablename__ = 'medical_examination_model'

    # primary keys
    document_code = Column(String(10), ForeignKey('document_model.document_code'), primary_key=True)

    # attributes
    symptom = Column(Text, default='')
    predicted_disease = Column(Text, default='')

    # foreign keys
    doctor_code = Column(String(6), ForeignKey('doctor_model.staff_code'))

    # relationships
    medical_bill = relationship('MedicalBillModel',
                                backref=backref('medical_examination', uselist=False, lazy=True),
                                foreign_keys='[MedicalBillModel.medical_examination_code]', lazy=True)
    medicine_list = relationship('MedicineModel', secondary='medicine_examination_detail_model',
                                 backref=backref('medical_examination_list', lazy=True), lazy=True)
