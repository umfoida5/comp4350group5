import cherrypy
import sys
sys.path.append('..')
from modules import database
#~ from athletes import Athletes
from model.athlete import Athlete
from modules.template import env
from modules.jsonable import make_jsonable
from modules.transaction import commit_on_success
import simplejson
class Profiles:
    #~ global athlete_id = 1
    @cherrypy.expose
    def index(self):
        tmpl = env.get_template('profile.html')
        return tmpl.render()
        
    @cherrypy.tools.allow(methods=['GET'])
    @cherrypy.tools.json_out()
    @cherrypy.expose
    def athlete(self, **kwargs):
        result = Athlete.query.get(1)
        
        return make_jsonable(result)
    
    @cherrypy.tools.json_out()
    @cherrypy.tools.allow(methods=['POST'])
    @cherrypy.expose
    @commit_on_success
    def update_about(self,id, about_msg):
        """updates the profiles about"""
        result = Athlete.query.get(1)
        result.about_me = about_msg
        return make_jsonable(result)
        

    @cherrypy.tools.json_out()
    @cherrypy.tools.allow(methods=['POST'])
    @cherrypy.expose
    @commit_on_success
    def update_address(self, id, address):
        """update the address"""
        result = Athlete.query.get(1)
        result.address = address
        return make_jsonable(result)
        
    @cherrypy.tools.json_out()
    @cherrypy.tools.allow(methods=['POST'])
    @cherrypy.expose
    @commit_on_success
    def update_dob(sef, id, birth_date):
        """update the date of birth"""
        result = Athlete.query.get(1)
        result.birth_date = birth_date
        return make_jsonable(result)

    @cherrypy.tools.json_out()
    @cherrypy.tools.allow(methods=['POST'])
    @cherrypy.expose
    @commit_on_success
    def update_email(self, id, email):
        """update the email adress"""
        result = Athlete.query.get(1)
        result.email = email
        return make_jsonable(result)
        
if(__name__ == '__main__'):
    
    database.init()
    prof = Profiles()
    res = prof.getAthlete()
    #~ print res.email
    print(res)
