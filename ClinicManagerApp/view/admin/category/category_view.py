from flask_admin.contrib.sqla.filters import FilterEmpty, FilterEqual, FilterNotEqual, FilterLike, FilterNotLike
from flask_admin.form import rules
from wtforms import validators
from wtforms.validators import DataRequired

from ClinicManagerApp.model.category.category_model import CategoryModel
from ClinicManagerApp.view.base_model_view import BaseModelView


class CategoryView(BaseModelView):
    column_sortable_list = ['category_id',
                            'name']
    column_searchable_list = ['category_id']

    column_filters = (FilterEqual(CategoryModel.name, name='Tên kho thuốc'),
                      FilterNotEqual(CategoryModel.name, name='Tên kho thuốc'),
                      FilterLike(CategoryModel.name, name='Tên kho thuốc'),
                      FilterNotLike(CategoryModel.name, name='Tên kho thuốc'),
                      FilterEmpty(column='medicine_list', name='Danh sách thuốc trong kho'))
    column_default_sort = 'category_id'
    column_labels = dict(category_id='Mã',
                         name='Tên kho thuốc',
                         medicine_list='Danh sách thuốc trong kho')
    column_editable_list = ('name',)
    column_list = ('category_id', 'name')

    form_rules = [
        rules.FieldSet(('name',), 'Thông tin kho thuốc'),

        rules.FieldSet(('medicine_list',), 'Thông tin khác có liên quan'),

    ]

    form_args = dict(
        name=dict(validators=[validators.DataRequired(),validators.Length(min=1, max=50)],
                  render_kw={
                      'placeholder': 'Tên kho thuốc'
                  }),
    )
    form_columns = ['name',
                    'medicine_list']

    def scaffold_list_columns(self):
        return ['category_id',
                'name',
                'medicine_list']
