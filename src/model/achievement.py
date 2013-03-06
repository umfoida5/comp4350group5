from sqlalchemy import Column, Table, ForeignKey, Integer, String, DateTime, Float
from sqlalchemy.orm import relationship, backref
from modules.database import Base
from modules.jsonable import Jsonable
from model.athlete import Athlete
from datetime import datetime

@Jsonable('achievement', 'unlocked_date')
class UnlockedAchievement(Base):
    __tablename__ = 'unlocked_achievements'

    id = Column(Integer, primary_key=True)
    athlete_id = Column(Integer, ForeignKey('athletes.id'), primary_key=True)
    achievement_id = Column(Integer, ForeignKey('achievements.id'), primary_key=True)
    unlocked_date = Column(DateTime, nullable=False, default=datetime.now())
    
    achievement = relationship("Achievement")
    athlete = relationship(
        Athlete, backref=backref(
            "unlocked_achievements",
            cascade="all, delete-orphan"
        )
    )

    def __init__(self, achievement):
        self.achievement = achievement

    def __repr__(self):
        return '<UnlockedAchievement %r %r %r>' % (
            self.athlete,
            self.achievement,
            self.unlocked_date
        )        

@Jsonable('title', 'description', 'image_url')
class Achievement(Base):
    __tablename__ = 'achievements'

    id = Column(Integer, primary_key=True)
    title = Column(String(128), unique=True, nullable=False)
    description = Column(String(500))
    image_url = Column(String(256), nullable=False)

    # TODO: make foreign keys to appropriate type tables
    activity = Column(String(32)) # Eg. run, bike
    operator = Column(String(32)) # Eg. average, total
    quantity = Column(Float) # quantity of metric
    metric = Column(String(32)) # Eg. km 
    start_date = Column(DateTime, default=datetime.now()) # start date of goal
    end_date = Column(DateTime, default=datetime.now()) # end date for goal (due date)    

    def __init__(
        self, 
        title, 
        description, 
        image_url,
        activity,
        operator, 
        quantity, 
        metric        
    ):
        self.title = title
        self.description = description
        self.image_url = image_url
        self.activity = activity
        self.operator = operator
        self.quantity = quantity
        self.metric = metric

    def __repr__(self):
        return '<Achievement %r %r %r>' % (
            self.title,
            self.description,
            self.image_url
        )
