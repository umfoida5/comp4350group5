import unittest
from model.athlete import Athlete
from modules.jsonable import Jsonable, make_jsonable

class JsonableTests(unittest.TestCase):	

	def test_make_jsonable_with_non_object_as_value(self):
		with self.assertRaises(AttributeError):
			make_jsonable("athlete")

	def test_make_jsonable_with_single_object_as_value(self):
		athlete = Athlete("firstname", "lastname", "a@a.a")
		data = make_jsonable(athlete)
		expected = {
			'achievements': [],
			'first_name': 'firstname',
			'last_name': 'lastname',
			'about_me': '',
			'avatar': '', 
			'address': '', 
			'birth_date': None, 
			'email': 'a@a.a'
		}

		self.assertEqual(data, expected)
		self.assertEqual(data, athlete.to_dict())

	def test_make_jsonable_with_list_of_objects_as_value(self):
		athlete1 = Athlete("firstname1", "lastname", "a@a.a")
		athlete2 = Athlete("firstname2", "lastname", "a@a.a")
		athlete3 = Athlete("firstname3", "lastname", "a@a.a")
		athlete_list = [athlete1, athlete2, athlete3]

		data = make_jsonable(athlete_list)
		expected = [
			{
				'achievements': [],
				'first_name': 'firstname1',
				'last_name': 'lastname',
				'about_me': '',
				'avatar': '', 
				'address': '', 
				'birth_date': None, 
				'email': 'a@a.a'
			},
			{
				'achievements': [],
				'first_name': 'firstname2',
				'last_name': 'lastname',
				'about_me': '',
				'avatar': '', 
				'address': '', 
				'birth_date': None, 
				'email': 'a@a.a'
			},
			{
				'achievements': [],
				'first_name': 'firstname3',
				'last_name': 'lastname',
				'about_me': '',
				'avatar': '', 
				'address': '', 
				'birth_date': None, 
				'email': 'a@a.a'
			}
		]

		self.assertEqual(data, expected)

		expected = []
		expected.append(athlete1.to_dict())
		expected.append(athlete2.to_dict())
		expected.append(athlete3.to_dict())
		self.assertEqual(data, expected)

if(__name__ == '__main__'):
	unittest.main()
