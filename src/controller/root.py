import cherrypy, httplib
from modules.template import env
from activities import Activities
from events import Events
from stats import Stats
from profiles import Profiles
from achievements import Achievements
from goals import Goals
from login import Login
from health import HealthController

class Root:
    activities = Activities()
    events = Events()
    stats = Stats()
    profiles = Profiles()
    achievements = Achievements()
    goals = Goals()
    login = Login()
    health = HealthController()

    @cherrypy.expose
    def index(self):
        tmpl = env.get_template('index.html')
        return tmpl.render()

    @cherrypy.expose
    def about(self):
        tmpl = env.get_template('about.html')
        return tmpl.render()

    @cherrypy.expose
    def get_current_username(self):
        if cherrypy.session.has_key('username'):
            return cherrypy.session.get('username')
        else:
            return ""

