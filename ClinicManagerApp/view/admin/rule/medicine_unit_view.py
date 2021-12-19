from flask_admin.contrib.sqla.filters import FilterLike, FilterNotLike
from flask_admin.form import rules
from wtforms import validators

from ClinicManagerApp.model.rule.medicine_unit_model import MedicineUnitModel
from ClinicManagerApp.view.base_model_view import BaseModelView


class MedicineUnitView(BaseModelView):
    # columns
    column_sortable_list = ['medicine_unit_id',
                            'name',
                            'medicine_list']
    column_searchable_list = ['medicine_unit_id',
                              'name']
    column_filters = (FilterLike(MedicineUnitModel.name, name='Tên đơn vị'),
                      FilterNotLike(MedicineUnitModel.name, name='Tên đơn vị'),
                      )

    column_default_sort = 'medicine_unit_id'

    column_labels = dict(medicine_unit_id='Mã',
                         name='Tên dơn vị',
                         medicine_list='Danh sách thuốc',
                         )
    column_editable_list = ('name',)
    column_list = ('medicine_unit_id', 'name')
    # form
    form_rules = [
        rules.FieldSet(('name',), 'Thông tin đơn vị thuốc'),

        rules.FieldSet(('medicine_list',), 'Thông tin khác có liên quan'),

    ]
    form_args = dict(
        name=dict(validators=[validators.DataRequired(), validators.Length(min=1, max=30)],
                  render_kw={
                      'placeholder': 'Tên đơn vị thuốc'
                  }),
    )

    def scaffold_list_columns(self):
        return ['medicine_unit_id',
                'name',
                'medicine_list']
