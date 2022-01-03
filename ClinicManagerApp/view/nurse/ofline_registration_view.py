
from flask_admin import expose
from flask_login import current_user
from flask import redirect, request, url_for
from ClinicManagerApp import app, detail_registration
from ClinicManagerApp.view.base_view import BaseView
from ClinicManagerApp.model.human.customer_model import CustomerModel
from ClinicManagerApp.controller.nurse.offline_registration_controller import \
    add_customer_daily, add_customer_db, get_amount_registration_daily


class OfflineRegistrationView(BaseView):
    add_customer_result = None

    @expose('/')
    def index(self):
        return self.render('nurse/offline_registration.html',
                           amount=(get_amount_registration_daily()- len(detail_registration['customer_list'])),
                           add_customer_result=get_add_customer_result())

    def is_accessible(self):
        return current_user.is_authenticated and \
               current_user.role.name.lower().__contains__('y tá')


def get_add_customer_result():
    result = OfflineRegistrationView.add_customer_result
    OfflineRegistrationView.add_customer_result = None
    return result


def add_customer(customer=None):
    OfflineRegistrationView.add_customer_result = add_customer_daily(id_card=customer.id_card)
    if OfflineRegistrationView.add_customer_result:
        OfflineRegistrationView.add_customer_result = add_customer_db(customer=customer)


@app.route('/api/nurse/customer_offline_data', methods=['post'])
def get_data_offline_registration():
    id_card = request.form['id_card']
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    sex = request.form['sex']
    date_of_birth = request.form['date_of_birth']
    address = request.form['address']
    phone_number = request.form['phone_number']
    customer = CustomerModel(id_card=id_card, first_name=first_name, last_name=last_name,
                             sex=sex.upper(), date_of_birth=date_of_birth, address=address,
                             phone_number=phone_number)
    add_customer(customer=customer)
    return redirect(url_for('offlineregistrationview.index'))
