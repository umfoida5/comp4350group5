from sqlalchemy import Column, Integer, String, Date, ForeignKey
from modules import database
from modules.jsonable import Jsonable

@Jsonable('health_date', 'weight', 'resting_heart_rate', 'comments')
class Health(database.Base):
    __tablename__ = 'health'

    id                 = Column(Integer, primary_key=True)
    athlete_id         = Column(Integer, ForeignKey("athletes.id"), nullable=False)
    health_date        = Column(Date(), nullable=False)
    weight             = Column(Integer)
    resting_heart_rate = Column(Integer)
    comments           = Column(String(200))

    def __init__(self, athlete_id, health_date, weight, resting_heart_rate, comments):
        self.athlete_id = athlete_id
        self.health_date = health_date
        self.weight = weight
        self.resting_heart_rate = resting_heart_rate
        self.comments = comments

    def __repr__(self):
        return '<Health Record %r %r %r %r>' % (
        self.health_date,
        self.weight,
        self.resting_heart_rate,
        self.comments
        )

