from flask_admin import BaseView
from flask_login import current_user


class BaseView(BaseView):

    def is_accessible(self):
        return current_user.is_authenticated and \
               current_user.role.name.lower().__contains__('quản trị viên')