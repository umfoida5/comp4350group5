#!/usr/bin/python

from modules import database
from model.athlete import Athlete
from model.achievement import Achievement
from model.activity import Activity
from model.event import Event
import datetime

database.init()
db_session = database.session

curr_time = datetime.datetime.now()

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

db_session.add(Activity(athletes[0].id, "Run", curr_time, 25, 50, 25))
db_session.add(Activity(athletes[1].id, "Walk", curr_time, 72, 40, 10))
db_session.add(Activity(athletes[2].id, "Bike", curr_time, 65, 70, 52))

db_session.commit()

db_session.add(Event(curr_time, "Join us at the Manitoba Marathon on Fathers Day.  More details at http://www.manitobamarathon.mb.ca/", "winnipeg", 2))
db_session.add(Event(curr_time, "Come join the run2!", "brandon", 3))
db_session.add(Event(curr_time, "Come join the run3!", "saskatoon", 10))

db_session.commit()

db_session.add(Achievement(
	"Newbie",
	"Congratulations, this is the very first time you are running!",
	"/images/achievements/newbie.jpeg"
))
db_session.add(Achievement(
	"Runner",
	"Yay! You have achieved the title of runner",
	"/images/achievements/runner.jpeg"
))
db_session.add(Achievement(
	"Crazy",
	"Yaaaahaaa, WOwhooo, beepee beepee",
	"/images/achievements/crazy.jpeg"
))
db_session.add(Achievement(
	"Local",
	"You must know all the locals by now - you are always running around!",
	"/images/achievements/local.jpeg"
))
db_session.add(Achievement(
	"Adventurer",
	"Using the same route everyday? That's not for you - congratulations, you have acquired the adventurer badge",
	"/images/achievements/crazy.jpeg"
))
db_session.commit()

athlete = Athlete.query.first()
achievement_objs = Achievement.query.all()

for i in achievement_objs:
	athlete.achievements.append(i)

db_session.commit()
