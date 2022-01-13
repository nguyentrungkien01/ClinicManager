from sqlalchemy import func, desc

from ClinicManagerApp import db
from ClinicManagerApp.model.feedback.feedback_model import FeedbackModel


def get_feedback_amount():
    data = db.session.query(func.count(FeedbackModel.feedback_id)).first()[0]
    return {
        'amount': 0 if data is None else data
    }


def get_general_feedback_info(begin_index=None, end_index=None):
    data = db.session.query(FeedbackModel.feedback_id,
                            FeedbackModel.subject,
                            FeedbackModel.customer_name,
                            FeedbackModel.date_created,
                            FeedbackModel.status) \
        .order_by(desc(FeedbackModel.date_created))\
        .order_by(FeedbackModel.status)
    if begin_index is not None and end_index is not None:
        data = data.slice(begin_index, end_index)

    data = data.all()
    feedback_list = []

    for feedback in data:
        feedback_list.append({
            'feedback_id': feedback[0],
            'feedback_subject': feedback[1],
            'customer_name': feedback[2],
            'date_created': feedback[3].strftime('%d/%m/%Y %H:%M:%S %p'),
            'feedback_status': feedback[4]
        })
    return feedback_list


def get_feedback_content(feedback_id=None):
    data = db.session.query(FeedbackModel.gmail,
                            FeedbackModel.content) \
        .filter(FeedbackModel.feedback_id.__eq__(feedback_id)).first()
    return {
        'gmail': data[0],
        'content': data[1]
    }


def set_feedback_status(feedback_id=None):
    try:
        feedback = FeedbackModel.query.filter(FeedbackModel.feedback_id.__eq__(feedback_id)).first()
        feedback.status = True
        db.session.add(feedback)
        db.session.commit()
        return {
            'result': True
        }
    except:
        db.session.rollback()
    return {
        'resuslt': False
    }
