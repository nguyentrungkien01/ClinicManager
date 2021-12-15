from flask_admin import expose

from ClinicManagerApp.view.base_view import BaseView


class RuleView(BaseView):
    @expose('/')
    def index(self):
        return self.render('admin/rule.html')