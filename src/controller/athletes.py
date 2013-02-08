import cherrypy
from modules.database import db_session
from model.athlete import Athlete
from modules.template import env

class Athletes:
    @cherrypy.expose
    def index(self):
        tmpl = env.get_template('athletes.html')
        return tmpl.render()

    @cherrypy.tools.json_out()
    @cherrypy.expose
    def json(self):
        response = {}
        athletes = Athlete.query.all()

        aaData = []
        for athlete in athletes:
            aaData.append((athlete.first_name, athlete.last_name))
        response['aaData'] = aaData

        return response
    
