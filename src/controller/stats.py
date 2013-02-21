import cherrypy
import sys
import controller.statistics_engine
from modules import database
from modules.template import env
from modules.jsonable import make_jsonable

class Stats:

    @cherrypy.expose
    def index(self):
        tmpl = env.get_template('stats.html')
        return tmpl.render()

    @cherrypy.expose
    def create(self):
        tmpl = env.get_template('stats.html')
        return tmpl.render()

    @cherrypy.tools.json_out()
    @cherrypy.expose
    def get_total(self, **params):
    	result = StatisticsEngine.total(StatisticsEngine, params)
	return make_jsonable(result)