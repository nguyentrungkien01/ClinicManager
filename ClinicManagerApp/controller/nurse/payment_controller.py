from sqlalchemy import func
from sqlalchemy.sql.elements import and_
from datetime import datetime
from ClinicManagerApp import db
from ClinicManagerApp.model.human.customer_model import CustomerModel
from ClinicManagerApp.model.human.nurse_model import NurseModel
from ClinicManagerApp.model.account.account_model import AccountModel
from ClinicManagerApp.model.human.doctor_model import DoctorModel
from ClinicManagerApp.model.rule.rule_model import RuleModel
from ClinicManagerApp.model.medicine.medicine_model import MedicineModel
from ClinicManagerApp.model.intermediary.medicine_examination_detail_model import medicine_examination_detail_model
from ClinicManagerApp.model.document.medical_examination_model import MedicalExaminationModel
from ClinicManagerApp.model.document.medical_bill_model import MedicalBillModel
from ClinicManagerApp.model.rule.medicine_unit_model import MedicineUnitModel


def get_customer_id_by_id_card(id_card=None):
    return db.session.query(CustomerModel.customer_id) \
        .filter(CustomerModel.id_card.__eq__(id_card)).first()[0]


def is_medical_examination_paid(medical_examination_id=None):
    try:
        data = db.session.query(MedicalBillModel.medical_examination_id) \
            .filter(MedicalBillModel.medical_examination_id.__eq__(int(medical_examination_id))) \
            .first()
        if data is None:
            return False
        return True
    except:
        return False


def is_medical_examination_exist(medical_examination_id=None):
    if medical_examination_id is None:
        return False
    data = db.session.query(MedicalExaminationModel) \
        .filter(MedicalExaminationModel.document_id.__eq__(medical_examination_id)).first()
    if data is None:
        return False
    return True


def get_customer_by_medical_examination_id(medical_examination_id=None):
    return db.session.query(CustomerModel.first_name,
                            CustomerModel.last_name,
                            CustomerModel.id_card,
                            CustomerModel.date_of_birth,
                            CustomerModel.sex) \
        .join(MedicalExaminationModel) \
        .filter(and_(MedicalExaminationModel.customer_id.__eq__(CustomerModel.customer_id),
                     MedicalExaminationModel.document_id.__eq__(medical_examination_id))) \
        .first()


def get_nurse_by_username(username=None):
    return db.session.query(NurseModel.staff_id,
                            NurseModel.first_name,
                            NurseModel.last_name) \
        .join(AccountModel) \
        .filter(and_(AccountModel.account_id.__eq__(NurseModel.account_id),
                     AccountModel.username.__eq__(str(username).strip()))) \
        .first()


def get_doctor_by_medical_examination_id(medical_examination_id=None):
    return db.session.query(DoctorModel.staff_id,
                            DoctorModel.first_name,
                            DoctorModel.last_name) \
        .join(MedicalExaminationModel) \
        .filter(and_(MedicalExaminationModel.doctor_id.__eq__(DoctorModel.staff_id),
                     MedicalExaminationModel.document_id.__eq__(medical_examination_id))) \
        .first()


def get_medical_examination_price():
    return RuleModel.query.filter(RuleModel.name.__eq__('tiền khám bệnh')).first().amount


def get_medical_examination_detail_by_id(medical_examination_id=None):
    return db.session.query(MedicineModel.name,
                            MedicineModel.unit_price,
                            func.sum(medicine_examination_detail_model.c.amount),
                            MedicineUnitModel.name) \
        .select_from(medicine_examination_detail_model) \
        .join(MedicineModel) \
        .join(MedicalExaminationModel) \
        .filter(MedicalExaminationModel.document_id.__eq__(medical_examination_id)) \
        .join(MedicineUnitModel) \
        .group_by(MedicineModel.name,
                  MedicineModel.unit_price,
                  MedicineUnitModel.name) \
        .all()


def get_bill_detail_by_medical_examination_id(username=None, medical_examination_id=None):
    if username is None or medical_examination_id is None:
        return None
    nurse = get_nurse_by_username(username=username)
    customer = get_customer_by_medical_examination_id(medical_examination_id=medical_examination_id)
    doctor = get_doctor_by_medical_examination_id(medical_examination_id=medical_examination_id)
    medicine_examination_detail = get_medical_examination_detail_by_id(medical_examination_id=medical_examination_id)
    medical_examination_price = get_medical_examination_price()
    medicine_list = []
    medicine_price_total = 0
    for medicine in medicine_examination_detail:
        medicine_price_total += medicine[1] * medicine[2]
        medicine_list.append({
            'name': medicine[0],
            'unit_price': '{:,.0f} VNĐ'.format(medicine[1]),
            'amount': medicine[2],
            'unit': medicine[3],
            'sum': '{:,.0f} VNĐ'.format(medicine[1] * medicine[2])
        })
    return {
        'customer': {
            'first_name': customer[0],
            'last_name': customer[1],
            'id_card': customer[2],
            'date_of_birth': datetime.strftime(customer[3], '%d/%m/%Y'),
            'sex': 'Nam' if customer[4].name.__eq__('MALE') else 'Nữ'
        },
        'nurse': {
            'staff_id': nurse[0],
            'first_name': nurse[1],
            'last_name': nurse[2]
        },
        'doctor': {
            'staff_id': doctor[0],
            'first_name': doctor[1],
            'last_name': doctor[2]
        },
        'medical_examination_id': medical_examination_id,
        'date_created': datetime.now().strftime('%d/%m/%Y %H:%M:%S %p'),
        'medicine_list': medicine_list,
        'medicine_price_total': '{:,.0f} VNĐ'.format(medicine_price_total),
        'medical_examination_price': '{:,.0f} VNĐ'.format(medical_examination_price),
        'total': '{:,.0f} VNĐ'.format(medicine_price_total + medical_examination_price)
    }


def convert_to_int_from_price_str(str_price):
    return int(str_price[0:str_price.index(' ')].replace(',', ''))


def get_data_for_bill(username=None, medical_examination_id=None):
    data = get_bill_detail_by_medical_examination_id(username=username,
                                                     medical_examination_id=medical_examination_id)
    return {
        'customer_id': get_customer_id_by_id_card(data['customer']['id_card']),
        'medical_examination_id': data['medical_examination_id'],
        'nurse_id': data['nurse']['staff_id'],
        'medical_examination_price': convert_to_int_from_price_str(data['medical_examination_price']),
        'medical_price': convert_to_int_from_price_str(data['medicine_price_total']),
        'total_price': convert_to_int_from_price_str(data['total'])
    }


def add_medical_bill(**kwargs):
    try:
        medical_bill = MedicalBillModel(customer_id=kwargs.get('customer_id'),
                                        medical_examination_id=kwargs.get('medical_examination_id'),
                                        nurse_id=kwargs.get('nurse_id'),
                                        medical_examination_price=kwargs.get('medical_examination_price'),
                                        medical_price=kwargs.get('medical_price'),
                                        total_price=kwargs.get('total_price'))
        db.session.add(medical_bill)
        db.session.commit()
        return True
    except:
        db.session.rollback()
    return False
