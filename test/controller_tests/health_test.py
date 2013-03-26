import unittest
import cherrypy
from modules import database
from model.athlete import Athlete
from controller.health import HealthController
from model.health import Health
from datetime import datetime

class HealthTest(unittest.TestCase):
    health = HealthController()

    def setUp(self):
        """Setup"""
        database.empty_database()
        # intialize the Athlete table with known values
        athlete = Athlete(
                "username",
                "password",
                "Test", 
                "Athlete", 
                "test@test.com", 
                datetime.strptime("20-12-2012", "%d-%m-%Y"), 
                "I'm a Test", 
                "test street", 
                "test avatar")
        database.session.add(athlete)

       
        database.session.commit()
        athlete = database.session.query(Athlete).first()

        newHealthRecord = Health(
            athlete.id, 
            datetime.strptime("21-12-2012", "%d-%m-%Y"), 
            100, 
            40, 
            "comment2")

        
        database.session.add(newHealthRecord)
        database.session.commit()

        self.test_athlete = athlete
        cherrypy.session['id'] = athlete.id

    def test_create(self):
        """Test Create"""
        self.health.create(
        	"21-12-2012",
        	100,
        	40,
        	"comment2")
        record = database.session.query(Health).get(1)
        self.assertTrue(record.weight == 100)
        self.assertTrue(record.resting_heart_rate == 40)
        self.assertTrue(record.comments == "comment2")


    def test_update_datatable(self):
        """Test Update Datatable """
        #retrieves empty json from datatables method   

        the_json = self.health.update_datatable()
        self.assertTrue(len(the_json['aaData']) == 1)

        self.assertTrue(the_json['aaData'][0]['weight'] == 100)
        self.assertTrue(the_json['aaData'][0]['resting_heart_rate']    == 40)
        self.assertTrue(the_json['aaData'][0]['comments']    == u'comment2')

    def test_json(self):
        """Test Json"""
        data = self.health.json('01-01-0001', '01-01-9999')
        expected = {'health': [{'resting_heart_rate': 40, 'weight': 100, 'health_date': '2012-12-21', 'comments': u'comment2'}]}
        self.assertEqual(data, expected)
