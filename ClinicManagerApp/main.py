from ClinicManagerApp import initTables, initAdmin
from ClinicManagerApp.controller.admin.admin_controller import *


@app.route('/')
def homePage():
    return "Hello"


if __name__ == '__main__':
    initTables()
    initAdmin()
    app.run(debug=True)
