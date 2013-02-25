import unittest
import sys
sys.path.append('../../src')
from modules import database
from model.activity import Activity
from model.athlete import Athlete
from controller.goals import Goals
from controller.activities import Activities

import datetime

class ActivitiesTest(unittest.TestCase):
    activity = Activities()
    
    @classmethod
    def setUpClass(cls):
        database.init("tracker_test")

    def setUp(self):
        database.empty_database()

        # intialize the Athlete table with known values
        database.session.add(
            Athlete(
                "Test", 
                "Athlete", 
                "test@test.com", 
                datetime.date(1111,11,11), 
                "I'm a Test", 
                "test street", 
                "test avatar"))

        database.session.commit()
        self.test_athlete = Athlete.query.filter_by(first_name = "Test").first()

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
        assert(results.distance == 123)
        assert(results.max_speed == 123)
        assert(results.duration == 123)
        
if(__name__ == '__main__'):
    unittest.main()
