import cherrypy
from modules.database import db_session
from model.athlete import Athlete

class Workouts:
    @cherrypy.tools.json_out()
    @cherrypy.expose
    def index(self, **params):
        return Athlete.query.all()
    
