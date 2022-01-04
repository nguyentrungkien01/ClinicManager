import datetime
import json

from flask_login import current_user
from sqlalchemy.sql.elements import and_

from ClinicManagerApp import db
from ClinicManagerApp.model.human.customer_model import CustomerModel
from ClinicManagerApp.model.rule.medicine_unit_model import MedicineUnitModel
from ClinicManagerApp.model.medicine.medicine_model import MedicineModel
from ClinicManagerApp.model.human.doctor_model import DoctorModel
from ClinicManagerApp.model.account.account_model import AccountModel
from ClinicManagerApp.model.document.medical_examination_model import MedicalExaminationModel
from ClinicManagerApp.model.intermediary.medicine_examination_detail_model import medicine_examination_detail_model


def get_customer_id_card(keyword=None):
    return db.session.query(CustomerModel.id_card) \
        .filter(CustomerModel.id_card.like('{}%'.format(keyword))) \
        .slice(0, 10) \
        .all()



def get_medicine_unit(medicine_name=None):
    return db.session.query(MedicineUnitModel.name) \
        .join(MedicineModel) \
        .filter(and_(MedicineUnitModel.medicine_unit_id.__eq__(MedicineModel.medicine_unit_id),
                     MedicineModel.name.__eq__(str(medicine_name).strip()))) \
        .first()


def get_medicine_name(medicine_name=None):
    return db.session.query(MedicineModel.name) \
        .filter(MedicineModel.name.__eq__(medicine_name)) \
        .all()


def get_customer_id_card_eq(id_card=None):
    return db.session.query(CustomerModel.id_card) \
        .filter(CustomerModel.id_card.__eq__(id_card)) \
        .all()


def get_doctor_infor(username=None):
    return db.session.query(DoctorModel.first_name,
                            DoctorModel.last_name) \
        .join(AccountModel) \
        .filter(and_(AccountModel.staff_id.__eq__(DoctorModel.staff_id),
                     AccountModel.username.__eq__(username))) \
        .all()


def get_medicine_id_by_name(name=None):
    return db.session.query(MedicineModel.medicine_id) \
        .filter(MedicineModel.name.__eq__(name)).first()[0]


def get_customer_id_by_id_card(id_card=None):
    return db.session.query(CustomerModel.customer_id) \
        .filter(CustomerModel.id_card.__eq__(id_card)).first()[0]


def get_doctor_id_by_username(username=None):
    return db.session.query(DoctorModel.staff_id) \
        .join(AccountModel) \
        .filter(and_(AccountModel.staff_id.__eq__(DoctorModel.staff_id),
                     AccountModel.username.__eq__(username))) \
        .all()[0][0]


def get_id_medical_examination(medical_examination=None):
    return db.session.query(MedicalExaminationModel.document_id) \
        .filter(and_(MedicalExaminationModel.symptom.__eq__(medical_examination.symptom),
                     MedicalExaminationModel.date_created.__eq__(medical_examination.date_created),
                     MedicalExaminationModel.predicted_disease.__eq__(medical_examination.predicted_disease),
                     MedicalExaminationModel.customer_id.__eq__(medical_examination.customer_id),
                     MedicalExaminationModel.doctor_id.__eq__(medical_examination.doctor_id))) \
        .first()[0]


def save_medicine_examination(**kwargs):
    try:
        id_card = kwargs.get('id_card')
        symptom = kwargs.get('symptom')
        predicted_disease = kwargs.get('predicted_disease')
        medicine_list = kwargs.get('medicine_list')
        medical_examination = MedicalExaminationModel(symptom=symptom,
                                                      predicted_disease=predicted_disease,
                                                      date_created=datetime.datetime.now(),
                                                      customer_id=int(get_customer_id_by_id_card(id_card)),
                                                      doctor_id=int(get_doctor_id_by_username(current_user.username)))
        db.session.add(medical_examination)
        db.session.commit()

        for medicine in medicine_list:
            statement = medicine_examination_detail_model.insert().values(
                medicine_id=get_medicine_id_by_name(medicine['name']),
                medical_examination_id=get_id_medical_examination(medical_examination),
                amount=int(medicine['amount']),
                dosage=medicine['dosage'],
                using_method=medicine['using_method'])
            db.session.execute(statement)
            db.session.commit()
        return True
    except:
        db.session.rollback()
        return False


def parse_json_array(datas):
    result = []
    for d in datas:
        if len(d) == 1:
            result.append({'value': d[0]})
    return json.dumps(result)
