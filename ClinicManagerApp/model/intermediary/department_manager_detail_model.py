from datetime import datetime

from sqlalchemy import Column, ForeignKey, Integer, DateTime

from ClinicManagerApp import db

department_manager_detail_model = db.Table('department_manager_detail_model',
                                           Column('department_id', Integer,
                                                  ForeignKey('department_model.department_id'), primary_key=True),
                                           Column('manager_id', Integer,
                                                  ForeignKey('doctor_model.staff_id'), primary_key=True),
                                           Column('joined_date', DateTime, default=datetime.now()),
                                           Column('leaved_date', DateTime, default=datetime.now())
                                           )
