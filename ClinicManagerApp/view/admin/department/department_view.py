from flask_admin.contrib.sqla.filters import FilterLike, FilterNotLike, IntEqualFilter, IntNotEqualFilter, \
    IntGreaterFilter, IntSmallerFilter, FilterEqual, FilterNotEqual, FilterEmpty
from flask_admin.form import rules
from wtforms import validators, FileField
from wtforms.validators import DataRequired
import cloudinary.uploader
from ClinicManagerApp.model.department.department_model import DepartmentModel
from ClinicManagerApp.view.base_model_view import BaseModelView


class DepartmentView(BaseModelView):
    # columns
    column_sortable_list = ['department_id',
                            'name',
                            'capacity']
    column_searchable_list = ['department_id',
                              'name',
                              'capacity']
    column_filters = (FilterLike(DepartmentModel.name, name='Tên khoa khám'),
                      FilterNotLike(DepartmentModel.name, name='Tên khoa khám'),
                      FilterEqual(DepartmentModel.name, name='Tên khoa khám'),
                      FilterNotEqual(DepartmentModel.name, name='Tên khoa khám'),
                      IntEqualFilter(DepartmentModel.capacity, name='Sức chứa'),
                      IntNotEqualFilter(DepartmentModel.capacity, name='Sức chứa'),
                      IntGreaterFilter(DepartmentModel.capacity, name='Sức chứa'),
                      IntSmallerFilter(DepartmentModel.capacity, name='Sức chứa'),
                      FilterEmpty('staff_list', name='Danh sách nhân viên trong khoa'),
                      FilterEmpty('manager', name='Trưởng khoa'))

    column_default_sort = 'department_id'

    column_labels = dict(department_id='Mã',
                         name='Tên khoa khám',
                         capacity='Sức chứa',
                         description='Mô tả',
                         manager='Trường khoa',
                         staff_list='Danh sách nhân viên trong khoa',
                         logo='Logo')

    column_list = ('department_id', 'name', 'capacity', 'logo', 'manager', 'description')

    # form
    form_rules = [
        rules.FieldSet(('name',
                        'capacity',
                        'logo',
                        'description',), 'Thông tin khoa khám'),

        rules.FieldSet(('manager', 'staff_list'), 'Thông tin khác có liên quan'),

    ]

    form_extra_fields = {
        'logo': FileField('Logo')
    }

    form_args = dict(
        name=dict(validators=[DataRequired(), validators.Length(min=1, max=150)],
                  render_kw={
                      'placeholder': 'Tên khoa khám'
                  }),
        capacity=dict(validators=[DataRequired(), validators.NumberRange(min=1, max=20)], )
    )

    def on_model_change(self, form, department_model, is_created):
        if form.logo.data:
            res = cloudinary.uploader.upload(form.logo.data, folder='department_logo')
            department_model.set_logo(str(res['secure_url']))
        else:
            department_model.set_logo('')

    def scaffold_list_columns(self):
        return ['department_id',
                'name',
                'capacity',
                'logo',
                'manager',
                'staff_list',
                'description']
