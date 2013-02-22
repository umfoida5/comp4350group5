import unittest
from modules import database
from model.goal import Goal
from controller.goals import Goals

class GoalsTest(unittest.TestCase):

	test_goal = None

    @classmethod
    def setUpClass(cls):
        database.init("tracker_test")

    def setUp(self):
        """
        This method is run before tests to provide setup
        """

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

        da

        # intialize the Goal table with known values
        database.session.add(
            Goal(self.,
                "run",
                "total",
                100,
                "distance",
                datetime.strptime("22-10-2012", "%d-%m-%Y"),
                datetime.strptime("22-13-2012", "%d-%m-%Y"),
                False,
                None))

        database.session.commit()
        self.test_goal = Goal.query.filter_by(goal_id = 1).first()

        # initialize the Activity table with known values
        for num in range(1, 4):

            database.session.add(            
                Activity(
                    self.test_athlete.id, 
                    "run",
                    datetime.date(1111, num, num),                    
                    num * 10, 
                    num * 5, 
                    num * 10))

            database.session.add(            
                Activity(
                    self.test_athlete.id, 
                    "run",
                    datetime.date(2222, num, num),                    
                    num * 10, 
                    num * 5, 
                    num * 10))

            database.session.add(
                Activity(
                    self.test_athlete.id, 
                    "bike",
                    datetime.date(1111, num, num),                    
                    num * 10, 
                    num * 5, 
                    num * 10))

            database.session.add(
                Activity(
                    self.test_athlete.id, 
                    "bike",
                    datetime.date(2222, num, num),                    
                    num * 10, 
                    num * 5, 
                    num * 10))

        database.session.commit()


    def test_goal_exists(self):
      	pass


    def test_goal_completes(self):

        # add goal to goals using functions

        # call the activities table add goal function with some parameters

        # test to see if goal was completed

    	pass


    def test_goal_does_not_complete(self):

        # similar to above, but make sure goal doesn't complete.

    	pass
