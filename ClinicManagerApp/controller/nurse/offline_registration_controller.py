import datetime

from ClinicManagerApp import db, client
from ClinicManagerApp.model.human.customer_model import CustomerModel
from ClinicManagerApp.model.rule.rule_model import RuleModel
from ClinicManagerApp.controller.utils_controller import readJsonFile, writeJsonFile


def get_amount_registration_daily():
    return RuleModel.query.filter(RuleModel.name.like('%số lượng%')).first().amount


def get_remaining_amount_daily_slot():
    return get_amount_registration_daily() - len(readJsonFile('daily_customer_list.json')['customer_list'])


def check_amount_registration_daily():
    daily_customer_list = readJsonFile('daily_customer_list.json')
    return len(daily_customer_list['customer_list']) <= get_amount_registration_daily()


def is_exist_customer_daily(id_card=None):
    daily_customer_list = readJsonFile('daily_customer_list.json')
    pdt = daily_customer_list['date']
    if not pdt:
        return False
    dt = datetime.datetime.now().strftime('%Y-%m-%d')
    if pdt == dt:
        for c in daily_customer_list['customer_list']:
            if c.__eq__(id_card):
                return True
    return False


def is_exist_customer_db(id_card=None):
    if CustomerModel.query.filter(CustomerModel.id_card.__eq__(id_card)).first():
        return True
    return False


def reset_daily_list():
    daily_customer_list = readJsonFile('daily_customer_list.json')
    pdt = daily_customer_list['date']
    dt = datetime.datetime.now().strftime('%Y-%m-%d')
    if pdt and pdt != dt:
        daily_customer_list['date'] = None
        daily_customer_list['customer_list'] = []
        writeJsonFile('daily_customer_list.json', daily_customer_list)


def add_customer_db(customer=None, send_message=False):
    if is_exist_customer_db(customer.id_card):
        return True
    message = 'Phòng khám Trung Thành xin kính chào quý khách! ' \
              'Khách hàng: {} {} có số ' \
              'CCCD: {}. ' \
              'Đã đăng ký thành công lịch hẹn khám tại phòng khám Trung Thành vào lúc {}' \
        .format(customer.last_name, customer.first_name, customer.id_card, datetime.datetime.now())
    phone_number = '+84' + customer.phone_number[1:]
    try:
        if send_message:
            client.messages \
                .create(
                from_='+15706092840',
                body=message,
                to='+84982482975'
            )
        db.session.add(customer)
        db.session.commit()
        return True
    except:
        db.session.rollback()

    return False


def get_customer_daily_list():
    result_list = []
    daily_customer_list = readJsonFile('daily_customer_list.json')
    for id_card in daily_customer_list['customer_list']:
        data = db.session.query(CustomerModel.last_name,
                                CustomerModel.first_name,
                                CustomerModel.date_of_birth,
                                CustomerModel.address,
                                CustomerModel.sex) \
            .filter(CustomerModel.id_card.__eq__(id_card)).first()
        result_list.append({
            'fullname': '{} {}'.format(data[0], data[1]),
            'date_of_birth': data[2].strftime('%d/%m/%Y'),
            'address': data[3],
            'sex': 'nam' if data[4].name == 'MALE' else 'nữ'
        })
    return result_list


def add_customer_daily(id_card=None):
    reset_daily_list()
    if not check_amount_registration_daily() or is_exist_customer_daily(id_card=id_card):
        return False
    daily_customer_list = readJsonFile('daily_customer_list.json')
    daily_customer_list['date'] = datetime.datetime.now().strftime('%Y-%m-%d')
    daily_customer_list['customer_list'].append(id_card)
    writeJsonFile('daily_customer_list.json', daily_customer_list)
    return True
