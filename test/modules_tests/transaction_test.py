import unittest
from modules import database
from modules.transaction import commit_on_success
from model.athlete import Athlete

class TransactionTests(unittest.TestCase):	

	@classmethod
	def setUpClass(cls):
		database.init("tracker_test")

	def setUp(self):
		database.empty_database()

	@commit_on_success
	def commit_changes_unless_specified(cls, given_object, commit=True):
		database.session.add(given_object)

		if commit == False:
			raise Exception()

	def test_commit_on_success_commits_changes(self):
		athlete = Athlete("firstname", "lastname", "a@a.a")
		self.commit_changes_unless_specified(athlete, True)

		self.assertTrue(len(Athlete.query.all()) == 1)
		self.assertIsNotNone(Athlete.query.first())
		self.assertTrue(Athlete.query.first() == athlete)

	def test_commit_on_success_rollbacks_changes(self):
		with self.assertRaises(Exception):
			self.commit_changes_unless_specified(
				Athlete("firstname", "lastname", "a@a.a"),
				False
			)

		self.assertTrue(len(Athlete.query.all()) == 0)

if(__name__ == '__main__'):
	unittest.main()
