from ClinicManagerApp.ModelView.BaseModelView import BaseModelView


class AccountModelView(BaseModelView):
    column_exclude_list = ['avatar']
    column_sortable_list = ['account_id', 'username', 'last_access']
