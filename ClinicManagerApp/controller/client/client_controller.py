
from sqlalchemy import func

from ClinicManagerApp import db
from ClinicManagerApp.model.department.department_model import DepartmentModel
from ClinicManagerApp.model.human.doctor_model import DoctorModel
from ClinicManagerApp.model.rule.major_model import MajorModel


def get_amount_department():
    return {
        'amount': db.session.query(func.count(DepartmentModel.department_id)).first()[0]
    }


def get_infor_department(begin_index=None, end_index=None):
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


def get_amount_doctor(major_id=None):
    data = db.session.query(func.count(DoctorModel.staff_id))

    if major_id is not None:
        data = data.join(MajorModel).filter(MajorModel.major_id.__eq__(major_id))

    return {
        'amount': data.first()[0]
    }


def get_infor_doctor(major_id=None, begin_index=None, end_index=None):
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
