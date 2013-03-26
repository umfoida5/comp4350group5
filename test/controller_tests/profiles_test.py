import unittest
import cherrypy
from controller.profiles import Profiles
from modules import database
from model.achievement import Achievement
from model.athlete import Athlete
import datetime

class ProfilesTest(unittest.TestCase):
    profile = Profiles()
    @classmethod
    def setUp(cls):
        database.empty_database()
        athlete = Athlete(username='john', password='john', first_name='John', last_name='Doe', email='email@gmail.com', birth_date=None)
        database.session.add(athlete)
        database.session.commit()

        cherrypy.session['id'] = athlete.id

    def test_get_athlete(self):
        json = self.profile.athlete()
        expected = {'achievements': [], 
            'first_name': u'John', 
            'last_name': u'Doe', 
            'about_me': u'', 
            'avatar': u'', 
            'address': u'', 
            'birth_date': None, 
            'email': 'email@gmail.com'
        }
        
        self.assertEqual(json, expected)

    def test_update_about(self):
        json = self.profile.update_about(2,"profile")
        athlete = Athlete.query.first()
        self.assertEqual(athlete.about_me, "profile")

        expected = {'achievements': [], 
            'first_name': u'John', 
            'last_name': u'Doe', 
            'about_me': u'profile', 
            'avatar': u'', 
            'address': u'', 
            'birth_date': None, 
            'email': 'email@gmail.com'
        }


        self.assertEqual(json, expected)

    def test_update_email(self):
        json = self.profile.update_email(1,"email@email.ca")
        athlete = Athlete.query.first()
        self.assertEqual(athlete.email, "email@email.ca")
        expected = {'achievements': [], 
            'first_name': u'John', 
            'last_name': u'Doe', 
            'about_me': u'', 
            'avatar': u'', 
            'address': u'', 
            'birth_date': None, 
            'email': 'email@email.ca'
        }
        self.assertEqual(json, expected)

    def test_update_address(self):
        json = self.profile.update_address(1,"123 fake street")
        athlete = Athlete.query.first()
        self.assertEqual(athlete.address, "123 fake street")
        expected = {'achievements': [], 
            'first_name': u'John', 
            'last_name': u'Doe', 
            'about_me': u'', 
            'avatar': u'', 
            'address': u'123 fake street', 
            'birth_date': None, 
            'email': 'email@gmail.com'
        }
        self.assertEqual(json, expected)

    def test_update_birth_date(self):
        json = self.profile.update_dob(1,"2001-12-12")
        athlete = Athlete.query.first()
        self.assertEqual(athlete.birth_date, datetime.date(2001,12,12))
        expected = {'achievements': [], 
            'first_name': u'John', 
            'last_name': u'Doe', 
            'about_me': u'', 
            'avatar': u'', 
            'address': u'', 
            'birth_date': '2001-12-12', 
            'email': 'email@gmail.com'
        }
        self.assertEqual(json, expected)
