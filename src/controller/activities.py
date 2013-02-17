import cherrypy
from sqlalchemy import or_
from model.activity import Activity
from model.athlete import Athlete
from modules import database
from modules.template import env
from modules.datatables import send_datatable_response

class Activities:
    @cherrypy.expose
    def index(self):
        tmpl = env.get_template('activities.html')
        return tmpl.render()

    @cherrypy.expose
    def create(self, distance, duration):
        db_session = database.session

        athlete = Athlete.query.first()
        new = Activity(athlete.id, int(distance), int(duration))
        db_session.add(new)
        db_session.commit()

    @cherrypy.tools.json_out()
    @cherrypy.expose
    def update_datatable(self, **params):
        return send_datatable_response(Activity, params)
