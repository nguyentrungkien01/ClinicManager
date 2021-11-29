from flask_admin import BaseView, expose


class AnalysisModelView(BaseView):
    @expose('/')
    def index(self):
        return self.render('admin/analysis.html')
