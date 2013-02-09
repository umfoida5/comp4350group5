import unittest
import cherrypy
import sys
import os
from jinja2 import Environment, FileSystemLoader
sys.path.append('../../src')
from controller.root import Root

env = Environment(loader=FileSystemLoader('view/web/templates'))

class RootTest(unittest.TestCase):
	
	def indexTest(self):
		return True
		
if(__name__ == '__main__'):
	unittest.main()
