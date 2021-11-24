
from ClinicManagerApp.ModelView.BaseModelView import BaseModelView


class DepartmentModelView(BaseModelView):
    column_sortable_list = ['department_id', 'name', 'capacity']
