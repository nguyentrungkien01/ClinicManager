from sqlalchemy import Column, String, Text

from ClinicManagerApp.Models.Document.DocumentModel import DocumentModel


class MedicalExaminationModel(DocumentModel):
    __tablename_ = 'medical_examination_model'
    symptom = Column(Text, default='')
    predicted_disease = Column(Text, default='')

