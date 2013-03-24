import unittest, datetime
import cherrypy
from modules import database
from controller.login import Login
from model.athlete import Athlete
from model.health import Health
from model.activity import Activity
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


	def test_logout_success(self):
		self.populate_database_with_test_data()
		db_session = database.session

		athlete1 = Athlete.query.all()[0];
		athlete2 = Athlete.query.all()[1];

		health_record   = Health(athlete1.id, '1999-01-01', 123, 123, 'this is a test')
		activity_record = Activity(athlete1.id, 'Run', '1999-01-01', 123, 123, 123)

		db_session.add(health_record)
		db_session.add(activity_record)
		db_session.commit()

		health_records_1 = Health.query.filter_by(athlete_id = athlete1.id).all()
		health_records_2 = Health.query.filter_by(athlete_id = athlete2.id).all()
		
		activity_record_1 = Activity.query.filter_by(athlete_id = athlete1.id).all()
		activity_record_2 = Activity.query.filter_by(athlete_id = athlete2.id).all()

		self.assertEqual(1, len(health_records_1))
		self.assertEqual(0, len(health_records_2))
		self.assertEqual(1, len(activity_record_1))
		self.assertEqual(0, len(activity_record_2))

		self.login_controller.update_tables_athlete_id(athlete1.id, athlete2.id)

		health_records_1 = Health.query.filter_by(athlete_id = athlete1.id).all()
		health_records_2 = Health.query.filter_by(athlete_id = athlete2.id).all()
		
		activity_record_1 = Activity.query.filter_by(athlete_id = athlete1.id).all()
		activity_record_2 = Activity.query.filter_by(athlete_id = athlete2.id).all()

		self.assertEqual(0, len(health_records_1))
		self.assertEqual(1, len(health_records_2))
		self.assertEqual(0, len(activity_record_1))
		self.assertEqual(1, len(activity_record_2))
