import cherrypy, httplib
from modules.transaction import commit_on_success
from modules.jsonable import make_jsonable
from modules.template import env
from model.athlete import Athlete
from model.achievement import Achievement, UnlockedAchievement

class Achievements:

    @cherrypy.expose
    def badges(self):
        tmpl = env.get_template('achievements.html')
        return tmpl.render()

    @cherrypy.tools.json_out()
    @cherrypy.expose
    def get_unlocked_achievements(self):
        unlocked_achievements = []
        athlete = Athlete.query.first()

        if athlete is not None:
            unlocked_achievements = UnlockedAchievement.query.filter_by(
                athlete_id=athlete.id
            ).all()
            
        return make_jsonable(unlocked_achievements)

    @cherrypy.tools.json_out()
    @cherrypy.expose
    def get_achievements(self):
        achievements = Achievement.query.all()
        return make_jsonable(achievements)      

    @commit_on_success
    def unlock(self, achievement):
        athlete = Athlete.query.first()
        if athlete != None and achievement != None:
            athlete.achievements.append(achievement)
