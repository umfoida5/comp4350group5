import cherrypy
from modules import datatables

class Workouts:
    @cherrypy.tools.json_out() 
    @cherrypy.expose
    def index(self, **params):
        table = 'workouts'
        columns = ['name', 'distance']
        return datatables.getresponse(table, columns, params)
    
