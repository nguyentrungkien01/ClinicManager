from sqlalchemy import Column, Integer, String

from ClinicManagerApp import db


class RuleModel(db.Model):
    __tablename__='rule_model'

    # attribute
    rule_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), unique=True, nullable=False, default='')
    amount = Column(Integer, default=0)

    def __str__(self):
        return self.name
