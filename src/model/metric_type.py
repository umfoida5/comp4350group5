from sqlalchemy import Column, String
from modules.database import Base
from modules.jsonable import Jsonable

# Stores allowed metric types. useful for stats and data filtering

@Jsonable('name')
class MetricType(Base):
    __tablename__ = 'metric_types'

    name = Column(
        String(32),
        primary_key=True) # the name of the metric, Eg. km, km/hr

    def __init__(self, name):
    	self.name = name

    def __repr__(self):
    	return '<MetricType %r>' % name
