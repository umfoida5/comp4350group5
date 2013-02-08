import unittest
import cherrypy
import sys
import os
from jinja2 import Environment, FileSystemLoader
sys.path.append('../../controller')
from root import Root

env = Environment(loader=FileSystemLoader('view/web/templates'))

class RootTest:
	
	def indexTest(self):
		return True
		
