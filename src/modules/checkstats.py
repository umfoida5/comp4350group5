from decorator import decorator
from model.goal import Goal
from model.athlete import Athlete
from model.achievement import Achievement
from controller.achievements import Achievements
from controller.statistics_engine import StatisticsEngine
from controller.goals import Goals
from modules import database

# uses stats engine to check if goals or achievements have been completed

@decorator
def check_for_completetions(f, *args, **kw):
    try:
        func = f(*args, **kw)

        database.session.commit() # save any uncommited changes in the current session

        # 1. get a list of all the goals/achievements
        # TODO: filter by athlete_id
        athlete = Athlete.query.first()
        goals = Goal.query.all()
        locked_achievements = get_list_of_locked_achievements(athlete)

        # 2. iterate through each to check if they are complete. (keep list of completed)
        # TODO: refactor so we don't need to elif this stuff (Blake!)
        completedGoals = get_completed(goals, athlete.id)
        completedAchievements = get_completed(locked_achievements, athlete.id)

        # 3. update database with completed goals/achievements.
        G = Goals()        
        for goal in completedGoals:
            G.mark_completed(goal)

        achievements_controller = Achievements()
        for achievement in completedAchievements:
            achievements_controller.unlock(athlete, achievement)

    except:
        raise

    return func

def get_list_of_locked_achievements(athlete):
    achievements = Achievement.query.all()
    unlocked_achievements = athlete.achievements
    achievement_ids = [ achievement.id for achievement in unlocked_achievements ]
    locked_achievements = [ achievement for achievement in achievements if achievement.id not in achievement_ids ]
    return locked_achievements


def get_completed(the_list, athlete_id):
    # TODO: replace these with static method calls
    engine = StatisticsEngine()    
    completed = []

    for element in the_list:
        result = None
        operator = element.operator.lower() # for easier comparison
        if operator == "total":
            result = engine.total(
                element.metric,
                element.activity,
                athlete_id,
                element.start_date,
                element.end_date,
                None
            )

        elif operator == "max":
            result = engine.maximum(
                element.metric,
                element.activity,
                athlete_id,
                element.start_date,
                element.end_date,
                None
            )

        elif operator == "min":
            result = engine.minimum(
                element.metric,
                element.activity,
                athlete_id,
                element.start_date,
                element.end_date,
                None
            )

        elif operator == "average":
            result = engine.average(
                element.metric,
                element.activity,
                athlete_id,
                element.start_date,
                element.end_date,
                None
            )
        else:
            raise

        # did we complete the element?
        if result[0].value >= element.quantity:
            completed.append(element)

    return completed
