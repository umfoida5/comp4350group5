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
        
        
    def test_create(self):
        self.activity.create("test", "11-11-1111", 123, 123, 123)
        results = Activity.query.filter(Activity.type == "test").first()
        self.assertTrue(results.distance == 123)
        self.assertTrue(results.max_speed == 123)
        self.assertTrue(results.duration == 123)

        self.activity.create("test2", "10-11-2000", 222, 222, 222)
        results = Activity.query.filter(Activity.type == "test2").first()
        self.assertTrue(results.distance == 222)
        self.assertTrue(results.max_speed == 222)
        self.assertTrue(results.duration == 222)

        self.activity.create("test3", "22-09-1999", 133, 111, 999)
        results = Activity.query.filter(Activity.type == "test3").first()
        self.assertTrue(results.distance == 133)
        self.assertTrue(results.duration == 111)
        self.assertTrue(results.max_speed == 999)      

    def test_update_datatable(self):
        #retrieves empty json from datatables method   
        database.empty_database()     
        the_json = self.activity.update_datatable()
        self.assertTrue(len(the_json['aaData']) == 0)


        self.setUp() 
        the_json = self.activity.update_datatable()
        self.assertTrue(len(the_json['aaData']) == 9)

        self.assertTrue(the_json['aaData'][0]['date']  == "1000-01-01")
        self.assertTrue(the_json['aaData'][0]['duration'] == 10)
        self.assertTrue(the_json['aaData'][0]['max_speed']    == 10)
        self.assertTrue(the_json['aaData'][0]['type']    == u'run')
        self.assertTrue(the_json['aaData'][0]['distance']    == 10)

    def test_json(self):
        data = self.activity.json('01-01-0001', '01-01-9999')
        expected = {'activities': [{'date': '1000-01-01', 'duration': 10, 'max_speed': 10, 'type': u'run', 'distance': 10}, {'date': '2000-01-01', 'duration': 10, 'max_speed': 10, 'type': u'run', 'distance': 10}, {'date': '3000-01-01', 'duration': 10, 'max_speed': 10, 'type': u'run', 'distance': 10}, {'date': '2000-02-02', 'duration': 20, 'max_speed': 20, 'type': u'run', 'distance': 20}, {'date': '4000-02-02', 'duration': 20, 'max_speed': 20, 'type': u'run', 'distance': 20}, {'date': '6000-02-02', 'duration': 20, 'max_speed': 20, 'type': u'run', 'distance': 20}, {'date': '3000-03-03', 'duration': 30, 'max_speed': 30, 'type': u'run', 'distance': 30}, {'date': '6000-03-03', 'duration': 30, 'max_speed': 30, 'type': u'run', 'distance': 30}, {'date': '9000-03-03', 'duration': 30, 'max_speed': 30, 'type': u'run', 'distance': 30}]}
        self.assertEqual(data, expected)

