import unittest
from datetime import datetime
from modules import database
from model.event import Event

class EventTests(unittest.TestCase):	

	def setUp(self):
		database.empty_database()

	def test_event_object_creation(self):
		event1 = Event(datetime.now(), "Unit Test Description 1", "location1", 1)
		event2 = Event(datetime.now(), "Unit Test Description 2", "location2", 2)
		event3 = Event(datetime.now(), "Unit Test Description 3", "location3", 3)
		database.session.add(event1)
		database.session.add(event2)
		database.session.add(event3)
		database.session.commit()

		queried_event1 = Event.query.filter_by(location = "location1").first()
		queried_event2 = Event.query.filter_by(location = "location2").first()
		queried_event3 = Event.query.filter_by(location = "location3").first()

		self.assertFalse(queried_event1 is None)
		self.assertFalse(queried_event2 is None)
		self.assertFalse(queried_event3 is None)

		self.assertEqual(queried_event1, event1)
		self.assertEqual(queried_event2, event2)
		self.assertEqual(queried_event3, event3)

		self.assertTrue(len(Event.query.all()) == 3)

