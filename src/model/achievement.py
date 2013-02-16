from sqlalchemy import Column, Table, ForeignKey, Integer, String, DateTime
from modules.database import Base
from modules.jsonable import Jsonable
from datetime import datetime

AthleteAchievements = Table(
    'athlete_achievements', 
    Base.metadata,
    Column('athlete_id', Integer, ForeignKey('athletes.id')),
    Column('achievement_id', Integer, ForeignKey('achievements.id'))
)

@Jsonable('title', 'description', 'image_url')
class Achievement(Base):
    __tablename__ = 'achievements'

    id = Column(Integer, primary_key=True)
    title = Column(String(128), nullable=False)
    description = Column(String(500))
    creation_date = Column(DateTime, default=datetime.now())
    image_url = Column(String(256))

    def __init__(self, title, description, image_url):
        self.title = title
        self.description = description
        self.image_url = image_url

    def __repr__(self):
        return '<Achievement %r %r %r %r>' % (
            self.title,
            self.description,
            self.creation_date,
            self.image_url
        )
