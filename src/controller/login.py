import cherrypy, httplib
from modules.jsonable import make_jsonable
from modules.template import env
from modules.transaction import commit_on_success
from modules import database
from model.athlete import Athlete

class Login:
    @cherrypy.expose
    def index(self):
        tmpl = env.get_template('login.html')
        return tmpl.render()
    
    @cherrypy.expose
    def do_login(self, username, pw, just_created=False):
		#Verifies credentials for username and password.
		#Returns None on success or a string describing the error on failure.
		db_session = database.session
		
		athlete = Athlete.query.filter(Athlete.username == username).first()
		
		if athlete is not None:
			if(athlete.password == pw):
				old_id = cherrypy.session.get('id')
				cherrypy.session['id'] = athlete.id
				cherrypy.session['tempUser'] = 'false'
				
				#if just_created == False:
					#TODO - Go through every table that has an Athlete,
					#       except the Athlete table.  Modify the athlete
					#       id to be the logged in athete.id.  Then delete
					#       the Athlete with the old_id.
				return None
			else:
				return "Incorrect password."
		else:
			return "Invalid username."

    @cherrypy.expose
    def signup(self, username, pw, firstName, lastName):
		db_session = database.session
		
		#TODO, update the temp athlete information with
		#cherrypy.session.get('id').
		#Don't add a new athlete...
		#db_session.query("athletes").filter_by(id = cherrypy.session.get('id')).\
		#	update({"username":username, "password":pw, "first_name":firstName, last_name:"lastName"})
		new_athlete = Athlete(username, pw, firstName, lastName)
		db_session.add(new_athlete)
		database.session.commit()
		
		
		
		self.do_login(username, pw, True)
	
