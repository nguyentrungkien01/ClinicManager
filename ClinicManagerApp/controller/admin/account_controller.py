import datetime
import hashlib
from ClinicManagerApp import db
from ClinicManagerApp.model.account.account_model import AccountModel
from ClinicManagerApp.model.human.staff_model import StaffModel
from ClinicManagerApp.model.rule.role_model import RoleModel
from ClinicManagerApp.model.department.department_model import DepartmentModel


def get_account(username=None, password=None):
    if username and password:
        return AccountModel.query.filter(AccountModel.username.__eq__(username),
                                         AccountModel.password.__eq__(
                                             hashlib.md5(password.encode('utf8')).hexdigest())).first()


def get_account_by_id(account_id=None):
    if account_id:
        return AccountModel.query.get(account_id)


def set_lass_access(account=None):
    if account:
        account.last_access = datetime.datetime.now()
        db.session.add(account)
        db.session.commit()


def change_password(username=None, old_password=None, new_password=None):
    if username and old_password and new_password:
        account = AccountModel.query.filter(AccountModel.username.__eq__(username),
                                            AccountModel.password.__eq__(
                                                hashlib.md5(old_password.encode('utf8')).hexdigest())).first()
        if account:
            account.password = hashlib.md5(new_password.encode('utf8')).hexdigest()
            db.session.add(account)
            db.session.commit()
            return True
        return False
    return False


def get_role_name_by_role_id(role_id=None):
    return db.session.query(RoleModel.name) \
        .filter(RoleModel.role_id.__eq__(role_id)).first()[0]


def get_info_current_user(username=None):
    data = db.session.query(StaffModel.first_name,
                            StaffModel.last_name,
                            StaffModel.date_of_birth,
                            StaffModel.date_of_work,
                            StaffModel.sex,
                            StaffModel.phone_number,
                            StaffModel.address,
                            StaffModel.email,
                            RoleModel.name,
                            DepartmentModel.name) \
        .select_from(StaffModel) \
        .join(DepartmentModel) \
        .join(AccountModel) \
        .join(RoleModel) \
        .filter(AccountModel.username.__eq__(username)).first()
    if data is None:
        return data
    return {
        'first_name': data[0],
        'last_name': data[1],
        'date_of_birth': datetime.datetime.strftime(data[2], '%d/%m/%Y'),
        'date_of_work': datetime.datetime.strftime(data[3], '%d/%m/%Y'),
        'sex': 'Nam' if data[4] == 'MALE' else 'Nữ',
        'phone_number': data[5],
        'address': data[6],
        'email': data[7],
        'role': data[8],
        'department': data[9]
    }
