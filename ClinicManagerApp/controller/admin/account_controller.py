from flask import request
from flask_login import login_user
from werkzeug.utils import redirect

from ClinicManagerApp import login, app
from ClinicManagerApp.model.account.account_model import AccountModel


@login.user_loader
def load_user(user_id):
    return AccountModel.query.get(user_id)


@app.route("/admin", methods=['POST'])
def login_admin():
    if request.method == 'POST':
        username = request.form.get("username")
        password = request.form.get("password")
        user = AccountModel.query.filter(AccountModel.username.__eq__(username),
                                         AccountModel.password.__eq__(password)).first()
        if user:
            login_user(user=user)
    return redirect('/admin')
