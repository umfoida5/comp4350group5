from sqlalchemy import Column, Integer, String, Date
from modules import database

#Athlete data model
class Athlete(database.Base):
    __tablename__ = 'athletes'
    id = Column(Integer, primary_key=True)
    first_name = Column(String(50))
    last_name = Column(String(50))
    email = Column(String(120))
    birth_date = Column(Date())
    about_me = Column(String(200))
    address = Column(String(200))
    avatar = Column(String(200))
    #height = Column(Integer)

	#initialise the Data model for the athlete
    def __init__(self, first_name, last_name, email, birth_date, about_me, address, avatar):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.birth_date = birth_date
        self.about_me = about_me
        self.address = address
        self.avatar = avatar

	
    def __repr__(self):
        return '<Athlete %r %r %r %r %r %r %r>' % (self.first_name, self.last_name, self.email, self.birth_date, self.about_me, self.address, self.avatar)

    #~ def getAthlete(aid):
        
