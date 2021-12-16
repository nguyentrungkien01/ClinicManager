import json

from sqlalchemy import func

from ClinicManagerApp import db
from ClinicManagerApp.model.document.medical_examination_model import MedicalExaminationModel
from ClinicManagerApp.model.document.medical_bill_model import MedicalBillModel
from ClinicManagerApp.model.intermediary.medicine_examination_detail_model import medicine_examination_detail_model
from ClinicManagerApp.model.medicine.medicine_model import MedicineModel
from ClinicManagerApp.model.rule.medicine_unit_model import MedicineUnitModel

min_year = 2021
max_year = 2100


def report_revenue(month=None, quarter=None, year=None, **kwargs):
    data = db.session.query(MedicalBillModel.date_created,
                            func.count(MedicalBillModel.document_id),
                            func.sum(MedicalBillModel.medical_examination_price +
                                     MedicalBillModel.medical_price)) \
        .group_by(MedicalBillModel.date_created) \
        .order_by(MedicalBillModel.date_created)

    if month:
        data = data.filter(func.month(MedicalBillModel.date_created) == month)

    if quarter:
        data = data.filter(func.quarter(MedicalBillModel.date_created) == quarter)

    if year:
        data = data.filter(func.year(MedicalBillModel.date_created) == year)

    if kwargs.get('begin_index') and kwargs.get('end_index'):
        data.slice(kwargs.get('begin_index'), kwargs.get('end_index'))

    return data.all()


def report_medicine_using_frequency(month=None, quarter=None, year=None, **kwargs):
    data = db.session.query(MedicineModel.name,
                            MedicineUnitModel.name,
                            func.sum(medicine_examination_detail_model.c.amount),
                            func.count(MedicalExaminationModel.document_id)) \
        .join(MedicalExaminationModel) \
        .filter(MedicalExaminationModel.document_id == medicine_examination_detail_model.c.medical_examination_id) \
        .join(MedicineModel) \
        .filter(MedicineModel.medicine_id == medicine_examination_detail_model.c.medicine_id) \
        .join(MedicineUnitModel) \
        .filter(MedicineUnitModel.medicine_unit_id == MedicineModel.medicine_unit_id) \
        .group_by(MedicineModel.name, MedicineUnitModel.name) \
        .order_by(MedicineModel.name)

    if month:
        data = data.filter(func.month(MedicalExaminationModel.date_created) == month)

    if quarter:
        data = data.filter(func.quarter(MedicalExaminationModel.date_created) == quarter)

    if year:
        data = data.filter(func.year(MedicalExaminationModel.date_created) == year)

    if kwargs.get('begin_index') is not None and kwargs.get('begin_index') is not None:
        data = data.slice(int(kwargs.get('begin_index')), int(kwargs.get('end_index')))

    return data.all()


def report(report_type=None, **kwargs):
    if report_type == 'revenue':
        return report_revenue(month=kwargs.get('month'),
                              quarter=kwargs.get('quarter'),
                              year=kwargs.get('year'),
                              begin_index=kwargs.get('begin_index'),
                              end_index=kwargs.get('end_index'))

    if report_type == 'frequency_of_medicine_use':
        return report_medicine_using_frequency(month=kwargs.get('month'),
                                               quarter=kwargs.get('quarter'),
                                               year=kwargs.get('year'),
                                               begin_index=kwargs.get('begin_index'),
                                               end_index=kwargs.get('end_index'))


def parse_json_array(datas):
    result = []

    for d in datas:
        if len(d) == 3:
            sum = 0
            for val in datas:
                sum += float(val[2])
            temp = {
                'date': d[0].strftime('%A, %d/%m/%Y'),
                'amount': int(d[1]),
                'revenue': '{:,.1f} VND'.format(float(d[2])),
                'rate': '{:.2f} %'.format(float(d[2]) / sum * 100)
            }
        if len(d) == 4:
            temp = {
                'medicine_name': d[0],
                'medicine_unit': d[1],
                'medicine_amount': int(d[2]),
                'examination_amount': int(d[3])
            }
        result.append(temp)

    return json.dumps(result)


def get_amount(report_type=None, **kwargs):
    if report_type == 'revenue':
        return len(report_revenue(month=kwargs.get('month'),
                                  quarter=kwargs.get('quarter'),
                                  year=kwargs.get('year')))

    if report_type == 'frequency_of_medicine_use':
        return len(report_medicine_using_frequency(month=kwargs.get('month'),
                                                   quarter=kwargs.get('quarter'),
                                                   year=kwargs.get('year')))
