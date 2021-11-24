from sqlalchemy import Column, DECIMAL, String, ForeignKey

from ClinicManagerApp.ModelDatabase.Document.DocumentModel import DocumentModel


class MedicalBillModel(DocumentModel):
    __tablename__ = 'medical_bill_model'

    # primary keys
    document_code = Column(String(10), ForeignKey('document_model.document_code'), primary_key=True)

    # attribute
    medical_price = Column(DECIMAL, default=0.0)
    medical_examination_price = Column(DECIMAL, default=0.0)
    total_price = Column(DECIMAL, default=0.0)

    # foreign key
    nurse_code = Column(String(6), ForeignKey('nurse_model.staff_code'))
    medical_examination_code = Column(String(10), ForeignKey('medical_examination_model.document_code'))
    # mapper
    __mapper_args__ = {
        'polymorphic_identity': 'medical_bill',
    }
