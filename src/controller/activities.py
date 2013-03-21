import cherrypy
from sqlalchemy import or_
from model.activity import Activity
from model.athlete import Athlete
from modules import database
from modules.transaction import commit_on_success
from modules.template import env
from modules.datatables import send_datatable_response
from modules.checkstats import check_for_completetions
from datetime import datetime
from modules.jsonable import make_jsonable

class Activities:
    @cherrypy.expose
    def index(self):
        tmpl = env.get_template('activities.html')
        return tmpl.render()

    @commit_on_success
    @check_for_completetions
    @cherrypy.expose
    def create(self, type, date, distance, duration, max_speed):
        db_session = database.session
        athlete = Athlete.query.filter_by(id = cherrypy.session.get('id')).one()
        new = Activity(athlete.id, type, datetime.strptime(date, "%d-%m-%Y"), int(distance), int(duration), max_speed)
        db_session.add(new)

    @cherrypy.tools.json_out()
    @cherrypy.expose
    def update_datatable(self, **params):
        return send_datatable_response(Activity, True, params)

    @cherrypy.tools.json_out()
    @cherrypy.expose
    def json(self, start_date, end_date):
        activities = Activity.query.filter(Activity.date.between(start_date, end_date), Activity.athlete_id == cherrypy.session.get('id')).all()
        json_data = {"activities":make_jsonable(activities)}      
        return json_data
