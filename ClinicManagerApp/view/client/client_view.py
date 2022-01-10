from flask import render_template, redirect, url_for, request, jsonify
import json
from ClinicManagerApp import app
from ClinicManagerApp.controller.nurse.offline_registration_controller import get_remaining_amount_daily_slot, \
    add_customer_daily, add_customer_db
from ClinicManagerApp.model.human.customer_model import CustomerModel
from ClinicManagerApp.controller.client.client_controller import get_amount_department as gad, \
    get_infor_department as gid, get_amount_doctor as gmd, get_major as gm, \
    get_infor_doctor as gido


class AddingResult:
    add_customer_result = None


@app.route('/')
def homepage():
    return render_template('/client/home.html',
                           amount_remaining_slot=get_remaining_amount_daily_slot(),
                           add_customer_result=get_add_customer_result())


def get_add_customer_result():
    result = AddingResult.add_customer_result
    AddingResult.add_customer_result = None
    return result


def add_customer(customer=None):
    AddingResult.add_customer_result = add_customer_daily(id_card=customer.id_card)
    if AddingResult.add_customer_result:
        AddingResult.add_customer_result = add_customer_db(customer=customer)


@app.route('/api/client/online_registration', methods=['post'])
def make_online_registration():
    id_card = request.form['id_card']
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    sex = request.form['sex']
    date_of_birth = request.form['date_of_birth']
    email = request.form['email']
    address = request.form['address']
    phone_number = request.form['phone_number']
    customer = CustomerModel(id_card=id_card, first_name=first_name, last_name=last_name,
                             sex=sex.upper(), date_of_birth=date_of_birth, address=address,
                             phone_number=phone_number, email=email)
    add_customer(customer=customer)
    return redirect(url_for('homepage'))


@app.route('/api/client/amount_department')
def get_amount_department():
    return jsonify(gad())


@app.route('/api/client/infor_department', methods=['post'])
def get_infor_department():
    begin_index = request.json.get('begin_index')
    end_index = request.json.get('end_index')
    return json.dumps(gid(begin_index=int(begin_index), end_index=int(end_index)))


@app.route('/api/client/major_doctor')
def get_major():
    return json.dumps(gm())


@app.route('/api/client/amount_doctor', methods=['post'])
def get_amount_doctor():
    major_id = request.json.get('major_id')
    return jsonify(gmd(major_id=major_id))


@app.route('/api/client/doctor_list', methods=['post'])
def get_infor_doctor():
    major_id = request.json.get('major_id')
    begin_index = request.json.get('begin_index')
    end_index = request.json.get('end_index')
    return json.dumps(gido(major_id=major_id, begin_index=begin_index, end_index=end_index))
