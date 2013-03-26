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
db_session.add(Event(curr_time, "Come join us for the MSWalk. It is a great cause and a lot of fun! More details at http://mssoc.convio.net/site/TR?fr_id=1996&pg=entry&s_locale=en_ca", "winnipeg", 15))
db_session.add(Event(curr_time, "Come join us for the MSWalk. It is a great cause and a lot of fun! More details at http://mssoc.convio.net/site/TR?fr_id=2158&pg=entry&s_locale=en_ca", "flin flon", 15))
db_session.add(Event(curr_time, "Come join us for the MSWalk. It is a great cause and a lot of fun! More details at http://mssoc.convio.net/site/TR?fr_id=2150&pg=entry&s_locale=en_ca", "lac du bonet", 15))
db_session.add(Event(curr_time, "Come join us for the MSWalk. It is a great cause and a lot of fun! More details at http://mssoc.convio.net/site/TR?fr_id=2152&pg=entry&s_locale=en_ca", "morden", 15))
db_session.add(Event(curr_time, "Come join us for the MSWalk. It is a great cause and a lot of fun! More details at http://mssoc.convio.net/site/TR?fr_id=2156&pg=entry&s_locale=en_ca", "parkland", 15))
db_session.add(Event(curr_time, "Come join us for the MSWalk. It is a great cause and a lot of fun! More details at http://mssoc.convio.net/site/TR?fr_id=2151&pg=entry&s_locale=en_ca", "portage la prairie", 15))
db_session.add(Event(curr_time, "Come join us for the MSWalk. It is a great cause and a lot of fun! More details at http://mssoc.convio.net/site/TR?fr_id=2154&pg=entry&s_locale=en_ca", "steinbach", 15))
db_session.add(Event(curr_time, "Come join us for the MSWalk. It is a great cause and a lot of fun! More details at http://mssoc.convio.net/site/TR?fr_id=2157&pg=entry&s_locale=en_ca", "the pas", 15))
db_session.add(Event(curr_time, "Come join us for the MSWalk. It is a great cause and a lot of fun! More details at http://mssoc.convio.net/site/TR?fr_id=2155&pg=entry&s_locale=en_ca", "thompson", 15))
db_session.add(Event(curr_time, "Come join us for the MSWalk. It is a great cause and a lot of fun! More details at http://mssoc.convio.net/site/TR?fr_id=2153&pg=entry&s_locale=en_ca", "westman", 15))

db_session.commit()

#Create Achivements

# Running
db_session.add(Achievement(
	"Couch to 5K",
	"Nice work! (run 5 km in one workout)",
	"../img/achievements/unlocked_achievement1.jpeg",
	"Run",
	"max",
	"5",
	"distance"
))
db_session.add(Achievement(
	"Runner",
	"Yay! You sure are going places! (run 50 km total)",
	"../img/achievements/unlocked_achievement6.jpeg",
	"Run",
	"total",
	"10",
	"distance"
))
db_session.add(Achievement(
	"Marathoner",
	"Wow, you are amazing! (run 42 km in one workout)",
	"../img/achievements/unlocked_achievement1.jpeg",
	"Run",
	"max",
	"42",
	"distance"
))
db_session.add(Achievement(
	"Ultra-Runner",
	"\"To give anything less than the best is to sacrifice the gift.\" (run 250 km total)",
	"../img/achievements/unlocked_achievement6.jpeg",
	"Run",
	"total",
	"250",
	"distance"
))
db_session.add(Achievement(
	"Forrest Gump",
	"Run, Forrest, Run!! (run 1000 km total)",
	"../img/achievements/unlocked_achievement10.jpeg",
	"Run",
	"total",
	"1000",
	"distance"
))
db_session.add(Achievement(
	"Keep that Pace",
	"Steady as she goes! (run an average top speed of 10 km/hr)",
	"../img/achievements/unlocked_achievement2.jpeg",
	"Run",
	"average",
	"10",
	"max_speed"
))
db_session.add(Achievement(
	"You're Crazy!",
	"Are you up for the challenge? (run for over 4 hours in one workout)",
	"../img/achievements/unlocked_achievement5.jpeg",
	"Run",
	"max",
	"240",
	"duration"
))

# Bike
db_session.add(Achievement(
	"Training Wheels",
	"Nice work! (bike 10 km total)",
	"../img/achievements/unlocked_achievement1.jpeg",
	"Bike",
	"total",
	"5",
	"distance"
))
db_session.add(Achievement(
	"Bicycling 101",
	"Good consistency! (bike 101 km total)",
	"../img/achievements/unlocked_achievement12.jpeg",
	"Bike",
	"total",
	"101",
	"distance"
))
db_session.add(Achievement(
	"Iron Maiden",
	"Run to the hiiiiiiiiiiillllsssssss, run for your liiiiiiiiiiives! (bike 80 km in one workout)",
	"../img/achievements/unlocked_achievement12.jpeg",
	"Bike",
	"max",
	"80",
	"distance"
))
db_session.add(Achievement(
	"Super Biker",
	"Wow, your legs must be sore! (bike 1000 km total)",
	"../img/achievements/unlocked_achievement10.jpeg",
	"Bike",
	"total",
	"1000",
	"distance"
))
db_session.add(Achievement(
	"Speed Demon",
	"What a blur! (bike an average top speed of 20 km/hr)",
	"../img/achievements/unlocked_achievement2.jpeg",
	"Bike",
	"average",
	"20",
	"max_speed"
))
db_session.add(Achievement(
	"The Flash",
	"WHOA! (bike a top speed of 50 km/hr in one workout)",
	"../img/achievements/unlocked_achievement5.jpeg",
	"Bike",
	"max",
	"50",
	"max_speed"
))


# Swim 
db_session.add(Achievement(
	"Take a Dip",
	"The water is so refreshing! (swim 1 km total)",
	"../img/achievements/unlocked_achievement1.jpeg",
	"Swim",
	"total",
	"1",
	"distance"
))
db_session.add(Achievement(
	"Swimmer",
	"Swimming is fun! (swim 20 km total)",
	"../img/achievements/unlocked_achievement13.jpeg",
	"Swim",
	"total",
	"1",
	"distance"
))
db_session.add(Achievement(
	"Under the Sea",
	"Where eveything is better! (swim 100 km total)",
	"../img/achievements/unlocked_achievement13.jpeg",
	"Swim",
	"total",
	"1",
	"distance"
))
db_session.add(Achievement(
	"Like a Fish",
	"Zoom zoom! (swim at an average 3 km/hr top speed)",
	"../img/achievements/unlocked_achievement11.jpeg",
	"Swim",
	"average",
	"3",
	"max_speed"
))
db_session.add(Achievement(
	"Treading Water",
	"Such endurance! (swim for over an hour in a workout)",
	"../img/achievements/unlocked_achievement2.jpeg",
	"Swim",
	"max",
	"60",
	"duration"
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
db_session.add(Athlete("cszapp", "cszapp", "Michael", "Zapp", "fakeemail@email.com", "1980-11-23", "Computer Science professor at the University of Manitoba.", "123 Fake Street Winnipeg, MB", "/comp4350group4/src/view/web/profile/pic.png"))
db_session.add(Athlete("frank", "frank", "frank", "frank", "frank@frank.frank", "1999,01,01", "I am frank.", "123 Frank Street Winnipeg MB", "/comp4350group4/src/view/web/profile/pic.png"))
db_session.add(Athlete("ios_unit_test", "ios_unit_test", "ios", "unit_test", "ios@apple.com", "1980-11-23", "IOS!!", "1 Infinite Loop Cupertino, CA", "/comp4350group4/src/view/web/profile/pic.png"))
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
	db_session.add(Activity(athleteID, "Run", curr_time, 50, 50, 25))
	db_session.add(Activity(athleteID, "Run", curr_time-timedelta(days=2), 20, 60, 25))
	db_session.add(Activity(athleteID, "Swim", curr_time-timedelta(days=4), 3, 40, 10))
	db_session.add(Activity(athleteID, "Swim", curr_time-timedelta(days=6), 4, 52, 10))
	db_session.add(Activity(athleteID, "Bike", curr_time-timedelta(days=8), 30, 60, 52))
	db_session.add(Activity(athleteID, "Bike", curr_time-timedelta(days=12), 35, 60, 55))

	db_session.add(Activity(athleteID, "Run", curr_time-timedelta(days=14), 5, 50, 25))
	db_session.add(Activity(athleteID, "Run", curr_time-timedelta(days=16), 25, 60, 25))
	db_session.add(Activity(athleteID, "Swim", curr_time-timedelta(days=18), 3, 40, 10))
	db_session.add(Activity(athleteID, "Swim", curr_time-timedelta(days=20), 4, 52, 10))
	db_session.add(Activity(athleteID, "Bike", curr_time-timedelta(days=22), 30, 60, 52))
	db_session.add(Activity(athleteID, "Bike", curr_time-timedelta(days=24), 35, 60, 55))

	db_session.add(Activity(athleteID, "Run", curr_time-timedelta(days=26), 10, 50, 25))
	db_session.add(Activity(athleteID, "Run", curr_time-timedelta(days=28), 12, 60, 25))
	db_session.add(Activity(athleteID, "Swim", curr_time-timedelta(days=30), 3, 40, 10))
	db_session.add(Activity(athleteID, "Swim", curr_time-timedelta(days=32), 4, 52, 10))
	db_session.add(Activity(athleteID, "Bike", curr_time-timedelta(days=34), 30, 60, 52))
	db_session.add(Activity(athleteID, "Bike", curr_time-timedelta(days=36), 35, 60, 55))

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
		"10000",
		"distance",
		curr_time - timedelta(days=5),
		curr_time + timedelta(days=10)
	))

	db_session.add(Goal(
		athleteID,
		"Bike",
		"total",
		"1000",
		"distance",
		curr_time + timedelta(days=11),
		curr_time + timedelta(days=21)
	))

	db_session.add(Goal(
		athleteID,
		"Swim",
		"total",
		"100",
		"distance",
		curr_time + timedelta(days=25),
		curr_time + timedelta(days=50)
	))

	db_session.commit()

	#Create Health Records
	db_session.add(Health(
		athleteID,
		curr_time - timedelta(days=1),
		300,
		100,
		"Here we go! First log!"
	))

	db_session.add(Health(
		athleteID,
		curr_time,
		130,
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
