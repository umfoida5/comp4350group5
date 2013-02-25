import unittest
from modules import database
from model.activity import Activity
from model.athlete import Athlete
from controller.goals import Goals
from controller.activities import Activities
from controller.calendar import Calendar
import datetime

class CalendarTest(unittest.TestCase):

    C = Calendar()

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

        database.session.commit()
    
    def test_json_all(self):
        ''' Gets json for all activities in the calendar '''
        json = self.C.json(datetime.date(999, 9, 9), datetime.date(9999, 9, 9))
        self.assertTrue(len(json["activities"]) == 3)

    def test_json_year(self):
        ''' Gets json for all activities for a year in the calendar '''
        json = self.C.json(datetime.date(1000, 01, 01), datetime.date(1000,12,31))
        self.assertTrue(len(json["activities"]) == 1)

    def test_json_month(self):
        ''' Gets json for all activities for a month  in the calendar '''
        json = self.C.json(datetime.date(1000, 01, 01), datetime.date(1000, 01, 31))
        self.assertTrue(len(json["activities"]) == 1)

    def test_json_day(self):
        ''' Gets json for all activities for a day in the calendar '''
        json = self.C.json(datetime.date(1000, 01, 01), datetime.date(1000, 01, 01))
        self.assertTrue(len(json["activities"]) == 1)

    def test_create_(self):
        self.C.create("test", "11-11-8888", 123, 123, 123)
        results = Activity.query.filter(Activity.type == "test").first()
        assert(results.distance == 123)
        assert(results.max_speed == 123)
        assert(results.duration == 123)

