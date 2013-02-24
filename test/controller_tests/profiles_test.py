import unittest
import sys
sys.path.append('../../src')
from controller.profiles import Profiles
from modules import database
from model.achievement import Achievement
from model.athlete import Athlete
import datetime
class ProfilesTest(unittest.TestCase):
		
	@classmethod
	def setUpClass(cls):
		database.init("tracker_test")
		database.empty_database()
		athlete = Athlete('John', 'Doe', 'email@gmail.com', datetime.datetime.now())
		database.session.add(athlete)
		database.session.commit()
		
	def test_update_about(self):
		profile = Profiles()
		json = profile.update_about(1,"profile")
		athlete = Athlete.query.first()
		self.assertEqual(athlete.about_me, "profile")
		self.assertNotEqual(json, "")
		
	def test_update_email(self):
		profile = Profiles()
		json = profile.update_email(1,"email@email.ca")
		athlete = Athlete.query.first()
		self.assertEqual(athlete.email, "email@email.ca")
		self.assertNotEqual(json, "")
		
	def test_update_address(self):
		profile = Profiles()
		json = profile.update_address(1,"123 fake street")
		athlete = Athlete.query.first()
		self.assertEqual(athlete.address, "123 fake street")
		self.assertNotEqual(json, "")
		
	def test_update_birth_date(self):
		profile = Profiles()
		json = profile.update_dob(1,"2001-12-12")
		athlete = Athlete.query.first()
		self.assertEqual(athlete.birth_date, datetime.date(2001,12,12))
		self.assertNotEqual(json, "")
		
if(__name__ == '__main__'):
	unittest.main()
