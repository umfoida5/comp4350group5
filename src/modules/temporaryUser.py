import cherrypy
from modules import database
from modules.transaction import commit_on_success
from model.athlete import Athlete
from sqlalchemy import and_

#Creates a temporary userID in the database
#so that users can use the site without
#having to login.
@commit_on_success
def createTemporaryUser():
	if cherrypy.session.get('id') is None:
		db_session = database.session
		athlete = Athlete(None, None, "FirstName", "LastName", "", None, "", "")
		db_session.add(athlete)
		db_session.flush()
		cherrypy.session['id'] = athlete.id
	
cherrypy.tools.createTemporaryUser = cherrypy.Tool('before_handler', createTemporaryUser)

@commit_on_success
def expire(id):
    Athlete.query.filter(and_(Athlete.id == id, Athlete.username == None)).delete()

@commit_on_success
def expireAll():
    Athlete.query.filter(Athlete.username == None).delete()

