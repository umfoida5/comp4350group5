import cherrypy, httplib
from modules.template import env
from activities import Activities
from events import Events
from stats import Stats
from profiles import Profiles
from achievements import Achievements
from goals import Goals
from calendar import Calendar
from login import Login
from health import HealthController

def http_methods_allowed(methods=['GET', 'HEAD']):
    method = cherrypy.request.method.upper()
    if method not in methods:
        cherrypy.response.headers['Allow'] = ", ".join(methods)
        raise cherrypy.HTTPError(httplib.METHOD_NOT_ALLOWED)

cherrypy.tools.allow = cherrypy.Tool('on_start_resource', http_methods_allowed)

class Root:
    activities = Activities()
    events = Events()
    stats = Stats()
    profiles = Profiles()
    achievements = Achievements()
    calendar = Calendar()
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
