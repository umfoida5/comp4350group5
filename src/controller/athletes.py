import cherrypy
from sqlalchemy import or_
from modules.database import db_session
from model.athlete import Athlete
from modules.template import env

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
        response = {'sEcho': int(params['sEcho'])}

        search = '%%%s%%' % params['sSearch']
        athletes_filter = Athlete.query.filter(or_(Athlete.first_name.like(search), Athlete.last_name.like(search)))

        response['iTotalRecords'] = Athlete.query.count()
        response['iTotalDisplayRecords'] = athletes_filter.count()

        athletes = athletes_filter.limit(params['iDisplayLength']).offset(params['iDisplayStart']).all()

        aaData = []
        for athlete in athletes:
            aaData.append((athlete.first_name, athlete.last_name))
        response['aaData'] = aaData

        return response
    
