import unittest
from modules import database
from model.achievement import Achievement

class AchievementTests(unittest.TestCase):	

	@unittest.skip("Partially implemented")
	def test_achievement_object_creation(self):
		achievement1 = Achievement("Title1", "desc1", "/images/a1.jpeg")
		achievement2 = Achievement("Title2", "desc2", "/images/a2.jpeg")
		achievement2 = Achievement("Title3", "desc3", "/images/a3.jpeg")
		database.session.commit()

		self.assertTrue(
			Achievement.query.filter_by(title = "Title1").first() != None
		)
		self.assertTrue(
			Achievement.query.filter_by(title = "Title2").first() != None
		)
		self.assertTrue(
			Achievement.query.filter_by(title = "Title3").first() != None
		)

	@unittest.skip("Not implemented")
	def test_athlete_and_achievement_association(self):
		self.fail("Not implemented")   

if(__name__ == '__main__'):
	unittest.main()

