import unittest
from modules import database
from model.goal import Goal
from controller.goals import Goals
from controller.activities import Activities
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
                datetime.date(1111,11,11), 
                "I'm a Test", 
                "test street", 
                "test avatar"))
        database.session.commit()


    def test_goal_exists(self):
        # create new goal
        G.create(
            "run",
            "total",
            100,
            "distance",
            datetime.date(2012,10,10),
            datetime.date(2012,10,12))

        # grab newly created goal from db
        goal = Goal.query.first()

        # make sure it is the same
        self.assertTrue(goal.metric == "distance")
        self.assertTrue(goal.quantity == 100)
        self.assertTrue(goal.activity == "run")


    def test_goal_total_completes(self):
        # create new goal
        G.create(
            "run",
            "total",
            100,
            "distance",
            datetime.date(2012,10,10),
            datetime.date(2012,10,12))

        A.create(
            "run",
            "11-10-2012",
            101,
            10,
            25)

        # see if goal was completed
        goal = Goal.query.first()
        self.assertTrue(goal.completed)


    def test_goal_total_not_completes(self):
        # create new goal
        G.create(
            "run",
            "total",
            100,
            "distance",
            datetime.date(2012,10,10),
            datetime.date(2012,10,12))

        A.create(
            "run",
            "11-10-2012",
            50,
            10,
            25)

        A.create(
            "bike",
            "11-10-2012",
            70,
            10,
            25)

        # see if goal was not completed
        goal = Goal.query.first()
        self.assertFalse(goal.completed)
