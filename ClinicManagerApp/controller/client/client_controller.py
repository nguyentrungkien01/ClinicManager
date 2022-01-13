from sqlalchemy import func
from twilio.rest import Client

from ClinicManagerApp import db
from ClinicManagerApp.model.department.department_model import DepartmentModel
from ClinicManagerApp.model.human.doctor_model import DoctorModel
from ClinicManagerApp.model.rule.major_model import MajorModel
from ClinicManagerApp.model.feedback.feedback_model import FeedbackModel
from ClinicManagerApp.model.human.staff_model import StaffModel
from ClinicManagerApp.model.document.medical_examination_model import MedicalExaminationModel


def get_department_amount():
    return {
        'amount': db.session.query(func.count(DepartmentModel.department_id)).first()[0]
    }


def get_department_infor(begin_index=None, end_index=None):
    data = db.session.query(DepartmentModel.name,
                            DepartmentModel.logo,
                            DepartmentModel.description) \
        .order_by(DepartmentModel.name)

    if begin_index is not None and end_index is not None:
        data = data.slice(begin_index, end_index)
    data = data.all()

    department_list = []
    for d in data:
        department_list.append({
            'department_name': d[0],
            'department_logo': d[1],
            'department_description': d[2]
        })
    return department_list


def get_doctor_amount(major_id=None):
    data = db.session.query(func.count(DoctorModel.staff_id))

    if major_id is not None:
        data = data.join(MajorModel).filter(MajorModel.major_id.__eq__(major_id))

    return {
        'amount': data.first()[0]
    }


def get_doctor_info(major_id=None, begin_index=None, end_index=None):
    data = db.session.query(DoctorModel.last_name,
                            DoctorModel.first_name,
                            DoctorModel.avatar,
                            DoctorModel.phone_number,
                            MajorModel.name,
                            DepartmentModel.name,
                            DoctorModel.facebook_link,
                            DoctorModel.twitter_link) \
        .join(MajorModel) \
        .filter(MajorModel.major_id.__eq__(DoctorModel.major_id)) \
        .join(DepartmentModel) \
        .filter(DepartmentModel.department_id.__eq__(DoctorModel.contained_department_id))

    if major_id is not None:
        data = data.filter(MajorModel.major_id.__eq__(major_id))

    data = data.order_by(DoctorModel.first_name)

    if begin_index is not None and end_index is not None:
        data = data.slice(begin_index, end_index)

    data = data.all()
    doctor_list = []
    for doctor in data:
        doctor_list.append({
            'full_name': '{} {}'.format(doctor[0], doctor[1]),
            'avatar': doctor[2],
            'phone_number': doctor[3],
            'major': doctor[4],
            'department': doctor[5],
            'facebook_link': doctor[6],
            'twitter_link': doctor[7]
        })
    return doctor_list


def get_major():
    data = db.session.query(MajorModel.major_id, MajorModel.name) \
        .order_by(MajorModel.major_id).all()
    major_list = []
    for major in data:
        major_list.append({
            'major_id': major[0],
            'major_name': major[1]
        })
    return major_list


def add_feedback(**kwargs):
    customer_fullname = kwargs.get('customer_fullname')
    customer_email = kwargs.get('customer_email')
    feedback_subject = kwargs.get('feedback_subject')
    feedback_content = kwargs.get('feedback_content')
    try:
        feedback = FeedbackModel(customer_name=customer_fullname,
                                 gmail=customer_email,
                                 content=feedback_content,
                                 subject=feedback_subject)
        db.session.add(feedback)
        db.session.commit()
        return True
    except:
        db.session.rollback()
        return False
    pass


def get_staff_amount():
    return {
        'amount': db.session.query(func.count(StaffModel.staff_id)).first()[0]
    }


def get_exp_doctor_amount():
    return {
        'amount': db.session.query(func.count(DoctorModel.staff_id))\
        .filter(DoctorModel.exp_year.__gt__(1.0)).first()[0]
    }


def get_medical_examination_amount():
    return {
        'amount': db.session.query(func.count(MedicalExaminationModel.document_id)).first()[0]
    }