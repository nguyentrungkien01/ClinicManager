from flask_admin import expose

from ClinicManagerApp.view.base_view import BaseView


class StatisticView(BaseView):
    @expose('/')
    def index(self):
        return self.render('admin/statistic.html')
