from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import relationship
from modules.database import Base
from achievement import AthleteAchievements

class Athlete(Base):
    __tablename__ = 'athletes'

    id = Column(Integer, primary_key=True)
    first_name = Column(String(50))
    last_name = Column(String(50))
    achievements = relationship("Achievement",
                    secondary=AthleteAchievements)    

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def __repr__(self):
        return '<Athlete %r %r %r>' % (
            self.first_name,
            self.last_name,
            self.achievements
        )
