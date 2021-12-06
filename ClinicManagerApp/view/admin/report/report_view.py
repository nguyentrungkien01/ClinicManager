from flask_admin import expose

from ClinicManagerApp.view.base_view import BaseView


class ReportView(BaseView):
    @expose('/')
    def index(self):
        return self.render('admin/report.html')
