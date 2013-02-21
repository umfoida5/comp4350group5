import unittest
from controller.athletes import Athlete

class AthletesTest(unittest.TestCase):

	@unittest.skip("Partially Implemented - test is failing")
	def test_init(self):
		athlete = Athlete()

	@unittest.skip("Partially Implemented - test is failing")
	def test_json(self):
		athlete = Athlete()
		jathletes = athlete.json()
		assert_not_nil(jathletes)
		