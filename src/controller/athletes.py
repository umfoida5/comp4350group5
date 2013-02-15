import cherrypy
from sqlalchemy import or_
from modules.database import db_session
from model.athlete import Athlete
from modules.template import env
from modules.datatables import dtify

class Athletes:
    @cherrypy.expose
    def index(self):
        tmpl = env.get_template('athletes.html')
        return tmpl.render()

    @cherrypy.expose
    def new(self):
        tmpl = env.get_template('athletes_new.html')
        return tmpl.render()

    @cherrypy.expose
    def edit(self):
        tmpl = env.get_template('athletes_edit.html')
        return tmpl.render()

    @cherrypy.expose
    def view(self):
        tmpl = env.get_template('athlete_view.html')
        return tmpl.render()

    @cherrypy.tools.json_out()
    @cherrypy.expose
    def json(self, **params):
        search = '%%%s%%' % params.get('sSearch', "")
        search_filter = or_(Athlete.first_name.ilike(search), Athlete.last_name.ilike(search))

        def convert(row):
            return {"first_name": row.first_name, "last_name": row.last_name}

        return dtify(Athlete.query, search_filter, convert, params)

