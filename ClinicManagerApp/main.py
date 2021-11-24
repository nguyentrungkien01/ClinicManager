from ClinicManagerApp import app, initAdmin,  initTables


@app.route('/')
def homePage():
    return "Hello"


if __name__ == '__main__':
    initTables()
    initAdmin()
    app.run(debug=True)
