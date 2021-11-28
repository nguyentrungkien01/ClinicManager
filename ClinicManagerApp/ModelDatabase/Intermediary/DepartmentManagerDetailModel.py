from sqlalchemy import Column, ForeignKey, Integer, String, DateTime

from ClinicManagerApp import db

department_manager_detail_model = db.Table('department_manager_detail_model',
                                           Column('department_id', Integer,
                                                  ForeignKey('department_model.department_id'), primary_key=True),
                                           Column('manager_code', String(6),
                                                  ForeignKey('doctor_model.staff_code'), primary_key=True),
                                           Column('joined_date', DateTime, primary_key=True),
                                           Column('leaved_date', DateTime)
                                           )