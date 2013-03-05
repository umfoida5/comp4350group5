import cherrypy, httplib
from modules.jsonable import make_jsonable
from modules.template import env
from modules.transaction import commit_on_success
from modules import database
from model.athlete import Athlete
from model.achievement import UnlockedAchievement
from model.activity import Activity
from model.goal import Goal

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
		
		athlete = Athlete.query.filter_by(username = username).first()
		
		if athlete is not None:
			if(athlete.password == pw):
				old_id = cherrypy.session.get('id')
				cherrypy.session['id'] = athlete.id
				cherrypy.session['tempUser'] = 'false'
				
				if just_created == False:
					self.__update_tables_athlete_id(old_id, athlete.id)
					
				return None
			else:
				#TODO - add raise.  Currently, prevents me from sending
				#       an error response to client.
				#raise cherrypy.HTTPError(400, "Incorrect password.")
				return "Incorrect password."
		else:
			#TODO - add raise.  Currently, prevents me from sending
			#       an error response to client.
			#raise cherrypy.HTTPError(400, "Invalid username.")
			return "Invalid username."

	@cherrypy.expose
	def do_logout(self):
		db_session = database.session
		athlete = Athlete(None, None, None, None)
		db_session.add(athlete)
		db_session.commit()
		cherrypy.session['id'] = athlete.id

	@cherrypy.expose
	def signup(self, username, pw, firstName, lastName):
		db_session = database.session
		athlete = Athlete.query.filter_by(id = cherrypy.session.get('id')).one()
		athlete.username = username
		athlete.password = pw
		athlete.first_name = firstName
		athlete.last_name = lastName
		db_session.commit()
		self.do_login(username, pw, True)

	def __update_tables_athlete_id(self, old_id, new_id):
		db_session = database.session
		
		#unlocked_achievements table
		achievements = UnlockedAchievement.query.filter_by(athlete_id = old_id)
		for achievement in achievements:
			achievement.athlete_id = new_id
			
		#activities table
		activities = Activity.query.filter_by(athlete_id = old_id)
		for activity in activities:
			activity.athlete_id = new_id
			
		#goals table
		goals = Goal.query.filter_by(athlete_id = old_id)
		for goal in goals:
			goal.athlete_id = new_id
