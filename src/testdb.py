#!/usr/bin/python

from modules.database import init_db, db_session
from model.athlete import Athlete

init_db()

db_session.add(Athlete("Joe", "Smith"))
db_session.add(Athlete("Bob", "Brown"))
db_session.add(Athlete("Frank", "Reese"))

db_session.commit()
