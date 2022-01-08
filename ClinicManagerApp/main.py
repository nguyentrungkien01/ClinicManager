from ClinicManagerApp import initTables, initAdmin, app


if __name__ == '__main__':
    initTables()
    initAdmin()
    app.run(debug=True)
