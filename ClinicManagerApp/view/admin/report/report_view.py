from flask import request
from flask_admin import expose

from ClinicManagerApp import app
from ClinicManagerApp.controller.admin.report_controller import parse_json_array, report, get_amount as ga
from ClinicManagerApp.controller.utils_controller import readJsonFile
from ClinicManagerApp.view.base_view import BaseView


class ReportView(BaseView):
    @expose('/')
    def index(self):
        selection = readJsonFile('report_data.json')
        return self.render('admin/report.html', selections=selection)


@app.route('/api/report', methods=['post'])
def get_data_report():
    # import pdb
    # pdb.set_trace()
    report_type = request.json.get('report_type')
    month = request.json.get('month')
    quarter = request.json.get('quarter')
    year = request.json.get('year')
    begin_index = request.json.get('begin_index')
    end_index = request.json.get('end_index')
    data = report(report_type=report_type, month=month, quarter=quarter, year=year,
                  begin_index=begin_index, end_index=end_index)
    return parse_json_array(data)


@app.route('/api/amount_report', methods=['post'])
def get_amount():
    report_type = request.json.get('report_type')
    month = request.json.get('month')
    quarter = request.json.get('quarter')
    year = request.json.get('year')
    return {'amount': ga(report_type=report_type, month=month, quarter=quarter, year=year)}


@app.route('/api/export_report', methods=['post'])
def get_all():
    report_type = request.json.get('report_type')
    month = request.json.get('month')
    quarter = request.json.get('quarter')
    year = request.json.get('year')
    return parse_json_array(report(report_type=report_type, month=month, quarter=quarter, year=year))
