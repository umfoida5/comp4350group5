import unittest
from controller.athletes import Athlete

class AthleteTest(unittest.TestCase):
    def test_init(self):
        athlete = Athlete()
    def test_json(self):
        athlete = Athlete()
        jathletes = athlete.json()
        assert_not_nil(jathletes)
		
