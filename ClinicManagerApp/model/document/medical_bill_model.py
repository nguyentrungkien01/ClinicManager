
from sqlalchemy import Column, DECIMAL, ForeignKey, Integer

from ClinicManagerApp.model.document.document_model import DocumentModel


class MedicalBillModel(DocumentModel):
    __tablename__ = 'medical_bill_model'

    # primary keys
    document_id = Column(Integer, ForeignKey('document_model.document_id'), primary_key=True)

    # attribute
    medical_price = Column(DECIMAL, default=0.0)
    medical_examination_price = Column(DECIMAL, default=0.0)
    total_price = Column(DECIMAL, default=0.0)

    # foreign key
    nurse_id = Column(Integer, ForeignKey('nurse_model.staff_id'))
    medical_examination_id = Column(Integer, ForeignKey('medical_examination_model.document_id'))

    # mapper
    __mapper_args__ = {
        'polymorphic_identity': 'medical_bill'
    }

    def __init__(self, **kwargs):
        self.medical_examination_price = kwargs.get('medical_examination_price')
        self.medical_examination_id = kwargs.get('medical_examination_id')
        self.customer_id = kwargs.get('customer_id')
        self.medical_price = kwargs.get('medical_price')
        self.nurse_id = kwargs.get('nurse_id')
        self.total_price = kwargs.get('total_price')
