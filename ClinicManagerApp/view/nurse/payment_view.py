from statistics import mean

from flask_admin import expose
from flask_login import current_user
from flask import redirect, url_for, request, jsonify
from ClinicManagerApp import app
from ClinicManagerApp.view.base_view import BaseView
from ClinicManagerApp.controller.nurse.payment_controller import get_bill_detail_by_medical_examination_id, \
    get_data_for_bill, add_medical_bill as amb, is_medical_examination_paid, is_medical_examination_exist


class PaymentView(BaseView):
    medical_examination_search_result = None

    @expose('/')
    def index(self):
        return self.render('nurse/payment.html',
                           medical_examination_search_result=get_medical_examination_search_result())

    def is_accessible(self):
        return current_user.is_authenticated and \
               current_user.role.name.lower().__contains__('y tá')


def get_medical_examination_search_result():
    result = PaymentView.medical_examination_search_result
    PaymentView.medical_examination_search_result = None
    return result


@app.route('/api/nurse/medical_examination_id', methods=['post'])
def get_medical_examination_data():
    medical_examination_id = request.form.get('medical_examination_id')

    PaymentView.medical_examination_search_result = \
        is_medical_examination_exist(medical_examination_id=medical_examination_id)

    if PaymentView.medical_examination_search_result:
        PaymentView.medical_examination_search_result = \
            is_medical_examination_paid(medical_examination_id=medical_examination_id)

        if medical_examination_id is not None and PaymentView.medical_examination_search_result == False:
            PaymentView.medical_examination_search_result = \
                get_bill_detail_by_medical_examination_id(username=current_user.username,
                                                          medical_examination_id=medical_examination_id)
    else:
        PaymentView.medical_examination_search_result = True
    return redirect(url_for('paymentview.index'))


@app.route('/api/nurse/payment', methods=['post'])
def add_medical_bill():
    medical_examination_id = int(request.json.get('medical_examination_id'))
    data = get_data_for_bill(username=current_user.username,
                             medical_examination_id=medical_examination_id)
    return jsonify({
        'result': amb(customer_id=data['customer_id'],
                      medical_examination_id=data['medical_examination_id'],
                      nurse_id=data['nurse_id'],
                      medical_examination_price=data['medical_examination_price'],
                      medical_price=data['medical_price'],
                      total_price=data['total_price'])
    })
