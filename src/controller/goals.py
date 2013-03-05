import cherrypy
from modules import database
from modules.transaction import commit_on_success
from modules.jsonable import make_jsonable
from modules.template import env
from modules.datatables import send_datatable_response
from model.athlete import Athlete
from model.goal import Goal
from datetime import datetime

class Goals:
    @cherrypy.expose
    def index(self):
        tmpl = env.get_template('goals.html')
        return tmpl.render()

    def get(self, goal_id=None):
        result = database.session.query(
            Goal.goal_id,
            Goal.athlete_id,
            Goal.quantity,
            Goal.operator,
            Goal.metric,
            Goal.activity,
            Goal.start_date,
            Goal.end_date)
        if goal_id is not None:
            result = result.filter(Goal.goal_id == goal_id)

        return result.all()

    @cherrypy.tools.json_out()
    @cherrypy.expose
    def get_json(self, goal_id=None):
        return make_jsonable(self.get(goal_id))

    @cherrypy.expose
    @commit_on_success
    def create(self, activity, operator, quantity, metric, start_date, end_date, recurring=False, parent_id=None):
        db_session = database.session

        athlete = Athlete.query.filter_by(id = cherrypy.session.get('id')).one()
        new = Goal(athlete.id,
            str(activity),
            str(operator),
            str(quantity),
            str(metric),
            datetime.strptime(start_date, "%d-%m-%Y"),
            datetime.strptime(end_date, "%d-%m-%Y"),
            bool(recurring),
            parent_id)

        db_session.add(new)

    @cherrypy.tools.json_out()
    @cherrypy.expose
    @commit_on_success
    def mark_completed(self, goal):
        result = Goal.query.get(goal.goal_id)
        result.completed = True

        #database.session.add(result)
        #return make_jsonable(result)
        
    @cherrypy.tools.json_out()
    @cherrypy.expose
    def update_datatable(self, **params):
        return send_datatable_response(Goal, params)
