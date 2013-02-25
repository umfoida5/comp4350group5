import unittest
from datetime import datetime
from modules import database
from model.athlete import Athlete
from model.goal import Goal

class GoalTests(unittest.TestCase):	

    @classmethod
    def setUpClass(cls):
        database.init("tracker_test")

    def setUp(self):
        database.empty_database()

    def test_goal_object_creation(self):
        athlete1 = Athlete("name1", "lastname1", "a@a.a.a", datetime.now())
        database.session.add(athlete1)
        database.session.commit()        

        athlete1 = Athlete.query.filter_by(first_name = "name1").first()
        
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

        self.assertIsNotNone(queried_goal1)
        self.assertIsNotNone(queried_goal2)

        self.assertEqual(queried_goal1, goal1)
        self.assertEqual(queried_goal2, goal2)

if(__name__ == '__main__'):
    unittest.main()

