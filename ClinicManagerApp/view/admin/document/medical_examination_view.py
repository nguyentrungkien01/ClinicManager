from flask_admin.contrib.sqla.filters import DateEqualFilter, DateSmallerFilter, DateGreaterFilter, \
    DateBetweenFilter, DateNotEqualFilter

from ClinicManagerApp.model.document.medical_examination_model import MedicalExaminationModel
from ClinicManagerApp.view.base_model_view import BaseModelView


class MedicalExaminationView(BaseModelView):
    can_create = False
    can_delete = False
    can_edit = False

    # columns
    column_sortable_list = ['document_id',
                            'date_created',
                            'date_created']
    column_searchable_list = ['document_id',
                              'symptom',
                              'predicted_disease']
    column_filters = (DateEqualFilter(MedicalExaminationModel.date_created, name='Ngày tạo'),
                      DateNotEqualFilter(MedicalExaminationModel.date_created, name='Ngày tạo'),
                      DateGreaterFilter(MedicalExaminationModel.date_created, name='Ngày tạo'),
                      DateSmallerFilter(MedicalExaminationModel.date_created, name='Ngày tạo'),
                      DateBetweenFilter(MedicalExaminationModel.date_created, name='Ngày tạo')
                      )
    column_default_sort = 'document_id'
    column_labels = dict(document_id='Mã',
                         date_created='Ngày tạo',
                         symptom='Triệu chứng',
                         predicted_disease='Bệnh chẩn đoán',
                         customer='Khách hàng',
                         medicine_list='Danh sách thuốc',
                         medical_bill='Hoá đơn thanh toán')

    def scaffold_list_columns(self):
        return ['document_id',
                'date_created',
                'symptom',
                'predicted_disease',
                'medicine_list',
                'customer',
                'medical_bill']
