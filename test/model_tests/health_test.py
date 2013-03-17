import unittest
from datetime import datetime
from modules import database
from model.health import Health
from model.athlete import Athlete

class HealthTests(unittest.TestCase):	

    def setUp(self):
        database.empty_database()

    def test_health_object_creation(self):
        athlete1 = Athlete("name1", "lastname1", "a@a.a.a", datetime.now())
        database.session.add(athlete1)
        database.session.commit()        
        
        health_record_1 = Health(athlete1.id, datetime.now(), 123, 23, "I am a test health record")
        health_record_2 = Health(athlete1.id, datetime.now(), 321, 32, "I am a second test health record")

        database.session.add(health_record_1)
        database.session.add(health_record_2)
        database.session.commit()

        health_records = Health.query.all()

        self.assertTrue(len(health_records) == 2)

        queried_health_record_1 = health_records[0]
        queried_health_record_2 = health_records[1]

        self.assertFalse(queried_health_record_1 is None)
        self.assertFalse(queried_health_record_2 is None)

        self.assertEqual(queried_health_record_1, health_record_1)
        self.assertEqual(queried_health_record_2, health_record_2)

