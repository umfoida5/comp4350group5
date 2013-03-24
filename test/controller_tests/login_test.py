import unittest, datetime
import cherrypy
from modules import database
from controller.login import Login
from model.athlete import Athlete
from Cookie import SimpleCookie

class LoginTest(unittest.TestCase):
	login_controller = Login()

	def setUp(self):
		database.empty_database()

	def populate_database_with_test_data(self):
		db_session = database.session
		db_session.add(Athlete("justin", "sha256andsalted", "Joe", "Smith", "email@email.com", "1980-11-23", "All work and no play makes Joe a dull boy", "123 Fake Street Winnipeg, MB", "/comp4350group4/src/view/web/profile/pic.png"))
		db_session.add(Athlete("ben", "sha256andsalted", "Bob", "Brown", "email@email.com", "1980-11-23", "All work and no play makes Joe a dull boy", "123 Fake Street Winnipeg, MB", "/comp4350group4/src/view/web/profile/pic.png"))
		db_session.add(Athlete("sammy", "sha256andsalted", "Frank", "Reese", "email@email.com", "1980-11-23", "All work and no play makes Joe a dull boy", "123 Fake Street Winnipeg, MB", "/comp4350group4/src/view/web/profile/pic.png"))
		db_session.commit()      

	def test_login_invalid_username(self):
		self.populate_database_with_test_data()
		
		#initialize temporary session id
		self.login_controller.do_login("badusername", "anypassword")
		temp_athlete_id = cherrypy.session.get('id')
		
		#Ensure login fails with bad data -> session 
		#id does not change
		self.login_controller.do_login("badusername", "anypassword")
		self.assertEqual(temp_athlete_id, cherrypy.session.get('id'))
		
		#Ensure login fails with bad data -> session 
		#id does not change
		self.login_controller.do_login("justi", "somepassword")
		self.assertEqual(temp_athlete_id, cherrypy.session.get('id'))
		
		#Ensure login fails with bad data -> session 
		#id does not change
		self.login_controller.do_login("benz", "thebestpassword")
		self.assertEqual(temp_athlete_id, cherrypy.session.get('id'))

	def test_login_invalid_password(self):
		self.populate_database_with_test_data()
		
		#initialize temporary session id
		self.login_controller.do_login("justin", "anypassword")
		temp_athlete_id = cherrypy.session.get('id')
		
		#Ensure login fails with bad data -> session 
		#id does not change
		self.login_controller.do_login("ben", "anypassword")
		self.assertEqual(temp_athlete_id, cherrypy.session.get('id'))
		
		#Ensure login fails with bad data -> session 
		#id does not change
		self.login_controller.do_login("justin", "somepassword")
		self.assertEqual(temp_athlete_id, cherrypy.session.get('id'))
		
		#Ensure login fails with bad data -> session 
		#id does not change
		self.login_controller.do_login("sammy", "thebestpassword")
		self.assertEqual(temp_athlete_id, cherrypy.session.get('id'))
	
	def test_login_success(self):
		self.populate_database_with_test_data()
		
		#initialize temporary session id
		self.login_controller.do_login("justin", "BADPASSWORD")
		temp_athlete_id = cherrypy.session.get('id')
		
		#Ensure login succeeds with good data -> session 
		#id should change between different users
		self.login_controller.do_login("ben", "sha256andsalted")
		self.assertNotEqual(temp_athlete_id, cherrypy.session.get('id'))
		
		#Ensure login succeeds with good data -> session 
		#id should change between different users
		self.login_controller.do_login("justin", "sha256andsalted")
		self.assertNotEqual(temp_athlete_id, cherrypy.session.get('id'))
		
		#Ensure login succeeds with good data -> session 
		#id should change between different users
		self.login_controller.do_login("sammy", "sha256andsalted")
		self.assertNotEqual(temp_athlete_id, cherrypy.session.get('id'))
	
	def test_signup_success(self):
		self.populate_database_with_test_data()

		#initialize temporary session id
		self.login_controller.do_login("justin", "sha256andsalted")
		temp_athlete_id = cherrypy.session.get('id')
		
		#Ensure signup succeeds with proper credentials
		#On successful signup, the temp ID becomes the permanent id
		self.login_controller.signup("fdart", "worstfdartpw", "justin", "fdart")
		athlete = Athlete.query.filter_by(id = cherrypy.session.get('id')).one()
		
		self.assertEqual("fdart", athlete.username)
		self.assertEqual("worstfdartpw", athlete.password)
		self.assertEqual("justin", athlete.first_name)
		self.assertEqual("fdart", athlete.last_name)

		self.assertEqual("fdart", cherrypy.session['username'])

	def test_signup_failure(self):
		self.populate_database_with_test_data()

		#initialize temporary session id
		self.login_controller.do_login("justin", "sha256andsalted")

		temp_athlete_id = cherrypy.session.get('id')
		message = self.login_controller.signup('justin', 'sha256andsalted', 'Joe', 'Smith')
		self.assertEqual('Username already exists. Please enter a new username.', message)

	def test_logout_success(self):
		self.populate_database_with_test_data()
		self.login_controller.do_login("ben", "anypassword")
		old_id = cherrypy.session.get('id')
		self.login_controller.do_logout()
		
		#test that session id is the same and session variable(s) are set back to default 
		self.assertNotEqual(old_id, cherrypy.session.get('id'))
		self.assertFalse(cherrypy.session.has_key('username'))
