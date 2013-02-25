import cherrypy
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
        result = Athlete.query.first()
        return make_jsonable(result)
    
    @cherrypy.tools.json_out()
    @cherrypy.expose
    def get_unlocked_achievements(self):
        unlocked_achievements = UnlockedAchievement.query.filter_by(athlete_id=1).all()
        return make_jsonable(unlocked_achievements)

    @cherrypy.tools.json_out()
    @cherrypy.expose
    @commit_on_success
    def update_about(self,id, about_msg):
        """updates the profiles about"""
        result = Athlete.query.first()
        result.about_me = about_msg
        return make_jsonable(result)

    @cherrypy.tools.json_out()
    @cherrypy.expose
    @commit_on_success
    def update_address(self, id, address):
        """update the address"""
        result = Athlete.query.first()
        result.address = address
        return make_jsonable(result)
        
    @cherrypy.tools.json_out()
    @cherrypy.expose
    @commit_on_success
    def update_dob(self, id, birth_date):
        """update the date of birth"""
        result = Athlete.query.first()
        result.birth_date = birth_date
        return make_jsonable(result)

    @cherrypy.tools.json_out()
    @cherrypy.expose
    @commit_on_success
    def update_email(self, id, email):
        """update the email adress"""
        result = Athlete.query.first()
        result.email = email
        return make_jsonable(result)
