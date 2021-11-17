from ClinicManagerApp import app, db

@app.route('/')
def homePage():
    try:
        db.drop_all()
        #db.create_all()
    except:
        db.session.rollback()
        return "fail"
    return "successful"


if __name__ == '__main__':
    app.run(debug=True)
