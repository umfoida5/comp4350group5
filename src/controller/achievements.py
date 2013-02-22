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
    def get_unlocked_achievements(self):
        athlete_id = Athlete.query.first().id
        unlocked_achievements = UnlockedAchievement.query.filter_by(
            athlete_id=athlete_id
        ).all()
        return make_jsonable(unlocked_achievements)
