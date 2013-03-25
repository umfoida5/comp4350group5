import cherrypy
from sqlalchemy import or_, asc
from model.health import Health
from model.athlete import Athlete
from modules import database
from modules.template import env
from modules.datatables import send_datatable_response
from datetime import datetime
from modules.jsonable import make_jsonable

class HealthController:
    @cherrypy.expose
    def index(self):
        tmpl = env.get_template('health.html')
        return tmpl.render()
    
    @cherrypy.expose
    def create(self, health_date, weight, resting_heart_rate, comment):
        db_session = database.session
        athlete = Athlete.query.filter_by(id = cherrypy.session.get('id')).one()
        newHealthRecord = Health(
            athlete.id, 
            datetime.strptime(health_date, "%d-%m-%Y"), 
            int(weight), 
            int(resting_heart_rate), 
            str(comment))
        db_session.add(newHealthRecord)
        db_session.commit()
    
    @cherrypy.tools.json_out()
    @cherrypy.expose
    def update_datatable(self, **params):
        return send_datatable_response(Health,True, params)
    
    @cherrypy.tools.json_out()
    @cherrypy.expose
    def json(self, start_date, end_date):
        formatted_start_date = datetime.strptime(start_date, "%d-%m-%Y")
        formatted_end_date   = datetime.strptime(end_date, "%d-%m-%Y")
        health = Health.query.filter(
            Health.health_date.between(formatted_start_date, formatted_end_date), 
            Health.athlete_id == cherrypy.session.get('id')).order_by(asc(Health.health_date)).all()
        json_data = {"health":make_jsonable(health)}      
        return json_data
