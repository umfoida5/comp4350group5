import cherrypy
from modules import database
from modules.transaction import commit_on_success
from model.athlete import Athlete

#Creates a temporary userID in the database
#so that users can use the site without
#having to login.
@commit_on_success
def isloggedin():
	if cherrypy.session.get('id') is None:
		db_session = database.session
		athlete = Athlete(None, None, None, None)
		db_session.add(athlete)
		#TODO DO WHEN I GET BACK, Create DB Athlete, set session ID
	
cherrypy.tools.isloggedin = cherrypy.Tool('before_handler', isloggedin)
