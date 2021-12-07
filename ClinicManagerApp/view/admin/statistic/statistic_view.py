from flask_admin import expose

from ClinicManagerApp.controller.utils_controller import readJsonFile
from ClinicManagerApp.view.base_view import BaseView


class StatisticView(BaseView):
    @expose('/')
    def index(self):
        selection = readJsonFile('statistic_data.json')
        return self.render('admin/statistic.html', selections=selection)
