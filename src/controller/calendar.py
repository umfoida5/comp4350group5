import cherrypy
from modules.template import env

class Calendar:
    @cherrypy.expose
    def index(self):
        tmpl = env.get_template('calendar_view.html')
        return tmpl.render()
