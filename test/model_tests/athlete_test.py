import unittest
from datetime import datetime
from modules import database
from model.athlete import Athlete

class AthleteTests(unittest.TestCase):	

	@classmethod
	def setUpClass(cls):
		database.init("tracker_test")

	def setUp(self):
		database.empty_database()

	def test_athlete_object_creation(self):
		athlete1 = Athlete("name1", "lastname1", "a@a.a.a", datetime.now())
		athlete2 = Athlete("name2", "lastname2", "a@a.a.a", datetime.now())
		athlete3 = Athlete("name3", "lastname3", "a@a.a.a", datetime.now())
		database.session.add(athlete1)
		database.session.add(athlete2)
		database.session.add(athlete3)
		database.session.commit()

		queried_athlete1 = Athlete.query.filter_by(first_name = "name1").first()
		queried_athlete2 = Athlete.query.filter_by(first_name = "name2").first()
		queried_athlete3 = Athlete.query.filter_by(first_name = "name3").first()

		self.assertIsNotNone(queried_athlete1)
		self.assertIsNotNone(queried_athlete2)
		self.assertIsNotNone(queried_athlete3)

		self.assertEqual(queried_athlete1, athlete1)
		self.assertEqual(queried_athlete2, athlete2)
		self.assertEqual(queried_athlete3, athlete3)

		self.assertTrue(len(Athlete.query.all()) == 3)

if(__name__ == '__main__'):
	unittest.main()

