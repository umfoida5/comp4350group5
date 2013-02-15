import unittest
import cherrypy
import sys
import os
#~ from jinja2 import Environment, FileSystemLoader
sys.path.append('../../src')
from controller.root import Root


class RootTest(unittest.TestCase):
	
	def indexTest(self):
		self.assertTrue(True)	
if(__name__ == '__main__'):
	unittest.main()
