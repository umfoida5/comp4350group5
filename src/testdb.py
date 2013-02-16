#!/usr/bin/python

from modules import database
from model.athlete import Athlete
from model.activity import Activity
from model.event import Event
import datetime

database.init()
db_session = database.session

db_session.add(Athlete("Joe", "Smith", "email@email.com", "1980-11-23", "All work and no play makes Joe a dull boy", "123 Fake Street Winnipeg, MB", "/comp4350group4/src/view/web/profile/pic.png"))
db_session.add(Athlete("Bob", "Brown", "email@email.com", "1980-11-23", "All work and no play makes Joe a dull boy", "123 Fake Street Winnipeg, MB", "/comp4350group4/src/view/web/profile/pic.png"))
db_session.add(Athlete("Frank", "Reese", "email@email.com", "1980-11-23", "All work and no play makes Joe a dull boy", "123 Fake Street Winnipeg, MB", "/comp4350group4/src/view/web/profile/pic.png"))
db_session.add(Athlete("Joe", "Smith", "email@email.com", "1980-11-23", "All work and no play makes Joe a dull boy", "123 Fake Street Winnipeg, MB", "/comp4350group4/src/view/web/profile/pic.png"))
db_session.add(Athlete("Bob", "Brown", "email@email.com", "1980-11-23", "All work and no play makes Joe a dull boy", "123 Fake Street Winnipeg, MB", "/comp4350group4/src/view/web/profile/pic.png"))
db_session.add(Athlete("Frank", "Reese", "email@email.com", "1980-11-23", "All work and no play makes Joe a dull boy", "123 Fake Street Winnipeg, MB", "/comp4350group4/src/view/web/profile/pic.png"))
db_session.add(Athlete("Joe", "Smith", "email@email.com", "1980-11-23", "All work and no play makes Joe a dull boy", "123 Fake Street Winnipeg, MB", "/comp4350group4/src/view/web/profile/pic.png"))
db_session.add(Athlete("Bob", "Brown", "email@email.com", "1980-11-23", "All work and no play makes Joe a dull boy", "123 Fake Street Winnipeg, MB", "/comp4350group4/src/view/web/profile/pic.png"))
db_session.add(Athlete("Frank", "Reese", "email@email.com", "1980-11-23", "All work and no play makes Joe a dull boy", "123 Fake Street Winnipeg, MB", "/comp4350group4/src/view/web/profile/pic.png"))
db_session.add(Athlete("Joe", "Smith", "email@email.com", "1980-11-23", "All work and no play makes Joe a dull boy", "123 Fake Street Winnipeg, MB", "/comp4350group4/src/view/web/profile/pic.png"))
db_session.add(Athlete("Bob", "Brown", "email@email.com", "1980-11-23", "All work and no play makes Joe a dull boy", "123 Fake Street Winnipeg, MB", "/comp4350group4/src/view/web/profile/pic.png"))
db_session.add(Athlete("Frank", "Reese", "email@email.com", "1980-11-23", "All work and no play makes Joe a dull boy", "123 Fake Street Winnipeg, MB", "/comp4350group4/src/view/web/profile/pic.png"))

db_session.commit()

athletes = Athlete.query.all()

db_session.add(Activity(athletes[0].id, 25, 50))
db_session.add(Activity(athletes[1].id, 72, 40))
db_session.add(Activity(athletes[2].id, 65, 70))

db_session.commit()

curr_time = datetime.datetime.now()

db_session.add(Event(curr_time, "Join us at the Manitoba Marathon on Fathers Day.  More details at http://www.manitobamarathon.mb.ca/", "winnipeg", 2))
db_session.add(Event(curr_time, "Come join the run2!", "brandon", 3))
db_session.add(Event(curr_time, "Come join the run3!", "saskatoon", 10))

db_session.commit()
