import cherrypy, httplib
from sqlalchemy import and_
from modules.jsonable import make_jsonable
from modules.template import env
from modules.transaction import commit_on_success
from modules import database
from model.athlete import Athlete
from model.achievement import UnlockedAchievement
from model.activity import Activity
from model.goal import Goal
from model.health import Health

class Login:
	@cherrypy.expose
	def index(self):
		tmpl = env.get_template('login.html')
		return tmpl.render()
    
        @commit_on_success
	@cherrypy.expose
	def do_login(self, username, pw, just_created=False):
		#Verifies credentials for username and password.
		#Returns None on success or a string describing the error on failure.
		db_session = database.session
		
		athlete = Athlete.query.filter_by(username = username).first()
		
		if athlete is not None:
			if(athlete.password == pw):				
				if not just_created:
					old_id = cherrypy.session.get('id')

                                        if not cherrypy.session.has_key('username'):
					    self.__update_tables_athlete_id(old_id, athlete.id)
                                            Athlete.query.filter(and_(
                                                Athlete.id == old_id,
                                                Athlete.username == None
                                            )).delete(False)

					cherrypy.session['id'] = athlete.id
					cherrypy.session['username'] = athlete.username
					
				return "Login was successful." 
			else:
				return "Incorrect password."
		else:
			return "Invalid username."

	@commit_on_success 
	@cherrypy.expose
	def do_logout(self):
		db_session = database.session
		athlete = Athlete(None, None, "FirstName", "LastName")
		db_session.add(athlete)
		db_session.flush()
		cherrypy.session['id'] = athlete.id
		cherrypy.session.pop('username')
		
		return "Logout was successful."

	@commit_on_success 
	@cherrypy.expose
	def signup(self, username, pw, firstName, lastName):
		db_session = database.session
		return_message = "Username already exists. Please enter a new username."

                if len(username) <= 3:
                    return "Username must be longer than 3 characters"
                elif len(pw) <= 3:
                    return "Password must be longer than 3 characters"
		
		if Athlete.query.filter_by(username=username).all() == []:
			cherrypy.session['username'] = username
			
			athlete = Athlete.query.filter_by(id = cherrypy.session.get('id')).one()
			athlete.username = username
			athlete.password = pw
			athlete.first_name = firstName
			athlete.last_name = lastName
			db_session.flush()
			return_message = self.do_login(username, pw, True)    
		
		return return_message

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
			
		#health table
		healthRecords = Health.query.filter_by(athlete_id = old_id)
		for health in healthRecords:
			health.athlete_id = new_id

                db_session.flush()

