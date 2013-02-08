import cherrypy
from athletes import Athletes
from activities import Activities
from modules.template import env

class Root:
    athletes = Athletes()
    activities = Activities()

    @cherrypy.expose
    def index(self):
        tmpl = env.get_template('index.html')
        return tmpl.render()

    @cherrypy.expose
    def about(self):
        tmpl = env.get_template('about.html')
        return tmpl.render()


