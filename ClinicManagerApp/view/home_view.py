from flask import jsonify
from flask_admin import AdminIndexView, expose
from flask_login import current_user

from ClinicManagerApp import app
from ClinicManagerApp.controller.admin.home_page_controller import get_top_medicine_selling, \
    get_amount_customer_in_month, get_revenue as gr, get_general_amount as gga


class HomeView(AdminIndexView):
    def is_visible(self):
        return not current_user.is_authenticated

    @expose('/')
    def index(self):
        return self.render('/admin/home_page.html',
                           top_medicine_list=get_top_medicine_selling())


@app.route('/api/homepage/top_medicine')
def get_top_medicine_list():
    return jsonify(get_top_medicine_selling())


@app.route('/api/homepage/customer_arrive_frequenly')
def get_amount_customer_arrive():
    return jsonify(get_amount_customer_in_month())


@app.route('/api/homepage/revenue')
def get_revenue():
    return jsonify(gr())


@app.route('/api/homepage/general_amount')
def get_general_amount():
    return jsonify(gga())
