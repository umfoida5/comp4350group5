import cherrypy
from sqlalchemy import or_
from modules.database import db_session
from model.activity import Activity
from model.athlete import Athlete
from modules.template import env
from modules.datatables import dtify

class Activities:
    @cherrypy.expose
    def index(self):
        tmpl = env.get_template('activities.html')
        return tmpl.render()

    @cherrypy.expose
    def create(self, distance, duration):
        athlete = Athlete.query.first()
        new = Activity(athlete.id, int(distance), int(duration))
        db_session.add(new)
        db_session.commit()

    @cherrypy.tools.json_out()
    @cherrypy.expose
    def json(self, **params):
        search = '%%%s%%' % params.get('sSearch', "")
        #search_filter = or_(Activity.distance.ilike(search), Activity.duration.ilike(search))
        search_filter = None

        def convert(row):
            return {"distance":row.distance, "duration":row.duration}

        return dtify(Activity.query, search_filter, convert, params)
    
