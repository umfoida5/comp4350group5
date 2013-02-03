import cherrypy

class Workouts:
    @cherrypy.expose
    def index(self, **params):
        return "test"
    
