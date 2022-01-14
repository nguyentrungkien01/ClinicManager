
import cloudinary.uploader
from flask import request
from flask_admin.contrib.sqla.filters import BooleanEqualFilter, FilterLike, FilterEmpty, DateEqualFilter, \
    DateNotEqualFilter, DateGreaterFilter, DateSmallerFilter, DateBetweenFilter, FilterNotLike, BooleanNotEqualFilter
from flask_admin.form import rules
from flask_login import login_user
from werkzeug.utils import redirect
from wtforms import validators, FileField, PasswordField
from wtforms.validators import DataRequired

from ClinicManagerApp import login, app
from ClinicManagerApp.controller.admin.account_controller import get_account, get_account_by_id, set_lass_access
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
                              'is_active', ]
    column_filters = (FilterLike(RoleModel.name, name='Vai trò'),
                      FilterNotLike(RoleModel.name, name='Vai trò'),
                      BooleanEqualFilter(AccountModel.is_active, name='Trạng thái kích hoạt'),
                      BooleanNotEqualFilter(AccountModel.is_active, name='Trạng thái kích hoạt'),
                      DateEqualFilter(AccountModel.last_access, name='Truy cập lân cuối'),
                      DateNotEqualFilter(AccountModel.last_access, name='Truy cập lân cuối'),
                      DateGreaterFilter(AccountModel.last_access, name='Truy cập lân cuối'),
                      DateSmallerFilter(AccountModel.last_access, name='Truy cập lân cuối'),
                      DateBetweenFilter(AccountModel.last_access, name='Truy cập lân cuối'),
                      FilterEmpty(AccountModel.avatar, name='Ảnh đại diện'))
    column_default_sort = 'account_id'
    column_labels = dict(account_id='Mã',
                         username='Tên đăng nhập',
                         password='Mật khẩu',
                         role='Vai trò',
                         is_active='Kích hoạt',
                         last_access='Truy cập lần cuối',
                         avatar='Ảnh đại diện'
                         )

    # form
    form_rules = [
        # Define field set with header text and four fields
        rules.FieldSet(('username',
                        'password',
                        'role',
                        'avatar',
                        'is_active'), 'Thông tin tài khoản')
    ]
    form_extra_fields = {
        'password': PasswordField('Mật khẩu',
                                  validators=[DataRequired(), validators.Length(min=8, max=12)],
                                  render_kw={
                                      'placeholder': 'Mật khẩu'
                                  }),
        'avatar': FileField('Ảnh đại diện')
    }
    form_args = dict(
        username=dict(validators=[DataRequired(), validators.Length(min=5, max=20)],
                      render_kw={
                          'placeholder': 'Tên đăng nhập'
                      }),
        role=dict(validators=[validators.DataRequired()], )
    )

    def on_model_change(self, form, account_model, is_created):
        if form.avatar.data:
            res = cloudinary.uploader.upload(form.avatar.data, folder='avatar_account')
            account_model.set_avatar(str(res['secure_url']))
        else:
            account_model.set_avatar('')

        if request.form.get('avatar'):
            account_model.set_password(form.password.data)
        else:
            account_model.set_password('12345678')

    def scaffold_list_columns(self):
        return ['account_id',
                'username',
                'password',
                'is_active',
                'role',
                'avatar',
                'last_access']


@login.user_loader
def load_account(account_id):
    return get_account_by_id(account_id)


@app.route("/admin", methods=['POST'])
def login_admin():
    if request.method == 'POST':
        username = request.form.get("username")
        password = request.form.get("password")
        if username and password:
            account = get_account(username, password)
        else:
            account = None
        if account and account.is_active == True:
            login_user(user=account)
            set_lass_access(account)
    return redirect('/admin')
