import cherrypy, time, re
import json
from modules import database
from model.athlete import Athlete
from modules.template import env
from modules.jsonable import make_jsonable
from modules.transaction import commit_on_success
from model.achievement import Achievement, UnlockedAchievement
class Profiles:
    
    @cherrypy.expose
    def index(self):
        tmpl = env.get_template('profile.html')
        return tmpl.render()
        
    @cherrypy.tools.json_out()
    @cherrypy.expose
    def athlete(self, **kwargs):
        result = Athlete.query.filter_by(id = cherrypy.session.get('id')).one()
        print make_jsonable(result)
        return make_jsonable(result)
    
    @cherrypy.tools.json_out()
    @cherrypy.expose
    def get_unlocked_achievements(self):
        unlocked_achievements = UnlockedAchievement.query.filter_by(athlete_id=cherrypy.session.get('id')).all()
        return make_jsonable(unlocked_achievements)

    @cherrypy.tools.json_out()
    @cherrypy.expose
    @commit_on_success
    def update_about(self,id, about_msg):
        """updates the profiles about"""
        result = Athlete.query.filter_by(id = cherrypy.session.get('id')).one()
        result.about_me = about_msg
        return make_jsonable(result)

    @cherrypy.tools.json_out()
    @cherrypy.expose
    @commit_on_success
    def update_address(self, id, address):
        """update the address"""
        result = Athlete.query.filter_by(id = cherrypy.session.get('id')).one()
        result.address = address
        return make_jsonable(result)
        
    @cherrypy.tools.json_out()
    @cherrypy.expose
    @commit_on_success
    def update_dob(self, id, birth_date):
        """update the date of birth"""
        try:
            time.strptime(birth_date, '%Y-%m-%d')
        except ValueError:

            return {"birth_date" : "Expected:(YYYY-MM-DD)"}

        result = Athlete.query.filter_by(id = cherrypy.session.get('id')).one()
        result.birth_date = birth_date
        return make_jsonable(result)

    @cherrypy.tools.json_out()
    @cherrypy.expose
    @commit_on_success
    def update_email(self, id, email):
        """update the email adress"""

        if re.match(r"[^@]+@[^@]+\.[^@]+", email):
            result = Athlete.query.filter_by(id = cherrypy.session.get('id')).one()
            result.email = email
            response = make_jsonable(result)
        else:
            response = "Invalid email address"

        return response
