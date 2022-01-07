from flask import render_template
from ClinicManagerApp import initTables, initAdmin, app


@app.route('/')
def home_page():
    return render_template('/client/home.html')


if __name__ == '__main__':
    initTables()
    initAdmin()
    app.run(debug=True)
