from flask_admin.contrib.sqla.filters import BooleanEqualFilter, FilterLike, FilterEmpty, DateEqualFilter, \
    DateNotEqualFilter, DateGreaterFilter, DateSmallerFilter, DateBetweenFilter, FilterNotLike, BooleanNotEqualFilter
from flask_admin.form import rules
from wtforms import validators
from wtforms.validators import DataRequired

from ClinicManagerApp.model.account.account_model import AccountModel
from ClinicManagerApp.model.rule.role_model import RoleModel
from ClinicManagerApp.view.base_model_view import BaseModelView


class AccountView(BaseModelView):
    # columns
    column_sortable_list = ['account_id',
                            'username',
                            'last_access']
    column_searchable_list = ['account_id',
                              'username',
                              'is_active']
    column_filters = (FilterLike(RoleModel.name, name='Vai trò'),
                      FilterNotLike(RoleModel.name, name='Vai trò'),
                      BooleanEqualFilter(AccountModel.is_active, name='Trạng thái kích hoạt'),
                      BooleanNotEqualFilter(AccountModel.is_active, name='Trạng thái kích hoạt'),
                      DateEqualFilter(AccountModel.last_access, name='Truy cập lân cuối'),
                      DateNotEqualFilter(AccountModel.last_access, name='Truy cập lân cuối'),
                      DateGreaterFilter(AccountModel.last_access, name='Truy cập lân cuối'),
                      DateSmallerFilter(AccountModel.last_access, name='Truy cập lân cuối'),
                      DateBetweenFilter(AccountModel.last_access, name='Truy cập lân cuối'),
                      FilterEmpty(AccountModel.avatar, name='Ảnh đại diện'),
                      FilterEmpty(column='staff', name='Nhân viên sở hữu'))

    column_default_sort = 'account_id'
    column_labels = dict(account_id='Mã',
                         username='Tên đăng nhập',
                         password='Mật khẩu',
                         role='Vai trò',
                         is_active='Kích hoạt',
                         last_access='Truy cập lần cuối',
                         avatar='Ảnh đại diện',
                         staff='Nhân viên sở hữu'
                         )
    column_editable_list = ('role',
                            'is_active',
                            'avatar',
                            'staff')

    # form
    form_rules = [
        # Define field set with header text and four fields
        rules.FieldSet(('username',
                        'password',
                        'role',
                        'avatar',
                        'is_active'), 'Thông tin tài khoản'),

        rules.FieldSet(('staff',), 'Thông tin khác có liên quan'),

    ]
    form_args = dict(
        username=dict(validators=[DataRequired(), validators.Length(min=5, max=20)],
                      render_kw={
                          'placeholder': 'Tên đăng nhập'
                      }),
        password=dict(validators=[DataRequired()],
                      render_kw={
                          'placeholder': 'Mật khẩu'
                      }),
        role=dict(validators=[validators.DataRequired()], )

    )

    def scaffold_list_columns(self):
        return ['account_id',
                'username',
                'password',
                'is_active',
                'role',
                'avatar',
                'last_access',
                'staff']
