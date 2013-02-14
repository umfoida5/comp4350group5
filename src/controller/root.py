import cherrypy
from athletes import Athletes
from activities import Activities
from events import Events
from stats import Stats
from modules.template import env

class Root:
    athletes = Athletes()
    activities = Activities()
    events = Events()
    stats = Stats()

    @cherrypy.expose
    def index(self):
        tmpl = env.get_template('index.html')
        return tmpl.render()

    @cherrypy.expose
    def about(self):
        tmpl = env.get_template('about.html')
        return tmpl.render()


