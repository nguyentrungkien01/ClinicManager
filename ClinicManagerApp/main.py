from flask import render_template

from ClinicManagerApp import initTables, initAdmin
from ClinicManagerApp.controller.admin.account_controller import *


@app.route('/')
def homePage():
    return render_template('/client/index.html')


if __name__ == '__main__':
    initTables()
    initAdmin()
    app.run(debug=True)
