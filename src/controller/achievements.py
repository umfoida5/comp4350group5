import cherrypy, httplib
from modules.jsonable import make_jsonable
from modules.template import env
from model.athlete import Athlete
from model.achievement import Achievement, UnlockedAchievement

class Achievements:

    @cherrypy.expose
    def badges(self):
        tmpl = env.get_template('achievements.html')
        return tmpl.render(achievements=Achievement.query.all())

    @cherrypy.tools.json_out()
    @cherrypy.expose
    @cherrypy.tools.allow(methods=['GET'])
    def get_unlocked_achievements(self):
        unlocked_achievements = UnlockedAchievement.query.filter_by(
            athlete_id=1
        ).all()
        return make_jsonable(unlocked_achievements)
