import cherrypy
from datetime import datetime
from modules import database
from model.event import Event
from modules.template import env
from modules.datatables import dtify

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
    def json(self, **params):
        search = '%%%s%%' % params['sSearch']
        search_filter = Event.location.like(search.lower()) #Search by location, lower case (we convert all input for City into lowercase)

        def convert(row):
            return (row.event_date.strftime('%b %d, %Y'), row.description, row.location, row.distance) #return the date string rather than the date itself

        return dtify(Event.query, search_filter, convert, params)
    
    @cherrypy.expose
    def createEvent(self, eventDate=None, eventLocation=None, eventDistance=None, eventDescription=None):
        db_session = database.session

        if eventDate is not None and eventLocation is not None and eventDistance is not None and eventDescription is not None:
            newEvent = Event(datetime.strptime(eventDate, "%d-%m-%Y"), eventDescription, eventLocation, int(eventDistance))
            db_session.add(newEvent)
            db_session.commit()
            
        tmpl = env.get_template('events.html')
        return tmpl.render() 
