from flask_admin.contrib.sqla.filters import FloatEqualFilter, FloatNotEqualFilter, FloatGreaterFilter, \
    FloatSmallerFilter, DateEqualFilter, DateNotEqualFilter, DateGreaterFilter, DateSmallerFilter, DateBetweenFilter

from ClinicManagerApp.ModelDatabase.Document.MedicalBillModel import MedicalBillModel
from ClinicManagerApp.ModelView.BaseModelView import BaseModelView


class MedicalBillModelView(BaseModelView):
    can_edit = False
    can_create = False
    can_delete = False

    # columns
    column_sortable_list = ['document_code',
                            'date_created',
                            'medical_price',
                            'medical_examination_price',
                            'total_price']

    column_searchable_list = ['document_code']

    column_filters = (DateEqualFilter(MedicalBillModel.date_created, name='Ngày tạo'),
                      DateNotEqualFilter(MedicalBillModel.date_created, name='Ngày tạo'),
                      DateGreaterFilter(MedicalBillModel.date_created, name='Ngày tạo'),
                      DateSmallerFilter(MedicalBillModel.date_created, name='Ngày tạo'),
                      DateBetweenFilter(MedicalBillModel.date_created, name='Ngày tạo'),
                      FloatEqualFilter(MedicalBillModel.medical_price, name='Tiền thuốc'),
                      FloatNotEqualFilter(MedicalBillModel.medical_price, name='Tiền thuốc'),
                      FloatGreaterFilter(MedicalBillModel.medical_price, name='Tiền thuốc'),
                      FloatSmallerFilter(MedicalBillModel.medical_price, name='Tiền thuốc'),
                      FloatEqualFilter(MedicalBillModel.medical_examination_price, name='Tiền khám bệnh'),
                      FloatNotEqualFilter(MedicalBillModel.medical_examination_price, name='Tiền khám bệnh'),
                      FloatGreaterFilter(MedicalBillModel.medical_examination_price, name='Tiền khám bệnh'),
                      FloatSmallerFilter(MedicalBillModel.medical_examination_price, name='Tiền khám bệnh'),
                      FloatEqualFilter(MedicalBillModel.total_price, name='Tổng tiền'),
                      FloatNotEqualFilter(MedicalBillModel.total_price, name='Tổng tiền'),
                      FloatGreaterFilter(MedicalBillModel.total_price, name='Tổng tiền'),
                      FloatSmallerFilter(MedicalBillModel.total_price, name='Tổng tiền'))

    column_default_sort = 'document_code'

    column_labels = dict(document_code='Mã',
                         date_created='Ngày tạo',
                         medical_price='Tiền thuốc',
                         medical_examination_price='Tiền khám bệnh',
                         total_price='Tổng tiền',
                         medical_examination='Phiếu khám bệnh',
                         customer='Khách hàng',
                         nurse='Y tá phụ trách'
                         )

    def scaffold_list_columns(self):
        return ['document_code',
                'date_created',
                'medical_examination',
                'customer',
                'nurse',
                'medical_examination_price',
                'medical_price',
                'total_price']
