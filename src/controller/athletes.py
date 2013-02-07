import cherrypy
from modules.database import db_session
from model.athlete import Athlete

class Athletes:
    @cherrypy.tools.json_out()
    @cherrypy.expose
    def index(self, **params):
        response = {}
        athletes = Athlete.query.all()

        aaData = []
        for athlete in athletes:
            aaData.append((athlete.first_name, athlete.last_name))
        response['aaData'] = aaData

        return response
    
