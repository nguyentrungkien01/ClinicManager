from flask_admin.contrib.sqla.filters import FilterLike, FilterNotLike, IntEqualFilter, IntNotEqualFilter, \
    IntGreaterFilter, IntSmallerFilter
from flask_admin.form import rules
from wtforms import validators

from ClinicManagerApp.model.rule.rule_model import RuleModel
from ClinicManagerApp.view.base_model_view import BaseModelView


class RuleView(BaseModelView):
    # columns
    column_sortable_list = ['rule_id',
                            'name',
                            'amount']
    column_searchable_list = ['rule_id',
                              'name',
                              'amount']
    column_filters = (FilterLike(RuleModel.name, name='Tên quy định'),
                      FilterNotLike(RuleModel.name, name='Tên quy định'),
                      IntEqualFilter(RuleModel.amount, name='Số lượng'),
                      IntNotEqualFilter(RuleModel.amount, name='Số lượng'),
                      IntGreaterFilter(RuleModel.amount, name='Số lượng'),
                      IntSmallerFilter(RuleModel.amount, name='Số lượng'))

    column_default_sort = 'rule_id'

    column_labels = dict(rule_id='Mã quy định',
                         name='Tên quy định',
                         amount='Số lượng',
                         )
    column_editable_list = ('name',
                            'amount')

    # form
    form_rules = [
        rules.FieldSet(('name',
                        'amount'), 'Thông tin quy định'),
    ]
    form_args = dict(
        name=dict(validators=[validators.DataRequired(), validators.Length(min=1, max=150)],
                  render_kw={
                      'placeholder': 'Tên quy định'
                  }),
        amount=dict(validators=[validators.DataRequired(), validators.NumberRange(0, 100000000)], )
    )

    def scaffold_list_columns(self):
        return ['rule_id',
                'name',
                'amount']

