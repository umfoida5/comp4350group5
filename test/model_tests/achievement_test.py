import unittest
from modules import database
from model.achievement import Achievement
from model.athlete import Athlete

class AchievementTests(unittest.TestCase):	

	def setUp(self):
		database.empty_database()

	def test_achievement_object_creation(self):
		achievement1 = Achievement("Title1", "desc1", "/images/a1.jpeg", "run", "average", 100, "distance")
		achievement2 = Achievement("Title2", "desc2", "/images/a2.jpeg", "bike", "total", 200, "duration")
		achievement3 = Achievement("Title3", "desc3", "/images/a3.jpeg", "walk", "average", 300, "duration")
		database.session.add(achievement1)
		database.session.add(achievement2)
		database.session.add(achievement3)
		database.session.commit()

		queried_achivement1 = Achievement.query.filter_by(
			title = "Title1"
		).first()
		queried_achivement2 = Achievement.query.filter_by(
			title = "Title2"
		).first()
		queried_achivement3 = Achievement.query.filter_by(
			title = "Title3"
		).first()

		self.assertTrue(queried_achivement1 is not None)
		self.assertTrue(queried_achivement2 is not None)
		self.assertTrue(queried_achivement3 is not None)

		self.assertEqual(queried_achivement1, achievement1)
		self.assertEqual(queried_achivement2, achievement2)
		self.assertEqual(queried_achivement3, achievement3)

		self.assertTrue(len(Achievement.query.all()) == 3)

	def test_athlete_and_achievement_association(self):
		achievement1 = Achievement("Title1", "desc1", "/images/a1.jpeg", "run", "average", 100, "distance")
		achievement2 = Achievement("Title2", "desc2", "/images/a2.jpeg", "bike", "total", 200, "duration")
		achievement3 = Achievement("Title3", "desc3", "/images/a3.jpeg", "walk", "average", 300, "duration")
		athlete1 = Athlete(
                        "joe1",
                        "password",
			"Joe",
			"Smith",
			"email@email.com",
			"1980-11-23",
			"desc1",
			"addr",
			"/pic.png"
		)	
		athlete2 = Athlete(
                        "joe2",
                        "password",
			"Joe",
			"Smith",
			"email@email.com",
			"1980-11-23",
			"desc1",
			"addr",
			"/pic.png"
		)	
		database.session.add(achievement1)
		database.session.add(achievement2)
		database.session.add(achievement3)
		database.session.add(athlete1)
		database.session.add(athlete2)
		database.session.flush()

		athlete1.achievements.append(achievement1)
		athlete1.achievements.append(achievement2)

		database.session.commit()

		self.assertTrue(achievement1 in athlete1.achievements)
		self.assertTrue(achievement2 in athlete1.achievements)
		self.assertFalse(achievement3 in athlete1.achievements)

		self.assertFalse(achievement1 in athlete2.achievements)
		self.assertFalse(achievement2 in athlete2.achievements)
		self.assertFalse(achievement3 in athlete2.achievements)		


