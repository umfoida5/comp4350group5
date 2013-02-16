import datetime
import cherrypy
from modules import database
from model.event import Event
from modules.template import env
from modules.datatables import dtify

class Stats:
    @cherrypy.expose
    def index(self):
        tmpl = env.get_template('stats.html')
        return tmpl.render()

    @cherrypy.expose
    def create(self):
        tmpl = env.get_template('stats.html')
        return tmpl.render()
