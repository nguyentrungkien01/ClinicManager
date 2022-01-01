from flask import request
from flask_admin import expose

from ClinicManagerApp import app
from ClinicManagerApp.controller.admin.statistic_controller import statistic, parse_json_array, get_medicine_name
from ClinicManagerApp.controller.utils_controller import readJsonFile
from ClinicManagerApp.view.base_view import BaseView


class StatisticView(BaseView):
    @expose('/')
    def index(self):
        selection = readJsonFile('statistic_data.json')
        return self.render('admin/statistic/statistic.html', selections=selection)


@app.route('/api/statistic', methods=['post'])
def get_data_statistic():
    # import pdb
    # pdb.set_trace()
    statistic_type = request.json.get('statistic_type')
    statistic_condition = request.json.get('statistic_condition')
    keyword = request.json.get('name_medicine')
    from_time = request.json.get('from_time')
    to_time = request.json.get('to_time')
    if statistic_type and statistic_condition:
        data = statistic(statistic_type=statistic_type,
                         statistic_condition=statistic_condition,
                         keyword=keyword)
        if from_time and to_time and int(from_time) <= int(to_time):
            data = statistic(statistic_type=statistic_type,
                             statistic_condition=statistic_condition,
                             from_time=int(from_time),
                             to_time=int(to_time),
                             keyword=keyword)
    else:
        data = statistic('revenue', 'month_statistic')
    return parse_json_array(data)


@app.route('/api/name_medicine', methods=['post'])
def get_medicine_name_statistic():
    # import pdb
    # pdb.set_trace()
    name_medicine = request.json.get('name_medicine')
    if name_medicine:
        data = get_medicine_name(str(name_medicine).strip())
    else:
        data = []
    return parse_json_array(data)



