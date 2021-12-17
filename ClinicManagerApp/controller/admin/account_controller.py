import datetime
import hashlib

from ClinicManagerApp import db
from ClinicManagerApp.model.account.account_model import AccountModel


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
