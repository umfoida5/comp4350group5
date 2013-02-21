import cherrypy
import sys
from controller.statistics_engine import StatisticsEngine
from modules.datatables import send_datatable_response
from modules import database
from modules.template import env
from modules.jsonable import make_jsonable

class Stats:

    @cherrypy.expose
    def index(self):
        tmpl = env.get_template('stats.html')
        return tmpl.render()

    @cherrypy.tools.json_out()
    @cherrypy.expose
    def get_total(self, **params):
    	mySE = StatisticsEngine()
    	result = StatisticsEngine.total(mySE, **params)
    	print "the results of the call: ",
    	print result
	return make_jsonable(result)