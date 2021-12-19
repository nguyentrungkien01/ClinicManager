from flask_admin.contrib.sqla.filters import FilterLike, FilterNotLike
from flask_admin.form import rules
from wtforms import validators

from ClinicManagerApp.model.rule.role_model import RoleModel
from ClinicManagerApp.view.base_model_view import BaseModelView


class RoleView(BaseModelView):
    # columns
    column_sortable_list = ['role_id',
                            'name']
    column_searchable_list = ['role_id',
                              'name']
    column_filters = (FilterLike(RoleModel.name, name='Vai trò'),
                      FilterNotLike(RoleModel.name, name='Vai trò'))

    column_default_sort = 'role_id'

    column_labels = dict(role_id='Mã',
                         name='Vai trò',
                         account_list='Danh sách tài khoản')
    column_editable_list = ('name',)
    column_list = ('role_id', 'name')

    # form
    form_rules = [
        rules.FieldSet(('name',), 'Thông tin vai trò'),

        rules.FieldSet(('account_list',), 'Thông tin khác có liên quan'),

    ]
    form_args = dict(
        name=dict(validators=[validators.DataRequired(), validators.Length(min=1, max=30)],
                  render_kw={
                      'placeholder': 'Vai trò'
                  }),
    )

    def scaffold_list_columns(self):
        return ['role_id',
                'name',
                'account_list']
