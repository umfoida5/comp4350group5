import unittest
from datetime import datetime
from modules import database
from model.athlete import Athlete
from model.goal import Goal

class GoalTests(unittest.TestCase):	

    def setUp(self):
        database.empty_database()

    def test_goal_object_creation(self):
        athlete1 = Athlete("name1", "lastname1", "a@a.a.a", datetime.now())
        database.session.add(athlete1)
        database.session.commit()        

        goal1 = Goal(athlete1.id, "run", "total", 100, "distance",
            datetime.now(), datetime.now())
        goal2 = Goal(athlete1.id, "run", "average", 10, "max_speed",
            datetime.now(), datetime.now())

        database.session.add(goal1)
        database.session.add(goal2)
        database.session.commit()

        goals = Goal.query.all()

        self.assertTrue(len(goals) == 2)

        queried_goal1 = goals[0]
        queried_goal2 = goals[1]

        self.assertFalse(queried_goal1 is None)
        self.assertFalse(queried_goal2 is None)

        self.assertEqual(queried_goal1, goal1)
        self.assertEqual(queried_goal2, goal2)

