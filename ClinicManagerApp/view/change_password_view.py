from flask_admin import expose
from flask_login import current_user

from ClinicManagerApp.view.base_view import BaseView


class ChangePasswordView(BaseView):
    @expose('/')
    def index(self):
        return self.render('/change_password.html')

    def is_accessible(self):
        return current_user.is_authenticated
