from flask_admin import expose
from flask_login import logout_user, current_user
from flask import redirect

from ClinicManagerApp.view.base_view import BaseView


class LogoutView(BaseView):
    @expose('/')
    def index(self):
        logout_user()

        return redirect('/admin')

    def is_accessible(self):
        return current_user.is_authenticated

    def is_visible(self):
        return False
