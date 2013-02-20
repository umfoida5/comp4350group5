import cherrypy
from sqlalchemy import or_
from model.event import Event
from modules import database
from modules.template import env
from modules.datatables import send_datatable_response
from datetime import datetime

class Events:
    @cherrypy.expose
    def index(self):
        tmpl = env.get_template('events.html')
        return tmpl.render()

    @cherrypy.expose
    def create(self, date, location, distance, description):
        db_session = database.session

        newEvent = Event(datetime.strptime(date, "%d-%m-%Y"), str(description), str(location), int(distance))
        db_session.add(newEvent)
        db_session.commit()

    @cherrypy.tools.json_out()
    @cherrypy.expose
    def update_datatable(self, **params):
        return send_datatable_response(Event, params)
