from sqlalchemy import Column, Integer, ForeignKey
from modules import database 
from modules.jsonable import Jsonable

@Jsonable('duration', 'distance')
class Activity(database.Base):
    __tablename__ = 'activities'

    id = Column(Integer, primary_key=True)
    athlete_id = Column(Integer, ForeignKey("athletes.id"), nullable=False)
    distance = Column(Integer)
    duration = Column(Integer)

    def __init__(self, athlete_id, distance, duration):
        self.athlete_id = athlete_id
        self.distance = distance
        self.duration = duration

    def __repr__(self):
        return '<Activity %r %r>' % (self.distance, self.duration)

