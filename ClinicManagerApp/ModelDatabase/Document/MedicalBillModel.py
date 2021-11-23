from sqlalchemy import Column, DECIMAL, String, ForeignKey, Integer

from ClinicManagerApp import db


class MedicalBillModel(db.Model):
    __tablename_ = 'medical_bill_model'
    document_code = Column(String(10), ForeignKey('document_model.code'),
                           primary_key=True, nullable=False)
    medical_price = Column(DECIMAL, default=0.0)
    medical_examination_price = Column(DECIMAL, default=0.0)
    total_price = Column(DECIMAL, default=0.0)

    nurse_code = Column(String(6), ForeignKey('nurse_model.staff_code'), nullable=False)
    customer_id = Column(Integer, ForeignKey('customer_model.person_id'), nullable=False)
    medical_examination_code = Column(String(10),
                                      ForeignKey('medical_examination_model.document_code'),
                                      nullable=False)
