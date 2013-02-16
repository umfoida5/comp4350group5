import unittest
from modules import database
from modules.transaction import commit_on_success

class TransactionTests(unittest.TestCase):	

	@unittest.skip("Not implemented")
	def test_commit_on_success(self):
		self.fail("Not implemented")   

if(__name__ == '__main__'):
	unittest.main()

