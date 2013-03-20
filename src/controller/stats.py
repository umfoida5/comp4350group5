import cherrypy
import sys
from controller.statistics_engine import StatisticsEngine
from model.athlete import Athlete
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
    	athlete = Athlete.query.filter_by(id = cherrypy.session.get('id')).one()
    	params['athlete_id'] = str(athlete.id)
    	result = StatisticsEngine.total(Stats.mySE, **params)
	return result
	
    @cherrypy.tools.json_out()
    @cherrypy.expose
    def get_average(self, **params):
    	athlete = Athlete.query.filter_by(id = cherrypy.session.get('id')).one()
    	params['athlete_id'] = str(athlete.id)
     	result = StatisticsEngine.average(Stats.mySE, **params)
	return result
	
    @cherrypy.tools.json_out()
    @cherrypy.expose
    def get_minimum(self, **params):
    	athlete = Athlete.query.filter_by(id = cherrypy.session.get('id')).one()
    	params['athlete_id'] = str(athlete.id)
     	result = StatisticsEngine.minimum(Stats.mySE, **params)
	return result
	
    @cherrypy.tools.json_out()
    @cherrypy.expose
    def get_maximum(self, **params):
    	athlete = Athlete.query.filter_by(id = cherrypy.session.get('id')).one()
    	params['athlete_id'] = str(athlete.id)
     	result = StatisticsEngine.maximum(Stats.mySE, **params)
	return result