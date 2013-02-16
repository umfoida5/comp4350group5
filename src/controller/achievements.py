import cherrypy, httplib, json
from modules.transaction import commit_on_success
from modules.jsonable import make_jsonable
from modules.template import env
from model.athlete import Athlete
from model.achievement import Achievement

class Achievements:
    @cherrypy.tools.json_out()
    @cherrypy.expose
    def get_all(self):
        achievements = Achievement.query.all()
        json_data = make_jsonable(achievements)
        return json_data

    @cherrypy.tools.json_out()
    @commit_on_success
    @cherrypy.expose
    def unlock(self, athlete_id, achievement_id): #Should only accept POST
        athlete = Athlete.query.get(athlete_id)
        achievement = Achievement.query.get(achievement_id)
        if athlete != None and achievement != None:
            athlete.achievements.append(achievement)
            cherrypy.response.status = httplib.NO_CONTENT
        else:
            cherrypy.response.status = httplib.NOT_FOUND
