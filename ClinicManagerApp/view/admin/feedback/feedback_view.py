import json

from flask import request, jsonify
from flask_admin import expose

from ClinicManagerApp import app
from ClinicManagerApp.controller.admin.feedback_controller import get_feedback_amount as gfa, \
    get_feedback_content as gfc, get_general_feedback_info as ggfi
from ClinicManagerApp.view.base_view import BaseView


class FeedbackView(BaseView):
    @expose('/')
    def index(self):
        return self.render('/admin/feedback.html')


@app.route('/api/admin/feedback_amount')
def get_feedback_amount():
    return jsonify(gfa())


@app.route('/api/admin/feedback_content', methods=['post'])
def get_feedback_content():
    feedback_id = request.json.get('feedback_id')
    return json.dumps(gfc(feedback_id=feedback_id))


@app.route('/api/admin/general_feedback_infor', methods=['post'])
def get_general_feedback_info():
    begin_index = request.json.get('begin_index')
    end_index = request.json.get('end_index')
    return json.dumps(ggfi(begin_index=begin_index, end_index=end_index))
