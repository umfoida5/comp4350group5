import sys
import unittest
sys.path.append('src')

from modules.database import init_db, db_session
from model import achievement

class AchievementTests(unittest.TestCase):
	pass
		
if(__name__ == '__main__'):
	unittest.main()
