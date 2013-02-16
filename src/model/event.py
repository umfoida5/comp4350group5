from sqlalchemy import Column, Integer, String, Date
from modules import database
from modules.jsonable import Jsonable

@Jsonable('event_date', 'description', 'location', 'distance')
class Event(database.Base):
    __tablename__ = 'events'

    id = Column(Integer, primary_key=True)
    event_date = Column(Date())
    description = Column(String(1000))
    location = Column(String(200))
    distance = Column(Integer)

    def __init__(self, event_date, description, location, distance):
        self.event_date = event_date
        self.description = description
        self.location = location
        self.distance = distance

    def __repr__(self):
        return '<Event %r %r %r %r>' % (
            self.event_date,
            self.description,
            self.location,
            self.distance
        )

