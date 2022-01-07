from flask import request, jsonify
from flask_admin import expose
from flask_login import current_user

from ClinicManagerApp import app
from ClinicManagerApp.view.base_view import BaseView
from ClinicManagerApp.controller.doctor.medical_examination_controller import get_customer_id_card as gcid, \
    parse_json_array, get_medicine_unit as gmu, get_medicine_name as gmn, get_customer_id_card_eq, get_doctor_infor, \
    save_medicine_examination as sme, get_customer_name_by_id_card
from ClinicManagerApp.controller.admin.statistic_controller import get_medicine_name


class MedicalExaminationCreationView(BaseView):
    @expose('/')
    def index(self):
        return self.render('doctor/medical_examination_creation.html')

    def is_accessible(self):
        return current_user.is_authenticated and \
               current_user.role.name.lower().__contains__('bác sĩ')


@app.route('/api/doctor/customer_id_card', methods=['post'])
def get_customer_id_card():
    id_card = request.json.get('id_card')
    if id_card:
        data = gcid(str(id_card).strip())
    else:
        data = []
    return parse_json_array(data)


@app.route('/api/doctor/medicine_name', methods=['post'])
def get_medicine_name_doctor():
    medicine_name = request.json.get('medicine_name')
    if medicine_name:
        data = get_medicine_name(str(medicine_name).strip())
    else:
        data = []
    return parse_json_array(data)


@app.route('/api/doctor/medicine_unit', methods=['post'])
def get_medicine_unit():
    medicine_name = request.json.get('medicine_name')
    return parse_json_array([gmu(medicine_name)])


@app.route('/api/doctor/check_medicine_name', methods=['post'])
def check_medicine_name_doctor():
    medicine_name = request.json.get('medicine_name')
    if medicine_name:
        data = gmn(str(medicine_name).strip())
    else:
        data = []
    return parse_json_array(data)


@app.route('/api/doctor/check_customer_id_card', methods=['post'])
def check_customer_id_card_doctor():
    id_card = request.json.get('id_card')
    if id_card:
        data = get_customer_id_card_eq(str(id_card).strip())
    else:
        data = []
    return parse_json_array(data)


@app.route('/api/doctor/current_doctor', methods=['post'])
def get_current_doctor_infor():
    data = get_doctor_infor(current_user.username)
    return jsonify({
        'info': '{} {}'.format(data[0][1], data[0][0])
    })


@app.route('/api/doctor/save_medical_examination_data', methods=['post'])
def save_medical_examination():
    id_card = request.json.get('id_card')
    symptom = request.json.get('symptom')
    predicted_disease = request.json.get('predicted_disease')
    medicine_list = request.json.get('medicine_list')
    add_result = sme(id_card=id_card,
                     symptom=symptom,
                     predicted_disease=predicted_disease,
                     medicine_list=medicine_list)

    return jsonify({
        'result': add_result['result'],
        'medical_examination_id': add_result['medical_examination_id']

    })


@app.route('/api/doctor/customer_name', methods=['post'])
def get_customer_fullname():
    id_card = request.json.get('id_card')
    customer_fullname = get_customer_name_by_id_card(id_card)
    return jsonify({
        'result': '{} {}'.format(customer_fullname[1], customer_fullname[0])
    })

