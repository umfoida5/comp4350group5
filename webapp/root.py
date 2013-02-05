import cherrypy
from workouts import Workouts

class Root:
    workouts = Workouts()

    @cherrypy.expose
    def index(self):
        raise cherrypy.InternalRedirect("/Code/index.html")

