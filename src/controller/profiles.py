import cherrypy
import sys
sys.path.append('..')
from modules import database
#~ from athletes import Athletes
from model.athlete import Athlete
from modules.template import env
from modules.jsonable import make_jsonable
class Profiles:
    #~ global athlete_id = 1
    @cherrypy.expose
    def index(self):
        tmpl = env.get_template('profile.html')
        return tmpl.render()
        
    @cherrypy.tools.json_out()
    @cherrypy.expose
    def get_athlete(self, **params):
	result = Athlete.query.get(1)
	#~ return result
	return make_jsonable(result)

if(__name__ == '__main__'):
    
    database.init()
    prof = Profiles()
    res = prof.getAthlete()
    #~ print res.email
    print(res)
