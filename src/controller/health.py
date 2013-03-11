import cherrypy
from sqlalchemy import or_
from model.health import Health
from model.athlete import Athlete
from modules import database
from modules.template import env
from modules.datatables import send_datatable_response
from datetime import datetime

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
    
