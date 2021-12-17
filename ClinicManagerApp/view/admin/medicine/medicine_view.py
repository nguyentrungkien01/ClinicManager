from flask_admin.contrib.sqla.filters import FilterLike, FilterNotLike, IntEqualFilter, IntNotEqualFilter, \
    IntGreaterFilter, IntSmallerFilter, FilterEqual, FilterNotEqual, FloatEqualFilter, FloatNotEqualFilter, \
    FloatGreaterFilter, FloatSmallerFilter, DateEqualFilter, DateNotEqualFilter, DateGreaterFilter, DateSmallerFilter, \
    DateBetweenFilter
from flask_admin.form import rules
from wtforms import validators

from ClinicManagerApp.model.medicine.medicine_model import MedicineModel
from ClinicManagerApp.model.rule.medicine_unit_model import MedicineUnitModel
from ClinicManagerApp.view.base_model_view import BaseModelView


class MedicineView(BaseModelView):
    # columns
    column_sortable_list = ['medicine_id',
                            'name',
                            'amount',
                            'unit_price',
                            'import_date',
                            'expiration_date',
                            'manufacturer']
    column_searchable_list = ['medicine_id',
                              'manufacturer',
                              'description']
    column_filters = (FilterLike(MedicineUnitModel.name, name='Đơn vị thuốc'),
                      FilterNotLike(MedicineUnitModel.name, name='Đơn vị thuốc'),
                      FilterLike(MedicineModel.name, name='Tên'),
                      FilterNotLike(MedicineModel.name, name='Tên'),
                      IntEqualFilter(MedicineModel.amount, name='Số lượng'),
                      IntNotEqualFilter(MedicineModel.amount, name='Số lượng'),
                      IntGreaterFilter(MedicineModel.amount, name='Số lượng'),
                      IntSmallerFilter(MedicineModel.amount, name='Số lượng'),
                      FloatEqualFilter(MedicineModel.unit_price, name='Đơn giá'),
                      FloatNotEqualFilter(MedicineModel.unit_price, name='Đơn giá'),
                      FloatGreaterFilter(MedicineModel.unit_price, name='Đơn giá'),
                      FloatSmallerFilter(MedicineModel.unit_price, name='Đơn giá'),
                      DateEqualFilter(MedicineModel.import_date, name='Ngày nhập hàng'),
                      DateNotEqualFilter(MedicineModel.import_date, name='Ngày nhập hàng'),
                      DateGreaterFilter(MedicineModel.import_date, name='Ngày nhập hàng'),
                      DateSmallerFilter(MedicineModel.import_date, name='Ngày nhập hàng'),
                      DateBetweenFilter(MedicineModel.import_date, name='Ngày nhập hàng'),
                      DateEqualFilter(MedicineModel.expiration_date, name='Ngày hết hạn'),
                      DateNotEqualFilter(MedicineModel.expiration_date, name='Ngày hết hạn'),
                      DateGreaterFilter(MedicineModel.expiration_date, name='Ngày hết hạn'),
                      DateSmallerFilter(MedicineModel.expiration_date, name='Ngày hết hạn'),
                      DateBetweenFilter(MedicineModel.expiration_date, name='Ngày hết hạn'),
                      FilterEqual(MedicineModel.manufacturer, name='Nhà sản xuất'),
                      FilterNotEqual(MedicineModel.manufacturer, name='Nhà sản xuất'),
                      FilterLike(MedicineModel.manufacturer, name='Nhà sản xuất'),
                      FilterNotLike(MedicineModel.manufacturer, name='Nhà sản xuất'),
                      )

    column_default_sort = 'medicine_id'

    column_labels = dict(medicine_id='Mã',
                         name='Tên thuốc',
                         amount='Số lượng thuốc',
                         medicine_unit='Đơn vị thuốc',
                         unit_price='Đơn giá',
                         import_date='Ngày nhập hàng',
                         expiration_date='Ngày hết hạn',
                         dosage='Liều lượng',
                         manufacturer='Nhà sản xuất',
                         category='Kho thuốc',
                         medical_examination_list='Danh sách phiếu khám bệnh',
                         description='Mô tả'
                         )
    column_editable_list = ('name',
                            'amount',
                            'unit_price')

    # form
    form_rules = [
        rules.FieldSet(('name',
                        'amount',
                        'medicine_unit',
                        'unit_price',
                        'import_date',
                        'expiration_date',
                        'dosage',
                        'manufacturer',
                        'description'), 'Thông tin thuốc'),

        rules.FieldSet(('category',), 'Thông tin khác có liên quan'),

    ]
    form_args = dict(
        name=dict(validators=[validators.DataRequired(), validators.Length(min=1, max=50)],
                  render_kw={
                      'placeholder': 'Tên thuốc'
                  }),
        amount=dict(validators=[validators.DataRequired(), validators.NumberRange(0, 1000)], ),
        medicine_unit=dict(validators=[validators.DataRequired()], ),
        unit_price=dict(validators=[validators.DataRequired(), validators.NumberRange(0, 100000000)], ),
        dosage=dict(validators=[validators.DataRequired(), validators.Length(min=0, max=100)],
                    render_kw={
                        'placeholder': 'Liều dùng thuốc'
                    }),
        manufacturer=dict(validators=[validators.DataRequired(), validators.Length(min=0, max=100)],
                          render_kw={
                              'placeholder': 'Nhà sản xuất thuốc'
                          }),
        description=dict(render_kw={
            'placeholder': 'Mô tả thuốc'
        }, )

    )

    def scaffold_list_columns(self):
        return ['medicine_id',
                'name',
                'amount',
                'medicine_unit',
                'unit_price',
                'import_date',
                'expiration_date',
                'dosage',
                'manufacturer',
                'category',
                'medical_examination_list',
                'description']
