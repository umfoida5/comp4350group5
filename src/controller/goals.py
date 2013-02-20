import cherrypy
from modules import database
from modules.transaction import commit_on_success
from modules.jsonable import make_jsonable
from modules.template import env
from model.athlete import Athlete
from model.goal import Goal

class Goals:
    @cherrypy.expose
    def index(self):
        tmpl = env.get_template('goals.html')
        return tmpl.render()

    @cherrypy.tools.json_out()
    @cherrypy.expose
    def get(self, goal_id=1):
        result = Goal.query.get(goal_id)

        return make_jsonable(result)

    @commit_on_success
    @cherrypy.expose
    def create(self, activity, operator, quantity, metric, start_date, end_date, recurring, parent_id=None):
        db_session = database.session
        
        athlete = Athlete.query.first()
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
    def update_datatable(self, **params):
        return send_datatable_response(Goal, params)
