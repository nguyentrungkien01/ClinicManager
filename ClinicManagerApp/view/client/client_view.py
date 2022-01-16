from flask import render_template, redirect, url_for, request, jsonify
import json
from ClinicManagerApp import app
from ClinicManagerApp.controller.nurse.offline_registration_controller import get_remaining_amount_daily_slot, \
    add_customer_daily, add_customer_db
from ClinicManagerApp.model.human.customer_model import CustomerModel
from ClinicManagerApp.controller.client.client_controller import get_department_amount as gda, \
    get_department_infor as gdi, get_doctor_amount as gdra, get_major as gm, \
    get_doctor_info as gdri, add_feedback, get_exp_doctor_amount, get_staff_amount, get_medical_examination_amount
from ClinicManagerApp.controller.utils_controller import readJsonFile, writeJsonFile


class AddingResult:
    add_customer_result = None


@app.route('/')
def homepage():
    return render_template('/client/home.html',
                           amount_remaining_slot=get_remaining_amount_daily_slot(),
                           add_customer_result=get_add_customer_result(),
                           counter={
                               'exp_doctor_amount':get_exp_doctor_amount()['amount'],
                               'staff_amount':get_staff_amount()['amount'],
                               'doctor_amount': gdra()['amount'],
                               'medical_examination_amount':get_medical_examination_amount()['amount']
                           })


def get_add_customer_result():
    result = AddingResult.add_customer_result
    AddingResult.add_customer_result = None
    return result


def add_customer(customer=None):
    daily_customer_list = readJsonFile('daily_customer_list.json')
    AddingResult.add_customer_result = add_customer_daily(id_card=customer.id_card)
    if AddingResult.add_customer_result:
        AddingResult.add_customer_result = add_customer_db(customer=customer)
        if not AddingResult.add_customer_result:
            writeJsonFile(filename='daily_customer_list.json', data=daily_customer_list)


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
    return jsonify(gda())


@app.route('/api/client/infor_department', methods=['post'])
def get_department_info():
    begin_index = request.json.get('begin_index')
    end_index = request.json.get('end_index')
    return json.dumps(gdi(begin_index=int(begin_index), end_index=int(end_index)))


@app.route('/api/client/major_doctor')
def get_major():
    return json.dumps(gm())


@app.route('/api/client/amount_doctor', methods=['post'])
def get_doctor_amount():
    major_id = request.json.get('major_id')
    return jsonify(gdra(major_id=major_id))


@app.route('/api/client/doctor_list', methods=['post'])
def get_doctor_info():
    major_id = request.json.get('major_id')
    begin_index = request.json.get('begin_index')
    end_index = request.json.get('end_index')
    return json.dumps(gdri(major_id=major_id, begin_index=begin_index, end_index=end_index))


@app.route('/api/client/send_feedback', methods=['post'])
def send_feedback():
  
    customer_fullname = request.json.get('customer_fullname')
    customer_email = request.json.get('customer_email')
    feedback_subject = request.json.get('feedback_subject')
    feedback_content = request.json.get('feedback_content')

    return jsonify({
        'result': add_feedback(customer_fullname=customer_fullname,
                               customer_email=customer_email,
                               feedback_subject=feedback_subject,
                               feedback_content=feedback_content)
    })
