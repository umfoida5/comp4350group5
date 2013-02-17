import cherrypy
from model.goal import Goal
from modules.template import env

class Goals:
    @cherrypy.expose
    def index(self):
        tmpl = env.get_template('goals.html')
        return tmpl.render()
