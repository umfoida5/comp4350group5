import cherrypy
from modules.database import db_session
from jinja2 import Environment, FileSystemLoader
#from model.athlete import Athlete

env = Environment(loader=FileSystemLoader('view/web/templates'))

class Activities:
    #@cherrypy.tools.json_out()
    
#    @cherrypy.expose
#    def index(self, **params):
#        return "test"
#        athletes = Athlete.query.all()
#        aaData = []
#        for athlete in athletes:
#            aaData.append((athlete.first_name, athlete.last_name))
#        response['aaData'] = aaData
#        return response

    @cherrypy.expose
    def index(self):
        tmpl = env.get_template('activities.html')
        return tmpl.render()
    
