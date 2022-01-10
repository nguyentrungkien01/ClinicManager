
from flask import request, jsonify
from flask_admin import expose
from flask_login import current_user

from ClinicManagerApp import app
from ClinicManagerApp.view.base_view import BaseView
from ClinicManagerApp.controller.admin.account_controller import change_password as cpw


class ChangePasswordView(BaseView):
    @expose('/')
    def index(self):
        return self.render('/admin/change_password.html')

    def is_accessible(self):
        return current_user.is_authenticated

    def is_visible(self):
        return False


@app.route('/api/staff/change_password', methods=['post'])
def change_password():
    username = request.json.get('username')
    old_password = request.json.get('old_password')
    new_password = request.json.get('new_password')
    return jsonify({
        'result': cpw(username=username, old_password=old_password, new_password=new_password)
    })
