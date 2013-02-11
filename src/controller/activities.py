import cherrypy
from sqlalchemy import or_
from modules.database import db_session
from model.activity import Activity
from modules.template import env
from modules.datatables import dtify

class Activities:
    @cherrypy.expose
    def index(self):
        tmpl = env.get_template('activities.html')
        return tmpl.render()

    @cherrypy.expose
    def new(self):
        tmpl = env.get_template('activities_new.html')
        return tmpl.render()

    @cherrypy.expose
    def edit(self):
        tmpl = env.get_template('activities_edit.html')
        return tmpl.render()

    @cherrypy.expose
    def view(self):
        tmpl = env.get_template('activity_view.html')
        return tmpl.render()

    @cherrypy.tools.json_out()
    @cherrypy.expose
    def json(self, **params):
        search = '%%%s%%' % params['sSearch']
        #search_filter = or_(Activity.distance.like(search), Activity.duration.like(search))
        search_filter = None

        def convert(row):
            return (row.distance, row.duration)

        return dtify(Activity.query, search_filter, convert, params)
    
