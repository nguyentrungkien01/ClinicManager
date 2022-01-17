import datetime
import calendar
from sqlalchemy import func, desc

from ClinicManagerApp import db
from ClinicManagerApp.model.intermediary.medicine_examination_detail_model import medicine_examination_detail_model
from ClinicManagerApp.model.medicine.medicine_model import MedicineModel
from ClinicManagerApp.model.rule.medicine_unit_model import MedicineUnitModel
from ClinicManagerApp.model.document.medical_bill_model import MedicalBillModel
from ClinicManagerApp.model.department.department_model import DepartmentModel
from ClinicManagerApp.model.human.staff_model import StaffModel
from ClinicManagerApp.model.human.customer_model import CustomerModel
from ClinicManagerApp.model.category.category_model import CategoryModel
def get_top_medicine_selling():
    medicine_list = db.session.query(MedicineModel.name,
                                     MedicineUnitModel.name,
                                     func.sum(medicine_examination_detail_model.c.amount *
                                              MedicineModel.unit_price)) \
        .select_from(medicine_examination_detail_model) \
        .join(MedicineModel) \
        .join(MedicineUnitModel) \
        .group_by(MedicineModel.name) \
        .order_by(desc(func.sum(medicine_examination_detail_model.c.amount *
                                MedicineModel.unit_price))) \
        .slice(0, 10) \
        .all()
    data = []
    for medicine in medicine_list:
        data.append({
            'name': medicine[0],
            'unit': medicine[1],
            'total_price': '{:,.0f} VNĐ'.format(medicine[2]), })
    return data


def get_amount_customer_in_month():
    month = datetime.datetime.now().month
    year = datetime.datetime.now().year
    days = [day for day in range(1, calendar.monthrange(year, month)[1] + 1)]
    datas = []
    for d in days:
        datas.append(db.session.query(func.count(MedicalBillModel.document_id)) \
                     .filter(func.month(MedicalBillModel.date_created).__eq__(month),
                             func.year(MedicalBillModel.date_created).__eq__(year),
                             func.day(MedicalBillModel.date_created).__eq__(d)).first()[0]
                     )
    return {
        'month': month,
        'year': year,
        'days': days,
        # 'datas': [100, 3, 4, 12, 9, 21, 23, 13, 5, 21, 34, 5, 1, 23, 23, 13, 27, 12, 2, 3, 4, 1, 0, 30, 2, 1, 3, 1, 28,
        #           29, 16]
        'datas': datas
    }


def get_revenue_today():
    return db.session.query(func.sum(MedicalBillModel.total_price)) \
        .filter(func.month(MedicalBillModel.date_created).__eq__(datetime.datetime.now().month),
                func.year(MedicalBillModel.date_created).__eq__(datetime.datetime.now().year),
                func.day(MedicalBillModel.date_created).__eq__(datetime.datetime.day)).first()[0]


def get_revenue_yesterday():
    yesterday = datetime.datetime.today() - datetime.timedelta(days=1)
    return db.session.query(func.sum(MedicalBillModel.total_price)) \
        .filter(func.month(MedicalBillModel.date_created).__eq__(yesterday.month),
                func.year(MedicalBillModel.date_created).__eq__(yesterday.year),
                func.day(MedicalBillModel.date_created).__eq__(yesterday.day)).first()[0]


def get_revenue():
    return {
        'yesterday': '{:,.0f} VNĐ'.format(0 if get_revenue_yesterday() is None else get_revenue_yesterday()),
        'today': '{:,.0f} VNĐ'.format(0 if get_revenue_today() is None else get_revenue_today())
    }


def get_general_amount():
    return {
        'department_amount': db.session.query(func.count(DepartmentModel.department_id)).first()[0],
        'staff_amount': db.session.query(func.count(StaffModel.staff_id)).first()[0],
        'customer_amount': db.session.query(func.count(CustomerModel.customer_id)).first()[0],
        'medicine_amount': db.session.query(func.count(MedicineModel.medicine_id)).first()[0],
        'category_amount': db.session.query(func.count(CategoryModel.category_id)).first()[0],

    }