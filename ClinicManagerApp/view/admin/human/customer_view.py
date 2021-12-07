from flask_admin.contrib.sqla.filters import FilterEqual, FilterLike, FilterNotLike, DateEqualFilter, \
    DateNotEqualFilter, DateGreaterFilter, DateSmallerFilter, DateBetweenFilter, BooleanEqualFilter, \
    BooleanNotEqualFilter, FilterNotEqual
from flask_admin.form import rules
from wtforms import validators

from ClinicManagerApp.model.human.customer_model import CustomerModel
from ClinicManagerApp.view.base_model_view import BaseModelView


class CustomerView(BaseModelView):

    can_create = False
    can_delete = False

    # columns
    column_sortable_list = ['customer_id',
                            'first_name',
                            'last_name',
                            'date_of_birth']
    column_searchable_list = ['customer_id']
    column_filters = (FilterEqual(CustomerModel.first_name, name='Tên'),
                      FilterNotEqual(CustomerModel.first_name, name='Tên'),
                      FilterLike(CustomerModel.first_name, name='Tên'),
                      FilterNotLike(CustomerModel.first_name, name='Tên'),
                      FilterEqual(CustomerModel.last_name, name='Họ và tên đệm'),
                      FilterNotEqual(CustomerModel.last_name, name='Họ và tên đệm'),
                      FilterLike(CustomerModel.last_name, name='Họ và tên đệm'),
                      FilterNotLike(CustomerModel.last_name, name='Họ và tên đệm'),
                      DateEqualFilter(CustomerModel.date_of_birth, name='Ngày sinh'),
                      DateNotEqualFilter(CustomerModel.date_of_birth, name='Ngày sinh'),
                      DateGreaterFilter(CustomerModel.date_of_birth, name='Ngày sinh'),
                      DateSmallerFilter(CustomerModel.date_of_birth, name='Ngày sinh'),
                      DateBetweenFilter(CustomerModel.date_of_birth, name='Ngày sinh'),
                      BooleanEqualFilter(CustomerModel.sex, name='Giới tính'),
                      BooleanNotEqualFilter(CustomerModel.sex, name='Giới tính'),
                      FilterLike(CustomerModel.address, name='Địa chỉ'),
                      FilterNotLike(CustomerModel.address, name='Địa chỉ'),
                      FilterLike(CustomerModel.email, name='Email'),
                      FilterNotLike(CustomerModel.email, name='Email'),
                      FilterEqual(CustomerModel.phone_number, name='Số điện thoại'))

    column_default_sort = 'customer_id'

    column_labels = dict(customer_id='Mã',
                         first_name='Tên',
                         last_name='Họ và tên đệm',
                         date_of_birth='Ngày sinh',
                         sex='Giới tính',
                         address='Địa chỉ',
                         email='Email',
                         phone_number='Số điện thoại',
                         document_list='Danh sách tài liệu'
                         )
    column_editable_list = ('first_name',
                            'last_name',
                            'date_of_birth',
                            'sex',
                            'address',
                            'email',
                            'phone_number',
                            'document_list')

    # form
    form_args = dict(
        first_name=dict(validators=[validators.DataRequired(),
                                    validators.Length(min=1, max=20)],
                        render_kw={
                            'placeholder': 'Tên khách hàng'
                        }),
        last_name=dict(validators=[validators.DataRequired(),
                                   validators.Length(min=1, max=50)],
                       render_kw={
                           'placeholder': 'Họ và tên đệm khách hàng'
                       }),
        date_of_birth=dict(validators=[validators.DataRequired()], ),
        address=dict(validators=[validators.DataRequired(),
                                 validators.Length(min=1, max=100)],
                     render_kw={
                         'placeholder': 'Địa chỉ khách hàng'
                     }),
        email=dict(validators=[validators.Length(min=1, max=50)],
                   render_kw={
                       'placeholder': 'Địa chỉ email khách hàng'
                   }),
        phone_number=dict(validators=[validators.Length(min=1, max=12)],
                          render_kw={
                              'placeholder': 'Số điện thoại khách hàng'
                          }),
    )

    form_rules = [
        # Define field set with header text and four fields
        rules.FieldSet(('first_name',
                        'last_name',
                        'date_of_birth',
                        'sex',
                        'address',
                        'email',
                        'phone_number'), 'Thông tin khách hàng'),

        rules.FieldSet(('document_list',), 'Thông tin khác có liên quan')
    ]

    def scaffold_list_columns(self):
        return ['customer_id',
                'first_name',
                'last_name',
                'date_of_birth',
                'sex',
                'address',
                'email',
                'phone_number',
                'document_list']

    # def after_model_change(self, form, model, is_created):
    #     pass