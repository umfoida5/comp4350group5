import cherrypy
import sys
from controller.statistics_engine import StatisticsEngine
from modules.datatables import send_datatable_response
from modules import database
from modules.template import env

class Stats:

    mySE = StatisticsEngine()

    @cherrypy.expose
    def index(self):
        tmpl = env.get_template('stats.html')
        return tmpl.render()

    @cherrypy.tools.json_out()
    @cherrypy.expose
    def get_total(self, **params):
    	result = StatisticsEngine.total(Stats.mySE, **params)
	return result
	
    @cherrypy.tools.json_out()
    @cherrypy.expose
    def get_average(self, **params):
     	result = StatisticsEngine.average(Stats.mySE, **params)
	return result
	
    @cherrypy.tools.json_out()
    @cherrypy.expose
    def get_minimum(self, **params):
     	result = StatisticsEngine.minimum(Stats.mySE, **params)
	return result
	
    @cherrypy.tools.json_out()
    @cherrypy.expose
    def get_maximum(self, **params):
     	result = StatisticsEngine.maximum(Stats.mySE, **params)
	return result
