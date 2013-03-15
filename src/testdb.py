#!/usr/bin/python

from modules import database
from model.athlete import Athlete
from model.achievement import Achievement
from model.achievement import UnlockedAchievement
from model.activity import Activity
from model.event import Event
from model.health import Health
from model.goal import Goal
from datetime import datetime, timedelta
import datetime

database.init()
database.empty_database()
db_session = database.session

curr_time = datetime.datetime.now()

#Create Events
db_session.add(Event(curr_time, "Join us at the Manitoba Marathon on Fathers Day.  More details at http://www.manitobamarathon.mb.ca/", "winnipeg", 2))
db_session.add(Event(curr_time, "Come join one of the largest marathons in the world, the Boston marathon. Find out how to qualify at http://www.baa.org/races/boston-marathon.aspx", "boston", 3))
db_session.add(Event(curr_time, "Do not miss La Tour De France! Find out more details at http://www.letour.fr/paris-nice/2013/us", "paris", 10))

db_session.commit()

#Create Achivements
db_session.add(Achievement(
	"Newbie",
	"Congratulations, this is the very first time you are running!",
	"../img/achievements/unlocked_achievement2.jpeg",
	"Run",
	"total",
	"10",
	"distance"
))
db_session.add(Achievement(
	"Runner",
	"Yay! You have achieved the title of runner",
	"../img/achievements/unlocked_achievement4.jpeg",
	"Bike",
	"average",
	"100",
	"distance"
))
db_session.add(Achievement(
	"Crazy",
	"Yaaaahaaa, WOwhooo, beepee beepee",
	"../img/achievements/unlocked_achievement3.jpeg",
	"Run",
	"total",
	"100",
	"distance"
))
db_session.add(Achievement(
	"Local",
	"You must know all the locals by now - you are always running around!",
	"../img/achievements/unlocked_achievement5.jpeg",
	"Run",
	"total",
	"10",
	"distance"
))
db_session.add(Achievement(
	"Adventurer",
	"Walk through the same route everyday? That's not for you - congratulations, you have acquired the adventurer badge",
	"../img/achievements/unlocked_achievement6.jpeg",
	"Run",
	"total",
	"10",
	"distance"
))
db_session.add(Achievement(
	"Inspired",
	"You have been biking everyday since 1993! That deserves a celebrtion!",
	"../img/achievements/unlocked_achievement7.jpeg",
	"Run",
	"total",
	"10",
	"distance"
))
db_session.add(Achievement(
	"Forest Gump",
	"Run Forest, RUN!",
	"../img/achievements/unlocked_achievement8.jpeg",
	"Run",
	"total",
	"10",
	"distance"
))
db_session.add(Achievement(
	"Iron Maiden",
	"Run to the hiiiiiiiiiiillllsssssss, run for your liiiiiiiiiiives",
	"../img/achievements/unlocked_achievement9.jpeg",
	"Run",
	"total",
	"10",
	"distance"
))
db_session.add(Achievement(
	"Healthy",
	"Eat healthy, be healhy! <3",
	"../img/achievements/unlocked_achievement1.jpeg",
	"Run",
	"total",
	"10",
	"distance"
))
db_session.add(Achievement(
	"Inventor",
	"Be creative!",
	"../img/achievements/unlocked_achievement10.jpeg",
	"Run",
	"total",
	"10",
	"distance"
))
db_session.add(Achievement(
	"Lack of Imagination",
	"Congratulations! This makes it two!",
	"../img/achievements/unlocked_achievement11.jpeg",
	"Run",
	"total",
	"10",
	"distance"
))
db_session.add(Achievement(
	"Newbie2",
	"Congratulations, this is the very first time you are running!",
	"../img/achievements/unlocked_achievement2.jpeg",
	"Run",
	"total",
	"10",
	"distance"
))
db_session.add(Achievement(
	"Runner2",
	"Yay! You have achieved the title of runner",
	"../img/achievements/unlocked_achievement4.jpeg",
	"Run",
	"total",
	"10",
	"distance"
))
db_session.add(Achievement(
	"Crazy2",
	"Yaaaahaaa, WOwhooo, beepee beepee",
	"../img/achievements/unlocked_achievement3.jpeg",
	"Run",
	"total",
	"10",
	"distance"
))
db_session.add(Achievement(
	"Local2",
	"You must know all the locals by now - you are always running around!",
	"../img/achievements/unlocked_achievement5.jpeg",
	"Run",
	"total",
	"10",
	"distance"
))
db_session.add(Achievement(
	"Adventurer2",
	"Walk through the same route everyday? That's not for you - congratulations, you have acquired the adventurer badge",
	"../img/achievements/unlocked_achievement6.jpeg",
	"Run",
	"total",
	"10",
	"distance"
))
db_session.add(Achievement(
	"Inspired2",
	"You have been biking everyday since 1993! That deserves a celebrtion!",
	"../img/achievements/unlocked_achievement7.jpeg",
	"Run",
	"total",
	"10",
	"distance"
))
db_session.add(Achievement(
	"Forest Gump2",
	"Run Forest, RUN!",
	"../img/achievements/unlocked_achievement8.jpeg",
	"Run",
	"total",
	"10",
	"distance"
))
db_session.add(Achievement(
	"Iron Maiden2",
	"Run to the hiiiiiiiiiiillllsssssss, run for your liiiiiiiiiiives",
	"../img/achievements/unlocked_achievement9.jpeg",
	"Run",
	"total",
	"10",
	"distance"
))
db_session.add(Achievement(
	"Healthy2",
	"Eat healthy, be healhy! <3",
	"../img/achievements/unlocked_achievement1.jpeg",
	"Run",
	"total",
	"10",
	"distance"
))
db_session.add(Achievement(
	"Inventor2",
	"Be creative!",
	"../img/achievements/unlocked_achievement10.jpeg",
	"Run",
	"total",
	"10",
	"distance"
))
db_session.add(Achievement(
	"Lack of Imagination2",
	"Congratulations! This makes it two!",
	"../img/achievements/unlocked_achievement11.jpeg",
	"Run",
	"total",
	"10",
	"distance"
))
db_session.add(Achievement(
	"Inventor3",
	"Be creative!",
	"../img/achievements/unlocked_achievement10.jpeg",
	"Run",
	"total",
	"10",
	"distance"
))
db_session.add(Achievement(
	"Lack of Imagination3",
	"Congratulations! This makes it two!",
	"../img/achievements/unlocked_achievement11.jpeg",
	"Run",
	"total",
	"10",
	"distance"
))
db_session.commit()

#Create Athletes
db_session.add(Athlete("justin", "justin", "Justin", "Fdart", "awesome@cc.umanitoba.ca", "1980-11-23", "Here's where I'm supposed to tell you my lifestory.  But I won't.  Hit me up to play some DotA 2?", "123 Fake Street Winnipeg, MB", "/comp4350group4/src/view/web/profile/pic.png"))
db_session.add(Athlete("ben", "ben", "Ben", "Zeghers", "ben@email.com", "1980-11-24", "Here's where I'm supposed to tell you my lifestory.  But I won't.  Really. I like fishing though.", "321 Fake Street Winnipeg, MB", "/comp4350group4/src/view/web/profile/pic.png"))
db_session.add(Athlete("sammy", "sammy", "Sammy", "Creed", "sammy@email.com", "1980-11-23", "Here's where I'm supposed to tell you my lifestory.  But I won't.  Really.  I'm very good at solving problems and puzzles.", "123 Fake Street Winnipeg, MB", "/comp4350group4/src/view/web/profile/pic.png"))
db_session.add(Athlete("blake", "blake", "Blake", "Beatty", "blake@email.com", "1980-11-23", "Here's where I'm supposed to tell you my lifestory.  But I won't.  Really.  I'm a scary vikings fan.", "123 Fake Street Winnipeg, MB", "/comp4350group4/src/view/web/profile/pic.png"))
db_session.add(Athlete("phil", "phil", "Phil", "Latka", "phil@email.com", "1980-11-23", "Here's where I'm supposed to tell you my lifestory.  But I won't.  Really.  Those names, I remember them.", "123 Fake Street Winnipeg, MB", "/comp4350group4/src/view/web/profile/pic.png"))
db_session.add(Athlete("alex", "alex", "Alex", "Salomon", "alex@email.com", "1980-11-23", "Here's where I'm supposed to tell you my lifestory.  But I won't.  Really.  I make some unreal food.", "123 Fake Street Winnipeg, MB", "/comp4350group4/src/view/web/profile/pic.png"))
db_session.add(Athlete("andrew", "andrew", "Andrew", "Konkin", "andrew@email.com", "1980-11-23", "Here's where I'm supposed to tell you my lifestory.  But I won't.  Really.  I put up with these other 6 idiots in the group, that's a strong character trait.", "123 Fake Street Winnipeg, MB", "/comp4350group4/src/view/web/profile/pic.png"))
db_session.commit()

#####################################################################
#																	#
# For each Athlete, we now go and add data such as which achivements#
# are unlocked, activies, goals and health records.					#
#																	#
#####################################################################

athletes = Athlete.query.all()

for athlete in athletes:
	athleteID = athlete.id

	#Create Activities
	db_session.add(Activity(athleteID, "Run", curr_time, 10, 50, 25))
	db_session.add(Activity(athleteID, "Run", curr_time+timedelta(days=2), 12, 60, 25))
	db_session.add(Activity(athleteID, "Walk", curr_time+timedelta(days=4), 3, 40, 10))
	db_session.add(Activity(athleteID, "Walk", curr_time+timedelta(days=6), 4, 52, 10))
	db_session.add(Activity(athleteID, "Bike", curr_time+timedelta(days=8), 30, 60, 52))
	db_session.add(Activity(athleteID, "Bike", curr_time+timedelta(days=12), 35, 60, 55))

	db_session.add(Activity(athleteID, "Run", curr_time+timedelta(days=14), 10, 50, 25))
	db_session.add(Activity(athleteID, "Run", curr_time+timedelta(days=16), 12, 60, 25))
	db_session.add(Activity(athleteID, "Walk", curr_time+timedelta(days=18), 3, 40, 10))
	db_session.add(Activity(athleteID, "Walk", curr_time+timedelta(days=20), 4, 52, 10))
	db_session.add(Activity(athleteID, "Bike", curr_time+timedelta(days=22), 30, 60, 52))
	db_session.add(Activity(athleteID, "Bike", curr_time+timedelta(days=24), 35, 60, 55))

	db_session.add(Activity(athleteID, "Run", curr_time+timedelta(days=26), 10, 50, 25))
	db_session.add(Activity(athleteID, "Run", curr_time+timedelta(days=28), 12, 60, 25))
	db_session.add(Activity(athleteID, "Walk", curr_time+timedelta(days=30), 3, 40, 10))
	db_session.add(Activity(athleteID, "Walk", curr_time+timedelta(days=32), 4, 52, 10))
	db_session.add(Activity(athleteID, "Bike", curr_time+timedelta(days=34), 30, 60, 52))
	db_session.add(Activity(athleteID, "Bike", curr_time+timedelta(days=36), 35, 60, 55))

	db_session.commit()

	#Unlock some activities
	achievementList = Achievement.query.all()

	for j in range(0, 9):
		athlete.achievements.append(achievementList[j])

	db_session.commit()

	#Create Goals
	db_session.add(Goal(
		athleteID,
		"Run",
		"total",
		"500",
		"km",
		curr_time,
		curr_time + timedelta(days=10)
	))

	db_session.add(Goal(
		athleteID,
		"Bike",
		"total",
		"1000",
		"km",
		curr_time + timedelta(days=11),
		curr_time + timedelta(days=21)
	))

	db_session.add(Goal(
		athleteID,
		"Walk",
		"total",
		"100",
		"km",
		curr_time + timedelta(days=25),
		curr_time + timedelta(days=50)
	))

	db_session.commit()

	#Create Health Records
	db_session.add(Health(
		athleteID,
		curr_time,
		185,
		73,
		"Here we go! First log!"
	))

	db_session.add(Health(
		athleteID,
		curr_time + timedelta(days=1),
		185,
		73,
		"Day 2, nothing yet."
	))

	db_session.add(Health(
		athleteID,
		curr_time + timedelta(days=2),
		185,
		73,
		"Day 3, nothing yet."
	))

	db_session.add(Health(
		athleteID,
		curr_time + timedelta(days=3),
		185,
		73,
		"Day 4, nothing yet."
	))

	db_session.add(Health(
		athleteID,
		curr_time + timedelta(days=4),
		184,
		73,
		"Day 5, first pound gone!"
	))

	db_session.add(Health(
		athleteID,
		curr_time + timedelta(days=5),
		184,
		72,
		""
	))

	db_session.add(Health(
		athleteID,
		curr_time + timedelta(days=6),
		187,
		74,
		"Day 6, shouldn't have eaten 7 McDoubles FML!"
	))

	db_session.add(Health(
		athleteID,
		curr_time + timedelta(days=16),
		180,
		72,
		"Day 16, ROCKING IT!"
	))

	db_session.add(Health(
		athleteID,
		curr_time + timedelta(days=26),
		177,
		74,
		"Day 26, I'm too sexy for my shirt!"
	))

	db_session.add(Health(
		athleteID,
		curr_time + timedelta(days=36),
		175,
		74,
		""
	))

	db_session.add(Health(
		athleteID,
		curr_time + timedelta(days=41),
		173,
		74,
		""
	))

	db_session.add(Health(
		athleteID,
		curr_time + timedelta(days=45),
		170,
		74,
		""
	))

	db_session.add(Health(
		athleteID,
		curr_time + timedelta(days=80),
		190,
		74,
		"Those double cheese"
	))
	db_session.commit()
