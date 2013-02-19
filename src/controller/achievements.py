import cherrypy, httplib
from modules.transaction import commit_on_success
from modules.jsonable import make_jsonable
from modules.template import env
from model.athlete import Athlete
from model.achievement import Achievement, AthleteAchievements

class Achievements:

    @cherrypy.expose
    def badges(self):
        tmpl = env.get_template('achievements.html')
        return tmpl.render(achievements=Achievement.query.all())

    @cherrypy.tools.json_out()
    @cherrypy.expose
    @cherrypy.tools.allow(methods=['GET'])
    def get_athlete_achievements(self):
        athlete_achievements = (Athlete.query.get(1)).achievements
        return make_jsonable(athlete_achievements)

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
