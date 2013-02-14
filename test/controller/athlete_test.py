import sys
import os
dirPath = os.path.join(os.pardir, '../../src')
print(dirPath)
sys.path.append(dirPath)
from controller.athletes import Athletes
import nose

class TestAthlete(object):
	@classmethod
	def setup_class(klass):
		"""This method is run once for each class before any tests are run"""
	@classmethod
	def teardown_class(klass):
		"""This method is run once for each class _after_ all tests are run"""
	def setup(self):
		""""""
	def teardown(self):
		""""""
	def test_init(self):
		athlete = Athletes()
	def test_json(self):
		athlete = Athletes()
		jathletes = athlete.json()
		assert_not_nil(jathletes)
		
