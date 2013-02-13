import cherrypy
from modules.database import db_session
from model.event import Event
from modules.template import env
from modules.datatables import dtify

class Events:
    @cherrypy.expose
    def index(self):
        tmpl = env.get_template('events.html')
        return tmpl.render()

    @cherrypy.expose
    def new(self):
        tmpl = env.get_template('events_new.html')
        return tmpl.render()

    @cherrypy.expose
    def edit(self):
        tmpl = env.get_template('events_edit.html')
        return tmpl.render()

    @cherrypy.tools.json_out()
    @cherrypy.expose
    def json(self, **params):
        search = '%%%s%%' % params['sSearch']
        search_filter = None

        def convert(row):
            return (row.event_date.strftime('%m/%d/%Y'), row.description, row.location, row.distance)

        return dtify(Event.query, search_filter, convert, params)
    
