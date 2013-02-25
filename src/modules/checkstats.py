from decorator import decorator
from model.goal import Goal
from controller.statistics_engine import StatisticsEngine
from controller.goals import Goals
from modules import database

# uses stats engine to check if goals or achievements have been completed

@decorator
def check_for_completetions(f, *args, **kw):
    try:
        func = f(*args, **kw)

        database.session.commit() # save any uncommited changes in the current session

        # TODO: replace these with static method calls
        engine = StatisticsEngine()

        # 1. get a list of all the goals/achievements
        # TODO: filter by athlete_id
        goals = Goal.query.all()
        completedGoals = []

        # 2. iterate through each to check if they are complete. (keep list of completed)
        # TODO: refactor so we don't need to elif this stuff (Blake!)
        for goal in goals:
            result = None
            operator = goal.operator.lower() # for easier comparison
            if operator == "total":
                result = engine.total(
                    goal.metric,
                    goal.activity,
                    goal.athlete_id,
                    goal.start_date,
                    goal.end_date,
                    None)

            elif operator == "max":
                result = engine.maximum(
                    goal.metric,
                    goal.activity,
                    goal.athlete_id,
                    goal.start_date,
                    goal.end_date,
                    None)

            elif operator == "min":
                result = engine.minimum(
                    goal.metric,
                    goal.activity,
                    goal.athlete_id,
                    goal.start_date,
                    goal.end_date,
                    None)

            elif operator == "average":
                result = engine.average(
                    goal.metric,
                    goal.activity,
                    goal.athlete_id,
                    goal.start_date,
                    goal.end_date,
                    None)
            else:
                raise

            # did we complete the goal?
            if result[0].value >= goal.quantity:
                completedGoals.append(goal)

        # 3. update database with completed goals/achievements.
        G = Goals()        
        for goal in completedGoals:
            G.mark_completed(goal)

    except:
        raise

    return func
