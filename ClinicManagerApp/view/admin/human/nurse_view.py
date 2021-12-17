from flask_admin.contrib.sqla.filters import FilterEqual, FilterNotEqual, FilterLike, FilterNotLike, DateEqualFilter, \
    DateNotEqualFilter, DateGreaterFilter, DateSmallerFilter, DateBetweenFilter, BooleanEqualFilter, \
    BooleanNotEqualFilter, FloatEqualFilter, FloatNotEqualFilter, FloatGreaterFilter, FloatSmallerFilter
from flask_admin.form import rules
from wtforms import validators, DateField, EmailField, TelField

from ClinicManagerApp.model.human.nurse_model import NurseModel
from ClinicManagerApp.view.base_model_view import BaseModelView


class NurseView(BaseModelView):
    # columns
    column_sortable_list = ['staff_id',
                            'first_name',
                            'last_name',
                            'date_of_birth',
                            'date_of_work',
                            'sex',
                            'address',
                            'email',
                            'phone_number',
                            'exp_year']
    column_searchable_list = ['staff_id']
    column_filters = (FilterEqual(NurseModel.first_name, name='Tên'),
                      FilterNotEqual(NurseModel.first_name, name='Tên'),
                      FilterLike(NurseModel.first_name, name='Tên'),
                      FilterNotLike(NurseModel.first_name, name='Tên'),
                      FilterEqual(NurseModel.last_name, name='Họ và tên đệm'),
                      FilterNotEqual(NurseModel.last_name, name='Họ và tên đệm'),
                      FilterLike(NurseModel.last_name, name='Họ và tên đệm'),
                      FilterNotLike(NurseModel.last_name, name='Họ và tên đệm'),
                      DateEqualFilter(NurseModel.date_of_birth, name='Ngày sinh'),
                      DateNotEqualFilter(NurseModel.date_of_birth, name='Ngày sinh'),
                      DateGreaterFilter(NurseModel.date_of_birth, name='Ngày sinh'),
                      DateSmallerFilter(NurseModel.date_of_birth, name='Ngày sinh'),
                      DateBetweenFilter(NurseModel.date_of_birth, name='Ngày sinh'),
                      BooleanEqualFilter(NurseModel.sex, name='Giới tính'),
                      BooleanNotEqualFilter(NurseModel.sex, name='Giới tính'),
                      FilterLike(NurseModel.address, name='Địa chỉ'),
                      FilterNotLike(NurseModel.address, name='Địa chỉ'),
                      FilterLike(NurseModel.email, name='Email'),
                      FilterNotLike(NurseModel.email, name='Email'),
                      FilterEqual(NurseModel.phone_number, name='Số điện thoại'),
                      DateEqualFilter(NurseModel.date_of_work, name='Ngày vào làm'),
                      DateNotEqualFilter(NurseModel.date_of_work, name='Ngày vào làm'),
                      DateGreaterFilter(NurseModel.date_of_work, name='Ngày vào làm'),
                      DateSmallerFilter(NurseModel.date_of_work, name='Ngày vào làm'),
                      DateBetweenFilter(NurseModel.date_of_work, name='Ngày vào làm'),
                      FloatEqualFilter(NurseModel.exp_year, name='Kinh nghiệm (năm)'),
                      FloatNotEqualFilter(NurseModel.exp_year, name='Kinh nghiệm (năm)'),
                      FloatGreaterFilter(NurseModel.exp_year, name='Kinh nghiệm (năm)'),
                      FloatSmallerFilter(NurseModel.exp_year, name='Kinh nghiệm (năm)'))

    column_default_sort = 'staff_id'

    column_labels = dict(staff_id='Mã',
                         first_name='Tên',
                         last_name='Họ và tên đệm',
                         date_of_birth='Ngày sinh',
                         sex='Giới tính',
                         address='Địa chỉ',
                         email='Email',
                         phone_number='Số điện thoại',
                         date_of_work='Ngày vào làm',
                         exp_year='Kinh nghiệm (năm)',
                         manager='Người quản lý',
                         contained_department='Khoa trực thuộc',
                         staff_list='Danh sách nhân viên quản lý',
                         medical_bill_list='Danh sách hóa đơn thanh toán',
                         account='Tài khoản',
                         )
    column_editable_list = ('first_name',
                            'last_name')

    # form
    form_rules = [
        # Define field set with header text and four fields
        rules.FieldSet(('first_name',
                        'last_name',
                        'date_of_birth',
                        'sex',
                        'address',
                        'email',
                        'phone_number',
                        'date_of_work',
                        'exp_year'), 'Thông tin y tá'),

        rules.FieldSet(('manager',
                        'contained_department',
                        'staff_list',
                        'account'), 'Thông tin khác có liên quan'),

    ]
    form_extra_fields = {
        'email': EmailField('Email',
                            validators=[validators.Length(min=0, max=50)],
                            render_kw={
                                'placeholder': 'Địa chỉ email y tá'
                            }),
        'date_of_birth': DateField('Ngày sinh', validators=[validators.DataRequired()], ),
        'date_of_work': DateField('Ngày vào làm', validators=[validators.DataRequired()], ),
        'phone_number': TelField('Số điện thoại', validators=[validators.Length(min=0, max=12)],
                                 render_kw={
                                     'placeholder': 'Số điện thoại y tá'
                                 })
    }
    form_args = dict(
        first_name=dict(validators=[validators.DataRequired(),
                                    validators.Length(min=1, max=20)],
                        render_kw={
                            'placeholder': 'Tên bác y tá'
                        }),
        last_name=dict(validators=[validators.DataRequired(),
                                   validators.Length(min=1, max=50)],
                       render_kw={
                           'placeholder': 'Họ và tên đệm y tá'
                       }),
        address=dict(validators=[validators.DataRequired(),
                                 validators.Length(min=1, max=100)],
                     render_kw={
                         'placeholder': 'Địa chỉ y tá'
                     }),
        exp_year=dict(validators=[validators.NumberRange(min=0.0, max=50.0)],)
    )

    def scaffold_list_columns(self):
        return ['staff_id',
                'first_name',
                'last_name',
                'date_of_birth',
                'sex',
                'address',
                'email',
                'phone_number',
                'date_of_work',
                'exp_year',
                'manager',
                'contained_department',
                'staff_list',
                'medical_bill_list',
                'account'
                ]
