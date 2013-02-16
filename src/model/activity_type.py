from sqlalchemy import Column, String
from modules.database import Base
from modules.jsonable import Jsonable

# Stores allowed activity types. Use this to populate drop downs or something

@Jsonable('name')
class ActivityType(Base):
    __tablename__ = 'activity_types'

    name = Column(
        String(32),
        primary_key=True) # the name of the activity, Eg. Bike, Run

    def __init__(self, name):
    	self.name = name

    def __repr__(self):
    	return '<ActivityType %r>' % name
