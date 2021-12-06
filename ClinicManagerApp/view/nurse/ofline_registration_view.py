from flask_admin import expose
from flask_login import current_user

from ClinicManagerApp.view.base_view import BaseView


class OfflineRegistrationView(BaseView):
    @expose('/')
    def index(self):
        return self.render('nurse/offline_registration.html')

    def is_accessible(self):
        return current_user.is_authenticated and \
               current_user.role.name.lower().__contains__('y tá')
