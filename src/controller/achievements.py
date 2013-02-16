import cherrypy, httplib
from modules.transaction import commit_on_success
from modules.jsonable import make_jsonable
from model.athlete import Athlete
from model.achievement import Achievement

class Achievements:
    @cherrypy.tools.json_out()
    @cherrypy.expose
    @cherrypy.tools.allow(methods=['GET'])
    def get_all(self):
        achievements = Achievement.query.all()
        json_data = {"achievements":make_jsonable(achievements)}
        return json_data

    @cherrypy.tools.json_out()
    @cherrypy.expose
    @commit_on_success
    @cherrypy.tools.allow(methods=['POST'])
    def unlock(self, athlete_id, achievement_id):
        athlete = Athlete.query.get(athlete_id)
        achievement = Achievement.query.get(achievement_id)
        if athlete != None and achievement != None:
            athlete.achievements.append(achievement)
            cherrypy.response.status = httplib.NO_CONTENT
        else:
            raise cherrypy.HTTPError(httplib.NOT_FOUND)
