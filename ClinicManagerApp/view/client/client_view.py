from flask import render_template, redirect, url_for

from ClinicManagerApp import app
from ClinicManagerApp.controller.nurse.offline_registration_controller import get_remaining_amount_daily_slot


@app.route('/')
def homepage():
    return render_template('/client/home.html', amount_remaining_slot=get_remaining_amount_daily_slot())


@app.route('/api/client/online_registration', methods=['post'])
def make_online_registration():

    return redirect(url_for('homepage'))
