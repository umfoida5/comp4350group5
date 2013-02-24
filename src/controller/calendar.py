import cherrypy
from modules.template import env
from model.activity import Activity
from model.athlete import Athlete
from modules.jsonable import make_jsonable
from modules import database
from datetime import datetime

class Calendar:
    @cherrypy.expose
    def index(self):
        tmpl = env.get_template('calendar_view.html')
        return tmpl.render()

    @cherrypy.tools.json_out()
    @cherrypy.expose
    def json(self, start_date, end_date):
        activities = Activity.query.filter(Activity.date.between(start_date, end_date)).all()
        cherrypy.response.headers["Access-Control-Allow-Origin"] = "*"
        json_data = {"activities":make_jsonable(activities)}      
        return json_data

    @cherrypy.expose
    def create(self, type, date, distance, duration, max_speed):
        db_session = database.session
        cherrypy.response.headers["Access-Control-Allow-Origin"] = "*"
        athlete = Athlete.query.first()
        new = Activity(athlete.id, type, datetime.strptime(date, "%d-%m-%Y"), int(distance), int(duration), max_speed)
        db_session.add(new)
        db_session.commit()
