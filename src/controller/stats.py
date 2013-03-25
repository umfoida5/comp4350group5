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

        the_object = []        
        for stat in result:
            dictionary = {"year":stat.year, "month":stat.month, "day":stat.day, "value":stat.value}
            the_object.append(dictionary)

    	return the_object
	
    @cherrypy.tools.json_out()
    @cherrypy.expose
    def get_average(self, **params):
    	athlete = Athlete.query.filter_by(id = cherrypy.session.get('id')).one()
    	params['athlete_id'] = str(athlete.id)
     	result = StatisticsEngine.average(Stats.mySE, **params)
        the_object = []        
        for stat in result:
            dictionary = {"year":stat.year, "month":stat.month, "day":stat.day, "value":stat.value}
            the_object.append(dictionary)

    	return the_object
	
    @cherrypy.tools.json_out()
    @cherrypy.expose
    def get_minimum(self, **params):
    	athlete = Athlete.query.filter_by(id = cherrypy.session.get('id')).one()
    	params['athlete_id'] = str(athlete.id)
     	result = StatisticsEngine.minimum(Stats.mySE, **params)

        the_object = []        
        for stat in result:
            dictionary = {"year":stat.year, "month":stat.month, "day":stat.day, "value":stat.value}
            the_object.append(dictionary)

    	return the_object

	
    @cherrypy.tools.json_out()
    @cherrypy.expose
    def get_maximum(self, **params):
    	athlete = Athlete.query.filter_by(id = cherrypy.session.get('id')).one()
    	params['athlete_id'] = str(athlete.id)
     	result = StatisticsEngine.maximum(Stats.mySE, **params)

        the_object = []        
        for stat in result:
            dictionary = {"year":stat.year, "month":stat.month, "day":stat.day, "value":stat.value}
            the_object.append(dictionary)

    	return the_object

