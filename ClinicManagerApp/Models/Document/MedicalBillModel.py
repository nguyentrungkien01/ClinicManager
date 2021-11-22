from sqlalchemy import Column, DECIMAL, String, ForeignKey, Integer

from ClinicManagerApp.Models.Document.DocumentModel import DocumentModel


class MedicalBillModel(DocumentModel):
    __tablename_ = 'medical_bill_model'
    medical_price = Column(DECIMAL, default=0.0)
    medical_examination_price = Column(DECIMAL, default=0.0)
    total_price = Column(DECIMAL, default=0.0)
    nurse_code = Column(String(6), ForeignKey('nurse_model.code'), nullable=False)
    customer_id = Column(Integer, ForeignKey('customer_model.id'), nullable=False)
    medical_examination_code = Column(String(10), ForeignKey('medical_examination_model.code'), nullable=False)
