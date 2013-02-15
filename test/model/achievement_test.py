import unittest
import sys

sys.path.append('../../src')
from modules.database import init_db, db_session
from model.achievement import Achievement

class AchievementTests(unittest.TestCase):	
	
	def test_cretion(self):
		achievement1 = Achievement("Title1", "desc1", "/images/a1.jpeg")
		achievement2 = Achievement("Title2", "desc2", "/images/a2.jpeg")
		achievement2 = Achievement("Title3", "desc3", "/images/a3.jpeg")
		db_session.commit()

		self.assertTrue(
			Achievement.query.filter_by(title = "Title1").first() != None
		)
		self.assertTrue(
			Achievement.query.filter_by(title = "Title2").first() != None
		)
		self.assertTrue(
			Achievement.query.filter_by(title = "Title3").first() != None
		)

if(__name__ == '__main__'):
	unittest.main()

