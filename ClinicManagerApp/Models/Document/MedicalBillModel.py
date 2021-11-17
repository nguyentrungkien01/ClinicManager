from sqlalchemy import Column, DECIMAL

from ClinicManagerApp.Models.Document.DocumentModel import DocumentModel


class MedicalBillModel(DocumentModel):
    __tablename_ = 'medical_bill_model'
    medicalPrice = Column(DECIMAL, default=0.0)
    medicalExaminationPrice = Column(DECIMAL, default=0.0)
    totalPrice = Column(DECIMAL, default=0.0)
