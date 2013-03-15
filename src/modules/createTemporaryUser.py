import cherrypy
from modules import database
from modules.transaction import commit_on_success
from model.athlete import Athlete

#Creates a temporary userID in the database
#so that users can use the site without
#having to login.
@commit_on_success
def createTemporaryUser():
	if cherrypy.session.get('id') is None:
		db_session = database.session
		athlete = Athlete(None, None, "FirstName", "LastName", "Click to Edit Email", "1980-03-25", "Click to Edit", "Click to Edit Address")
		db_session.add(athlete)
		db_session.flush()
		cherrypy.session['id'] = athlete.id
		cherrypy.session['username'] = ""
	
cherrypy.tools.createTemporaryUser = cherrypy.Tool('before_handler', createTemporaryUser)
