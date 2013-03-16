import unittest
import cherrypy
from modules import database
from model.activity import Activity
from model.athlete import Athlete
from controller.goals import Goals
from controller.activities import Activities
import datetime

class ActivitiesTest(unittest.TestCase):
    activity = Activities()
    
    def setUp(self):
        database.empty_database()
        # intialize the Athlete table with known values
        athlete = Athlete(
                "username",
                "password",
                "Test", 
                "Athlete", 
                "test@test.com", 
                datetime.datetime.now(), 
                "I'm a Test", 
                "test street", 
                "test avatar")
        database.session.add(athlete)
        database.session.commit()

        self.test_athlete = athlete
        cherrypy.session['id'] = athlete.id

        # initialize the Activity table with known values
        for num in range(1, 4):

            database.session.add(            
                Activity(
                    self.test_athlete.id, 
                    "run",
                    datetime.date(num * 1000, num, num),                    
                    num * 10, 
                    num * 10, 
                    num * 10))

            database.session.add(            
                Activity(
                    self.test_athlete.id, 
                    "run",
                    datetime.date(num * 2000, num, num),                    
                    num * 10, 
                    num * 10, 
                    num * 10))

            database.session.add(
                Activity(
                    self.test_athlete.id, 
                    "run",
                    datetime.date(num * 3000, num, num),                    
                    num * 10, 
                    num * 10, 
                    num * 10))

        database.session.commit()
        
        
    def test_create_(self):
        self.activity.create("test", "11-11-1111", 123, 123, 123)
        results = Activity.query.filter(Activity.type == "test").first()
        self.assertTrue(results.distance == 123)
        self.assertTrue(results.max_speed == 123)
        self.assertTrue(results.duration == 123)
        
