from operator import and_

from flask import json
from sqlalchemy import func, extract

from ClinicManagerApp import db
from ClinicManagerApp.model.medicine.medicine_model import MedicineModel
from ClinicManagerApp.model.document.medical_examination_model import MedicalExaminationModel
from ClinicManagerApp.model.document.medical_bill_model import MedicalBillModel
from ClinicManagerApp.model.intermediary.medicine_examination_detail_model import medicine_examination_detail_model

min_year = 2021
max_year = 2100


def statistic_revenue_month(from_month=None, to_month=None):
    data = db.session.query(func.month(MedicalBillModel.date_created),
                            func.sum(MedicalBillModel.medical_price +
                                     MedicalBillModel.medical_examination_price)) \
        .group_by(func.month(MedicalBillModel.date_created))

    if from_month and to_month:
        return data.filter(and_(extract('month', MedicalBillModel.date_created) >= from_month,
                                extract('month', MedicalBillModel.date_created) <= to_month)).all()
    return data.all()


def statistic_revenue_quarter(from_quarter=None, to_quarter=None):
    data = db.session.query(func.quarter(MedicalBillModel.date_created),
                            func.sum(MedicalBillModel.medical_price +
                                     MedicalBillModel.medical_examination_price)) \
        .group_by(func.quarter(MedicalBillModel.date_created))

    if from_quarter and to_quarter:
        return data.filter(and_(extract('quarter', MedicalBillModel.date_created) >= from_quarter,
                                extract('quarter', MedicalBillModel.date_created) <= to_quarter)).all()
    return data.all()


def statistic_revenue_year(from_year=None, to_year=None):
    data = db.session.query(func.year(MedicalBillModel.date_created),
                            func.sum(MedicalBillModel.medical_price +
                                     MedicalBillModel.medical_examination_price)) \
        .group_by(func.year(MedicalBillModel.date_created))

    if from_year and to_year:
        return data.filter(and_(extract('year', MedicalBillModel.date_created) >= from_year,
                                extract('year', MedicalBillModel.date_created) <= to_year)).all()
    return data.all()


def statistic_medicine_using_frequency_month(from_month=None, to_month=None, keyword=None):
    data = db.session.query(func.month(MedicalExaminationModel.date_created),
                            func.sum(medicine_examination_detail_model.c.amount)) \
        .join(MedicalExaminationModel) \
        .filter(MedicalExaminationModel.document_id == medicine_examination_detail_model.c.medical_examination_id) \
        .join(MedicineModel) \
        .filter(MedicineModel.medicine_id == medicine_examination_detail_model.c.medicine_id) \
        .group_by(func.month(MedicalExaminationModel.date_created))

    if keyword:
        data = data.filter(MedicineModel.name.__eq__(keyword))

    if from_month and to_month:
        return data.filter(and_(extract('month', MedicalExaminationModel.date_created) >= from_month,
                                extract('month', MedicalExaminationModel.date_created) <= to_month)).all()
    return data.all()


def statistic_medicine_using_frequency_quarter(from_quarter=None, to_quarter=None, keyword=None):
    data = db.session.query(func.quarter(MedicalExaminationModel.date_created),
                            func.sum(medicine_examination_detail_model.c.amount)) \
        .join(MedicalExaminationModel) \
        .filter(MedicalExaminationModel.document_id == medicine_examination_detail_model.c.medical_examination_id) \
        .join(MedicineModel) \
        .filter(MedicineModel.medicine_id == medicine_examination_detail_model.c.medicine_id) \
        .group_by(func.quarter(MedicalExaminationModel.date_created))

    if keyword:
        data = data.filter(MedicineModel.name.__eq__(keyword))

    if from_quarter and to_quarter:
        return data.filter(and_(extract('quarter', MedicalExaminationModel.date_created) >= from_quarter,
                                extract('quarter', MedicalExaminationModel.date_created) <= to_quarter)).all()
    return data.all()


def statistic_medicine_using_frequency_year(from_year=None, to_year=None, keyword=None):
    data = db.session.query(func.year(MedicalExaminationModel.date_created),
                            func.sum(medicine_examination_detail_model.c.amount)) \
        .join(MedicalExaminationModel) \
        .filter(MedicalExaminationModel.document_id == medicine_examination_detail_model.c.medical_examination_id) \
        .join(MedicineModel) \
        .filter(MedicineModel.medicine_id == medicine_examination_detail_model.c.medicine_id) \
        .group_by(func.year(MedicalExaminationModel.date_created))

    if keyword:
        data = data.filter(MedicineModel.name.__eq__(keyword))

    if from_year and to_year:
        return data.filter(and_(extract('year', MedicalExaminationModel.date_created) >= from_year,
                                extract('year', MedicalExaminationModel.date_created) <= to_year)).all()
    return data.all()


def statistic_medical_examination_month(from_month=None, to_month=None):
    data = db.session.query(func.month(MedicalExaminationModel.date_created),
                            func.count(MedicalExaminationModel.document_id)) \
        .group_by(func.month(MedicalExaminationModel.date_created))

    if from_month and to_month:
        return data.filter(and_(func.month(MedicalExaminationModel.date_created) >= from_month,
                                func.month(MedicalExaminationModel.date_created) <= to_month)).all()
    return data.all()


def statistic_medical_examination_quarter(from_quarter=None, to_quarter=None):
    data = db.session.query(func.quarter(MedicalExaminationModel.date_created),
                            func.count(MedicalExaminationModel.document_id)) \
        .group_by(func.quarter(MedicalExaminationModel.date_created))

    if from_quarter and to_quarter:
        return data.filter(and_(func.quarter(MedicalExaminationModel.date_created) >= from_quarter,
                                func.quarter(MedicalExaminationModel.date_created) <= to_quarter)).all()
    return data.all()


def statistic_medical_examination_year(from_year=None, to_year=None):
    data = db.session.query(func.year(MedicalExaminationModel.date_created),
                            func.count(MedicalExaminationModel.document_id)) \
        .group_by(func.year(MedicalExaminationModel.date_created))

    if from_year and to_year:
        return data.filter(and_(func.year(MedicalExaminationModel.date_created) >= from_year,
                                func.year(MedicalExaminationModel.date_created) <= to_year)).all()
    return data.all()


def statistic_revenue(statistic_condition, **kwargs):
    if statistic_condition.__contains__('month'):
        return statistic_revenue_month(kwargs.get('from_time'), kwargs.get('to_time'))

    if statistic_condition.__contains__('quarter'):
        return statistic_revenue_quarter(kwargs.get('from_time'), kwargs.get('to_time'))

    if statistic_condition.__contains__('year'):
        return statistic_revenue_year(kwargs.get('from_time'), kwargs.get('to_time'))


def statistic_medicine_using_frequency(statistic_condition, **kwargs):
    if not kwargs.get('keyword'):
        return []

    if statistic_condition.__contains__('month'):
        return statistic_medicine_using_frequency_month(kwargs.get('from_time'),
                                                        kwargs.get('to_time'),
                                                        kwargs.get('keyword'))
    if statistic_condition.__contains__('quarter'):
        return statistic_medicine_using_frequency_quarter(kwargs.get('from_time'),
                                                          kwargs.get('to_time'),
                                                          kwargs.get('keyword'))
    if statistic_condition.__contains__('year'):
        return statistic_medicine_using_frequency_year(kwargs.get('from_time'),
                                                       kwargs.get('to_time'),
                                                       kwargs.get('keyword'))


def statistic_medical_examination(statistic_condition, **kwargs):
    if statistic_condition.__contains__('month'):
        return statistic_medical_examination_month(kwargs.get('from_time'), kwargs.get('to_time'))

    if statistic_condition.__contains__('quarter'):
        return statistic_medical_examination_quarter(kwargs.get('from_time'), kwargs.get('to_time'))

    if statistic_condition.__contains__('year'):
        return statistic_medical_examination_year(kwargs.get('from_time'), kwargs.get('to_time'))


def statistic(statistic_type=None, statistic_condition=None, **kwargs):
    data = None
    if statistic_type == 'revenue':
        data = statistic_revenue(statistic_condition, **kwargs)

    if statistic_type == 'frequency_of_medicine_use':
        data = statistic_medicine_using_frequency(statistic_condition, **kwargs)

    if statistic_type == 'frequency_of_examination':
        data = statistic_medical_examination(statistic_condition, **kwargs)

    return data


def parse_json_array(datas):
    result = []
    for d in datas:
        if len(d) == 1:
            temp = {'value': d[0]}
        if len(d) == 2:
            temp = {'key': d[0], 'value': float(d[1])}
        result.append(temp)
    return json.dumps(result)


def get_name_medicine(keyword=None):
    return db.session.query(MedicineModel.name).filter(MedicineModel.name.like('%{}%'.format(keyword))).all()
