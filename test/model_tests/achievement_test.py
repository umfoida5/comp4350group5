import unittest
from modules import database
from model.achievement import Achievement
from model.athlete import Athlete

class AchievementTests(unittest.TestCase):	

	@classmethod
	def setUpClass(cls):
		database.init("tracker_test")

	def setUp(self):
		database.empty_database()

	def test_achievement_object_creation(self):
		achievement1 = Achievement("Title1", "desc1", "/images/a1.jpeg")
		achievement2 = Achievement("Title2", "desc2", "/images/a2.jpeg")
		achievement3 = Achievement("Title3", "desc3", "/images/a3.jpeg")
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

		self.assertIsNotNone(queried_achivement1)
		self.assertIsNotNone(queried_achivement2)
		self.assertIsNotNone(queried_achivement3)

		self.assertEqual(queried_achivement1, achievement1)
		self.assertEqual(queried_achivement2, achievement2)
		self.assertEqual(queried_achivement3, achievement3)

		self.assertTrue(len(Achievement.query.all()) == 3)

	def test_athlete_and_achievement_association(self):
		achievement1 = Achievement("Title1", "desc1", "/images/a1.jpeg")
		achievement2 = Achievement("Title2", "desc2", "/images/a2.jpeg")
		achievement3 = Achievement("Title3", "desc3", "/images/a3.jpeg")	
		athlete1 = Athlete(
			"Joe",
			"Smith",
			"email@email.com",
			"1980-11-23",
			"desc1",
			"addr",
			"/pic.png"
		)	
		athlete2 = Athlete(
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

		self.assertIn(achievement1, athlete1.achievements)
		self.assertIn(achievement2, athlete1.achievements)
		self.assertNotIn(achievement3, athlete1.achievements)

		self.assertNotIn(achievement1, athlete2.achievements)
		self.assertNotIn(achievement2, athlete2.achievements)
		self.assertNotIn(achievement3, athlete2.achievements)		

if(__name__ == '__main__'):
	unittest.main()

