import cherrypy
from jinja2 import Environment, FileSystemLoader
from workouts import Workouts
env = Environment(loader=FileSystemLoader('view/web/templates'))

class Root:
    workouts = Workouts()

    @cherrypy.expose
    def index(self):
        tmpl = env.get_template('index.html')
        return tmpl.render()

    @cherrypy.expose
    def about(self):
        tmpl = env.get_template('about.html')
        return tmpl.render()


