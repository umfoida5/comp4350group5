import cherrypy
from modules.template import env
from model.activity import Activity
from modules.jsonable import make_jsonable
import datetime

class Calendar:
    @cherrypy.expose
    def index(self):
        tmpl = env.get_template('calendar_view.html')
        return tmpl.render()

    @cherrypy.tools.json_out()
    @cherrypy.expose
    @cherrypy.tools.allow(methods=['GET'])
    def get(self, **args):
        if (len(args) >= 2):
            activities = Activity.query.filter(Activity.date.between(args["start_date"], args["end_date"])).all()
        else:
            activities = Activity.query.all()

        json_data = {"activities":make_jsonable(activities)}      
        return json_data
