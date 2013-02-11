import sys
import unittest
sys.path.append('../../src')
from controller.athletes import Athletes
from modules.database import init_db, db_session
class AthleteTests(unittest.TestCase):
		
	def test_json(self):
		init_db()
		js = Athletes.json(Athletes(), beaty="be", blake="bl")
		print(js)
		self.assertEqual("", js) 
		
if(__name__ == '__main__'):
	unittest.main()
