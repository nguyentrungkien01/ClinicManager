from flask_admin.contrib.sqla.filters import FilterLike, FilterNotLike
from flask_admin.form import rules
from wtforms import validators

from ClinicManagerApp.model.rule.major_model import MajorModel
from ClinicManagerApp.view.base_model_view import BaseModelView


class MajorView(BaseModelView):
    # columns
    column_sortable_list = ['major_id',
                            'name']
    column_searchable_list = ['major_id',
                              'name']
    column_filters = (FilterLike(MajorModel.name, name='Chuyên ngành bác sĩ'),
                      FilterNotLike(MajorModel.name, name='Chuyên ngành bác sĩ'))

    column_default_sort = 'major_id'

    column_labels = dict(major_id='Mã',
                         name='Chuyên ngành bác sĩ',
                         doctor_list='Danh sách bác sĩ')
    column_editable_list = ('name',)
    column_list = ('major_id', 'name')

    # form
    form_rules = [
        rules.FieldSet(('name',), 'Thông tin chuyên ngành bác sĩ'),

        rules.FieldSet(('doctor_list',), 'Thông tin khác có liên quan'),

    ]
    form_args = dict(
        name=dict(validators=[validators.DataRequired(), validators.Length(min=1, max=30)],
                  render_kw={
                      'placeholder': 'Chuyên ngành bác sĩ'
                  }),
    )

    def scaffold_list_columns(self):
        return ['major_id',
                'name',
                'doctor_list']
