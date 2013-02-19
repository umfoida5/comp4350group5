import cherrypy
import sys
sys.path.append('..')
from modules import database
#~ from athletes import Athletes
from model.athlete import Athlete
from modules.template import env
from modules.jsonable import make_jsonable
from hashlib import md5
class Profiles:
    #~ global athlete_id = 1
    @cherrypy.expose
    def index(self):
        tmpl = env.get_template('profile.html')
        return tmpl.render()
        
    @cherrypy.tools.json_out()
    @cherrypy.expose
    def get_athlete(self, **kwargs):
	result = Athlete.query.get(1)
	#~ return result
	return make_jsonable(result)
    
    @cherrypy.tools.json_in()
    @cherrypy.expose
    def update_about(self, msg):
        """updates the profiles about"""

    @cherrypy.tools.json_in()
    @cherrypy.expose
    def update_address(self, **kwargs):
        """update the address"""
        
    @cherrypy.tools.json_in()
    @cherrypy.expose
    def update_dob(sef, **kwargs):
        """update the date of birth"""

    @cherrypy.tools.json_in()
    @cherrypy.expose
    def update_email(self, **kwargs):
        """update the email adress"""
        
if(__name__ == '__main__'):
    
    database.init()
    prof = Profiles()
    res = prof.getAthlete()
    #~ print res.email
    print(res)
