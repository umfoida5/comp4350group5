import unittest, datetime
import cherrypy
from sqlalchemy.orm.exc import NoResultFound
from modules import database
from controller.events import Events
from model.event import Event

class EventsTest(unittest.TestCase):
    events_controller = Events()

    def setUp(self):
        database.empty_database()

    def populate_database_with_test_data(self):
        event1 = Event("1980-01-01", "I am a test event 1", "test_city_1", 123)  

        database.session.add(event1)
        database.session.flush()
        database.session.commit()

    def test_create(self):
        self.events_controller.create(
            "01-01-1980", 
            "test_city_1",   
            123,
            "I am a test event 1",)
        
        the_event = Event.query.first()

        self.assertTrue(the_event.event_date  == datetime.date(1980,01,01))
        self.assertTrue(the_event.description == "I am a test event 1")
        self.assertTrue(the_event.location    == "test_city_1")
        self.assertTrue(the_event.distance    == 123)

    def test_update_datatable(self):
        #retrieves empty json from datatables method        
        the_json = self.events_controller.update_datatable()
        self.assertTrue(len(the_json['aaData']) == 0)


        self.populate_database_with_test_data() 
        the_json = self.events_controller.update_datatable()
        self.assertTrue(len(the_json['aaData']) == 1)

        self.assertTrue(the_json['aaData'][0]['event_date']  == "1980-01-01")
        self.assertTrue(the_json['aaData'][0]['description'] == "I am a test event 1")
        self.assertTrue(the_json['aaData'][0]['location']    == "test_city_1")
        self.assertTrue(the_json['aaData'][0]['distance']    == 123)

