from flask import render_template

<<<<<<< HEAD
from ClinicManagerApp import initTables, initAdmin
from ClinicManagerApp.controller.admin.account_controller import *
=======
from ClinicManagerApp import initTables, initAdmin, app
>>>>>>> 53c8531ff497b574d8c55c2b90e7f166a00a33b0


@app.route('/')
def homePage():
    return render_template('/client/index.html')


if __name__ == '__main__':
    initTables()
    initAdmin()
    app.run(debug=True)
