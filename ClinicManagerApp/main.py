from flask import render_template

from ClinicManagerApp import initTables, initAdmin, app


@app.route('/')
def homePage():
    return render_template('/client/index.html')


if __name__ == '__main__':
    initTables()
    initAdmin()
    app.run(debug=True)
