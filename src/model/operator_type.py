from sqlalchemy import Column, String
from modules.database import Base
from modules.jsonable import Jsonable

# Stores allowed operator types. Stuff like max, min, average. Stats and other stuff

@Jsonable('name')
class OperatorType(Base):
    __tablename__ = 'operator_types'

    name = Column(
        String(32), 
        primary_key=True) # the name of the operator, Eg. max, min, avaerage. Must be SQL operator

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<OperatorType %r>' % name
