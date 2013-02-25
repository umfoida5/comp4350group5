import unittest
from modules import database
from model.goal import Goal
from controller.goals import Goals
from controller.activities import Activities
from model.athlete import Athlete
from datetime import datetime

class GoalsTest(unittest.TestCase):

    # TODO: make these static
    G = Goals()
    A = Activities()

    @classmethod
    def setUpClass(cls):
        database.init("tracker_test")

    def setUp(self):
        # intialize the Athlete table with known values
        database.session.add(
            Athlete(
                "Test", 
                "Athlete", 
                "test@test.com", 
                datetime.now(), 
                "I'm a Test", 
                "test street", 
                "test avatar"))
        database.session.commit()


    def test_goal_exists(self):
        # create new goal
        self.G.create(
            "run",
            "total",
            100,
            "distance",
            "20-10-2012",
            "21-10-2012")

        # grab newly created goal from db
        goal = Goal.query.first()

        # make sure it is the same
        self.assertTrue(goal.metric == "distance")
        self.assertTrue(goal.quantity == 100)
        self.assertTrue(goal.activity == "run")


    def test_goal_total_completes(self):
        # create new goal
        self.G.create(
            "run",
            "total",
            100,
            "distance",
            "20-10-2012",
            "4-10-2012")

        self.A.create(
            "run",
            "11-10-2012",
            101,
            10,
            25)

        self.A.create(
            "run",
            "11-10-2012",
            101,
            10,
            25)

        database.session.commit()

        # see if goal was completed
        goal = Goal.query.first()
        self.assertTrue(goal.completed)


    def test_goal_total_not_completes(self):
        # create new goal
        self.G.create(
            "run",
            "total",
            100,
            "distance",
            "12-12-2013",
            "30-12-2013")

        self.A.create(
            "run",
            "11-10-2012",
            50,
            10,
            25)

        self.A.create(
            "bike",
            "13-10-2012",
            70,
            10,
            25)

        # see if goal was not completed
        goal = Goal.query.first()
        self.assertFalse(goal.completed)

