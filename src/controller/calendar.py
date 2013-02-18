import cherrypy
from modules.template import env
from model.activity import Activity
from modules.jsonable import make_jsonable
class Calendar:
    @cherrypy.expose
    def index(self):
        tmpl = env.get_template('calendar_view.html')
        return tmpl.render()

    @cherrypy.tools.json_out()
    @cherrypy.expose
    @cherrypy.tools.allow(methods=['GET'])
    def get(self):
        activities = Activity.query.all()
        json_data = {"activities":make_jsonable(activities)}      
        return json_data
