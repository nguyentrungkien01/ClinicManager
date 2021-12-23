from sqlalchemy import Column, Text, ForeignKey, Integer
from sqlalchemy.orm import backref, relationship

from ClinicManagerApp.model.document.document_model import DocumentModel


class MedicalExaminationModel(DocumentModel):
    __tablename__ = 'medical_examination_model'

    # primary keys
    document_id = Column(Integer, ForeignKey('document_model.document_id'), primary_key=True)

    # attributes
    symptom = Column(Text, default='')
    predicted_disease = Column(Text, default='')

    # foreign keys
    doctor_id = Column(Integer, ForeignKey('doctor_model.staff_id'))

    # relationships
    medical_bill = relationship('MedicalBillModel',
                                backref=backref('medical_examination', uselist=False, lazy=True),
                                foreign_keys='[MedicalBillModel.medical_examination_id]', uselist=False, lazy=True)
    medicine_list = relationship('MedicineModel', secondary='medicine_examination_detail_model',
                                 backref=backref('medical_examination_list', lazy=True), lazy=True)

    # mapper
    __mapper_args__ = {
        'polymorphic_identity': 'medical_examination'
    }