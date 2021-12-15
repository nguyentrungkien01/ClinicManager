from sqlalchemy import Column, DECIMAL, String, ForeignKey, Integer

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