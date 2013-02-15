from sqlalchemy import Column, Integer, String, Date
from modules import database

class Athlete(database.Base):
    __tablename__ = 'athletes'
    id = Column(Integer, primary_key=True)
    first_name = Column(String(50))
    last_name = Column(String(50))
    #~ email = Column(String(120))
    #birth_date = Column(Date())
    #about_me = Column(String(200))
    #location = Column(String(200))
    #height = Column(Integer)

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def __repr__(self):
        return '<Athlete %r %r >' % (self.first_name, self.last_name)

    #~ def getAthlete(aid):
        
