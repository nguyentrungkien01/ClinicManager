from flask_admin import expose
from flask_login import current_user

from ClinicManagerApp.view.base_view import BaseView
from ClinicManagerApp.controller.admin.account_controller import get_info_current_user


class ProfileView(BaseView):
    @expose('/')
    def index(self):
        return self.render('/admin/profile.html',
                           infor_current_user=get_info_current_user(username=current_user.username))

    def is_accessible(self):
        return current_user.is_authenticated

    def is_visible(self):
        return False