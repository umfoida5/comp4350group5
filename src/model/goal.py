from sqlalchemy import Column, ForeignKey, Integer, String, Boolean, Float, DateTime
from modules.database import Base
from modules.jsonable import Jsonable
from datetime import datetime

# defining base Goal object, so athletes can set goals for themselves.

@Jsonable('activity', 'operator', 'quantity', 'metric', 'start_date', 'end_date', 'completed')
class Goal(Base):
    __tablename__ = 'goals'
    goal_id = Column(
        Integer,
        primary_key=True) # unqiue id
    
    athlete_id = Column(
        Integer,
        nullable=False) # owner athlete id

    activity = Column(
    	String(32),
        ForeignKey("activity_types.name"),
        nullable=False) # Eg. run, bike
    
    operator = Column(
    	String(32),
        ForeignKey("operator_types.name"),
        nullable=False) # Eg. average, total

    quantity = Column(
    	Float,
        nullable=False) # quantity of metric
    
    metric = Column(
        String(32),
        ForeignKey("metric_types.name"),
        nullable=False) # Eg. km

    start_date = Column(
        DateTime,
        default=datetime.now()) # start date of goal

    end_date = Column(
    	DateTime,
    	default=datetime.now()) # end date for goal (due date)

    completed = Column(Boolean,
        nullable=False,
        default=False) # was this goal completed on time?

    recurring = Column(Boolean,
        nullable=False,
        default=False) # does this goal recur over time?

    parent_id = Column(Integer) # for recurring goals ONLY; parent id is the original goal id

    def __init__(self, activity, operator, quantity, metric,
    	start_date, end_date, recurring, parent_id=None
    ):
        self.activity = activity
        self.operator = operator
        self.quantity = quantity
        self.metric = metric
        self.start_date = start_date
        self.end_date = end_date
        self.recurring = recurring
        self.parent_id = parent_id

    def __repr__(self):
        return '<Goal %r %r %r %r %r %r %r>' % (
            self.activity, self.operator, self.quantity, self.metric,
            self.start_date, self.end_date, self.completed)
