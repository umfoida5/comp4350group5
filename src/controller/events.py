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
    def create(self):
        tmpl = env.get_template('events_create.html')
        return tmpl.render()

    @cherrypy.tools.json_out()
    @cherrypy.expose
    def update_datatable(self, **params):
        search = '%%%s%%' % params['sSearch']
        search_filter = or_(
            Event.location.ilike(search),
            Event.description.ilike(search)
        )
        return send_datatable_response(Event.query, search_filter, params)
    
    @cherrypy.expose
    def createEvent(self, eventDate=None, eventLocation=None, eventDistance=None, eventDescription=None):
        db_session = database.session

        if eventDate is not None and eventLocation is not None and eventDistance is not None and eventDescription is not None:
            newEvent = Event(datetime.strptime(eventDate, "%d-%m-%Y"), eventDescription, eventLocation, int(eventDistance))
            db_session.add(newEvent)
            db_session.commit()
            
        tmpl = env.get_template('events.html')
        return tmpl.render() 
