import datetime

from ClinicManagerApp import detail_registration, db
from ClinicManagerApp.model.human.customer_model import CustomerModel
from ClinicManagerApp.model.rule.rule_model import RuleModel


def get_amount_registration_daily():
    return RuleModel.query.filter(RuleModel.name.__eq__('số lượng')).first().amount


def check_amount_registration_daily():
    return len(detail_registration['customer_list']) <= get_amount_registration_daily()


def is_exist_customer_daily(id_card=None):
    pdt = detail_registration['date']
    if not pdt:
        return False
    dt = datetime.datetime.now().strftime('%Y-%m-%d')
    if pdt == dt:
        for c in detail_registration['customer_list']:
            if c.__eq__(id_card):
                return True
    return False


def is_exist_customer_db(id_card=None):
    if CustomerModel.query.filter(CustomerModel.id_card.__eq__(id_card)).first():
        return True
    return False


def reset_daily_list():
    pdt = detail_registration['date']
    dt = datetime.datetime.now().strftime('%Y-%m-%d')
    if pdt and pdt != dt:
        detail_registration['date'] = dt
        detail_registration['customer_list'] = []


def add_customer_db(customer=None):
    if is_exist_customer_db(customer.id_card):
        return True
    try:
        db.session.add(customer)
        db.session.commit()
        return True
    except:
        db.session.rollback()
    return False


def get_fullname_customer_list_by_id_card():
    result_list = []
    for id_card in detail_registration['customer_list']:
        data = db.session.query(CustomerModel.last_name, CustomerModel.first_name) \
            .filter(CustomerModel.id_card.__eq__(id_card)).first()
        result_list.append('{} {}'.format(data[0], data[1]))
    return result_list


def add_customer_daily(id_card=None):
    reset_daily_list()
    if not check_amount_registration_daily() or is_exist_customer_daily(id_card=id_card):
        return False
    detail_registration['date'] = datetime.datetime.now().strftime('%Y-%m-%d')
    detail_registration['customer_list'].append(id_card)
    return True
