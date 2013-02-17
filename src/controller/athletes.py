import cherrypy
from sqlalchemy import or_
import sys
sys.path.append('..')
from model.athlete import Athlete
from modules.template import env
from modules.datatables import send_datatable_response

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
    def update_datatable(self, **params):
        search = '%%%s%%' % params.get('sSearch', "")
        search_filter = or_(
            Athlete.first_name.ilike(search),
            Athlete.last_name.ilike(search)
        )
        return send_datatable_response(Athlete.query, search_filter, params)
        
    @cherrypy.tools.json_out()
    @cherrypy.expose
    def getAthlete(self, **params):
		#~ get_filter = Athlete.id ==
		def convert(row):
			return {"first_name": row.first_name, "last_name": row.last_name}
		return dtify(Athlete.query, get_filter, convert, params)
		
if(__name__ == '__main__'):
	ath = Athletes()
	print(ath.getAthlete())
	
