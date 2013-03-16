import unittest
import cherrypy
from datetime import date
from model.athlete import Athlete
from model.activity import Activity
from modules.datatables import send_datatable_response
from modules import database

class DatatablesTests(unittest.TestCase):	
    @classmethod
    def setUp(self):
        database.empty_database()
        session = database.session

        session.add(Athlete('john', 'password', 'John', 'Doe', 'email@gmail.com'))
        session.commit()
        athlete_id = Athlete.query.first().id
        cherrypy.session['id'] = athlete_id

        session.add(Activity(athlete_id, "Bike", date(2013, 2, 8), 25, 50, 25))
        session.add(Activity(athlete_id, "Run", date(2013, 2, 9), 35, 20, 40))
        session.add(Activity(athlete_id, "Walk", date(2013, 2, 10), 72, 40, 10))
        session.add(Activity(athlete_id, "Walk", date(2013, 2, 11), 72, 40, 10))
        session.add(Activity(athlete_id, "Ak", date(2013, 2, 11), 65, 70, 52))

        session.commit()

    def test_datatables(self):
        request_params = {
            'sEcho': "0",
            'sSearch': "k",
            'iColumns': "5",
            'bSearchable_0': "true",
            'bSearchable_1': "false",
            'bSearchable_2': "false",
            'bSearchable_3': "false",
            'bSearchable_4': "false",
            'mDataProp_0': "type",
            'mDataProp_1': "date",
            'mDataProp_2': "duration",
            'mDataProp_3': "distance",
            'mDataProp_4': "max_speed",
            'iSortCol_0': "0",
            'sSortDir_0': "asc",
            'iDisplayLength': "2",
            'iDisplayStart': "1"
        }

        data = send_datatable_response(Activity, True, request_params)

        expected = {
            'sEcho': 0,
            'iTotalRecords': 5,
            'iTotalDisplayRecords': 4,
            'aaData': [
                {
                    'type': "Bike",
                    'date': "2013-02-08",
                    'duration': 50,
                    'distance': 25,
                    'max_speed': 25
                },
                {
                    'type': "Walk",
                    'date': "2013-02-10",
                    'duration': 40,
                    'distance': 72,
                    'max_speed': 10
                }
            ]
        }

        self.assertEqual(data, expected)

if(__name__ == '__main__'):
    unittest.main()
