import cherrypy
from modules.database import db_session
from model.activity import Activity
from modules.template import env

class Activities:
    @cherrypy.expose
    def index(self):
        tmpl = env.get_template('activities.html')
        return tmpl.render()

    @cherrypy.tools.json_out()
    @cherrypy.expose
    def json(self):
        response = {}
        activities = Activity.query.all()

        aaData = []
        for activity in activities:
            aaData.append((activity.distance, activity.duration))
        response['aaData'] = aaData

        return response
    
