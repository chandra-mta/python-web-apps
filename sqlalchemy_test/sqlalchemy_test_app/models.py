from .extensions import db
from sqlalchemy import Column, String, Integer


class Score(db.Model):
    __tablename__ = 'scores'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    value = Column(Integer)