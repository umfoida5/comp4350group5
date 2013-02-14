import cherrypy
from sqlalchemy import or_
from modules.database import db_session
from model.athlete import Athlete
from modules.template import env
from modules.datatables import dtify

class Profiles:
    @cherrypy.expose
    def index(self):
        tmpl = env.get_template('profile.html')
        return tmpl.render()
        
