from flask_admin.contrib.sqla.filters import FilterLike, FilterNotLike, IntEqualFilter, IntNotEqualFilter, \
    IntGreaterFilter, IntSmallerFilter, FilterEqual, FilterNotEqual, FilterEmpty
from flask_admin.form import rules
from wtforms import validators
from wtforms.validators import DataRequired

from ClinicManagerApp.Model.ModelDatabase.Department.DepartmentModel import DepartmentModel
from ClinicManagerApp.Model.ModelView.BaseModelView import BaseModelView


class DepartmentModelView(BaseModelView):
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
                         staff_list='Danh sách nhân viên trong khoa')

    column_editable_list = ('name',
                            'capacity',
                            'description')

    # form
    form_rules = [
        rules.FieldSet(('name',
                        'capacity',
                        'description'), 'Thông tin khoa khám'),

        rules.FieldSet(('manager', 'staff_list'), 'Thông tin khác có liên quan'),

    ]

    form_args = dict(
        name=dict(validators=[DataRequired(), validators.Length(min=1, max=50)],
                  render_kw={
                      'placeholder': 'Tên khoa khám'
                  }),
        capacity=dict(validators=[DataRequired(), validators.NumberRange(min=1, max=20)], )
    )

    def scaffold_list_columns(self):
        return ['department_id',
                'name',
                'capacity',
                'manager',
                'staff_list',
                'description']
