#!/usr/bin/python

from modules.database import init_db, db_session
from model.athlete import Athlete
from model.activity import Activity
from model.event import Event
import datetime

init_db()

db_session.add(Athlete("Joe", "Smith"))
db_session.add(Athlete("Bob", "Brown"))
db_session.add(Athlete("Frank", "Reese"))
db_session.add(Athlete("Joe", "Smith"))
db_session.add(Athlete("Bob", "Brown"))
db_session.add(Athlete("Frank", "Reese"))
db_session.add(Athlete("Joe", "Smith"))
db_session.add(Athlete("Bob", "Brown"))
db_session.add(Athlete("Frank", "Reese"))
db_session.add(Athlete("Joe", "Smith"))
db_session.add(Athlete("Bob", "Brown"))
db_session.add(Athlete("Frank", "Reese"))

db_session.commit()

athletes = Athlete.query.all()

db_session.add(Activity(athletes[0].id, 25, 50))
db_session.add(Activity(athletes[1].id, 72, 40))
db_session.add(Activity(athletes[2].id, 65, 70))

db_session.commit()

curr_time = datetime.datetime.now()

db_session.add(Event(curr_time, "Join us at the Manitoba Marathon on Fathers Day.  More details at http://www.manitobamarathon.mb.ca/", "Winnipeg", 2))
db_session.add(Event(curr_time, "Come join the run2!", "Brandon", 3))
db_session.add(Event(curr_time, "Come join the run3!", "Saskatoon", 10))

db_session.commit()
