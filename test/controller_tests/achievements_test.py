import unittest, datetime
from modules import database
from controller.achievements import Achievements
from model.achievement import Achievement
from model.athlete import Athlete

class AchievementsTest(unittest.TestCase):
	ach_controller = Achievements()

	@classmethod
	def setUpClass(cls):
		database.init("tracker_test")

	def setUp(self):
		database.empty_database()

	def populate_database_with_test_data(self):
		achievement1 = Achievement("Title1", "desc1", "/images/a1.jpeg")
		achievement2 = Achievement("Title2", "desc2", "/images/a2.jpeg")
		achievement3 = Achievement("Title3", "desc3", "/images/a3.jpeg")	

		athlete1 = Athlete(
            "username",
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
            "username",
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

	def test_get_all_achievements_with_data_on_database(self):
		self.populate_database_with_test_data()
		
		achievements = self.ach_controller.get_achievements()
		expected = [
			{
				'image_url': u'/images/a1.jpeg',
				'description': u'desc1', 
				'title': u'Title1'
			},
			{
				'image_url': u'/images/a2.jpeg', 
				'description': u'desc2', 
				'title': u'Title2'
			},
			{
				'image_url': u'/images/a3.jpeg', 
				'description': u'desc3', 
				'title': u'Title3'
			}
		]
		self.assertEqual(achievements, expected)

	def test_get_all_achievements_with_empty_database(self):
		achievements = self.ach_controller.get_achievements()
		self.assertEqual(achievements, [])		
	
	def test_get_unlock_achievement_with_data_on_database(self):
		self.populate_database_with_test_data()
		
		unlocked_achievements = self.ach_controller.get_unlocked_achievements()
		self.assertTrue(len(unlocked_achievements) == 2)
		
		unlocked_achievements[0]['unlocked_date'] = 'test_date_string1'
		unlocked_achievements[1]['unlocked_date'] = 'test_date_string2'

		expected = [
			{
				'unlocked_date': 'test_date_string1', 
				'achievement': {
					'image_url': u'/images/a1.jpeg', 
					'description': u'desc1', 
					'title': u'Title1'
				}
			},
			{
				'unlocked_date': 'test_date_string2', 
				'achievement': {
					'image_url': u'/images/a2.jpeg', 
					'description': u'desc2', 
					'title': u'Title2'
				}
			}
		]
		self.assertEqual(unlocked_achievements, expected)
	
	def test_unlock_achievement_with_empty_database_raise_exception(self):
		unlocked_achievements = self.ach_controller.get_unlocked_achievements()
		self.assertEqual(unlocked_achievements, [])









