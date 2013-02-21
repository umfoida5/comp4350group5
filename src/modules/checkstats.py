from decorator import decorator
from controller.statistics_engine import StatisticsEngine
from controller.goals import Goals
from modules import database

# uses stats engine to check if goals or achievements have been completed

@decorator
def check_for_completetions(f, *args, **kw):
    try:
        func = f(*args, **kw)

        # TODO: replace these with static method calls
        engine = StatisticsEngine()
        g = Goals()

        # 1. get a list of all the goals/achievements (filter by athlete_id?)
        # TODO: replace with static method call
        goals = g.get()
        completedGoals = []

        # 2. iterate through each to check if they are complete. (keep list of completed)
        for goal in goals:
            result = None
            # TODO: refactor so we don't need to elif this stuff
            operator = goal.operator
            if operator == "total":
                result = engine.total(
                    goal.metric,
                    goal.activity,
                    goal.start_date,
                    goal.end_date)
                if result[0].sum >= goal.quantity:
                    completedGoals.append(goal)

            elif operator == "max":
                pass
            elif operator == "min":
                pass
            elif operator == "average":
                pass

        # 3. update database with completed goals/achievements.
        for goal in completedGoals:
            g.mark_completed(goal)

     except:
         raise

     return func
