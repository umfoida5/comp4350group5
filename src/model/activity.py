from sqlalchemy import Column, Integer, String, Date, ForeignKey
from modules.database import Base

class Activity(Base):
    __tablename__ = 'activities'
    id = Column(Integer, primary_key=True)
    athlete_id = Column(Integer, ForeignKey("athletes.id"), nullable=False)
    distance = Column(Integer)
    duration = Column(Integer)
    #birth_date = Column(Date())
    #about_me = Column(String(200))
    #location = Column(String(200))
    #height = Column(Integer)

    def __init__(self, distance, duration):
        self.distance = distance
        self.duration = duration

    def __repr__(self):
        return '<Activity %r %r>' % (self.distance, self.duration)

