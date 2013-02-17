import cherrypy
from modules.template import env

class Stats:
    @cherrypy.expose
    def index(self):
        tmpl = env.get_template('stats.html')
        return tmpl.render()

    @cherrypy.expose
    def create(self):
        tmpl = env.get_template('stats.html')
        return tmpl.render()
