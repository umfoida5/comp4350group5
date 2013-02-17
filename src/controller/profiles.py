import cherrypy
from modules import database
from modules.template import env

class Profiles:
    @cherrypy.expose
    def index(self):
        tmpl = env.get_template('profile.html')
        return tmpl.render()
        
