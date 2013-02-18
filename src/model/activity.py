from sqlalchemy import Column, Integer, ForeignKey, String, Date
from modules import database 
from modules.jsonable import Jsonable

@Jsonable('type', 'date', 'duration', 'distance', 'max_speed')
class Activity(database.Base):
    __tablename__ = 'activities'

    id = Column(Integer, primary_key=True)
    athlete_id = Column(Integer, ForeignKey("athletes.id"), nullable=False)
    type = Column(String(100))
    date = Column(Date())
    distance = Column(Integer)
    duration = Column(Integer)
    max_speed = Column(Integer)

    def __init__(self, athlete_id, type, date, distance, duration, max_speed):
        self.athlete_id = athlete_id
        self.type = type
        self.date = date
        self.distance = distance
        self.duration = duration
        self.max_speed = max_speed

    def __repr__(self):
        return '<Activity %r %r>' % (self.distance, self.duration)

