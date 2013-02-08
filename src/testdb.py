#!/usr/bin/python

from modules.database import init_db, db_session
from model.athlete import Athlete
from model.activity import Activity

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
