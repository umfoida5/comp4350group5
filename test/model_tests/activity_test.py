import unittest
from datetime import datetime
from modules import database
from model.activity import Activity
from model.athlete import Athlete

class ActivityTests(unittest.TestCase):	

    @classmethod
    def setUpClass(cls):
        database.init("tracker_test")

    def setUp(self):
        database.empty_database()
        database.session.add(Athlete("test_first", "test_last", "test@test.test", datetime.now()))
        database.session.commit()

    def test_activity_object_creation(self):
        test_athlete = Athlete.query.filter(Athlete.first_name == "test_first").first()
        self.assertIsNotNone(test_athlete)

        activity1 = Activity(test_athlete.id, "test1", datetime.now(), 111, 111, 111)
        activity2 = Activity(test_athlete.id, "test2", datetime.now(), 222, 222, 222)
        activity3 = Activity(test_athlete.id, "test3", datetime.now(), 333, 333, 333)
        database.session.add(activity1)
        database.session.add(activity2)
        database.session.add(activity3)
        database.session.commit()

        queried_activity1 = Activity.query.filter_by(type = "test1").first()
        queried_activity2 = Activity.query.filter_by(type = "test2").first()
        queried_activity3 = Activity.query.filter_by(type = "test3").first()

        self.assertIsNotNone(queried_activity1)
        self.assertIsNotNone(queried_activity2)
        self.assertIsNotNone(queried_activity3)

        self.assertEqual(queried_activity1, activity1)
        self.assertEqual(queried_activity2, activity2)
        self.assertEqual(queried_activity3, activity3)

        self.assertTrue(len(Activity.query.all()) == 3)

if(__name__ == '__main__'):
    unittest.main()

