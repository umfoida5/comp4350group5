import unittest
import sys
sys.path.append('../../src')
from modules import database
from model.activity import Activity
from model.athlete import Athlete
from controller.goals import Goals
from controller.activities import Activities
from controller.statistics_engine import StatisticsEngine
from controller.stats import Stats
from datetime import datetime


class StatsTest(unittest.TestCase):

    mySE = StatisticsEngine()

    @classmethod
    def setUpClass(cls):
        database.init("tracker_test")
	
    def setUp(self):
	database.empty_database()
	    
	# intialize the Athlete table with known values
	database.session.add(
	Athlete(
        "username",
        "password",
	    "Test", 
	    "Athlete", 
	    "test@test.com", 
	    "1111-11-11", 
	    "I'm a Test", 
	    "test street", 
	    "test avatar"))

	database.session.commit()
        self.test_athlete = Athlete.query.filter_by(first_name = "Test").first()
        
        # initialize the Activity table with known values
	for num in range(1, 4):
	
	    database.session.add(            
	        Activity(
	            self.test_athlete.id, 
	            "Run",
	            "1-1-1",                    
	            num * 10, 
	            num * 10, 
	            num * 10))
	
        database.session.commit()
        
    def test_function_calls(self):
    	self.testTotal = StatisticsEngine.total(StatsTest.mySE, "distance","Run",self.test_athlete.id,"1-1-1","1-1-1",None)
    	self.testAvg = StatisticsEngine.average(StatsTest.mySE, "distance","Run",self.test_athlete.id,"1-1-1","1-1-1",None)
    	self.testMin = StatisticsEngine.minimum(StatsTest.mySE, "distance","Run",self.test_athlete.id,"1-1-1","1-1-1",None)
    	self.testMax = StatisticsEngine.maximum(StatsTest.mySE, "distance","Run",self.test_athlete.id,"1-1-1","1-1-1",None)
    	
    	self.assertTrue("60" in str(self.testTotal))
    	self.assertTrue("20" in str(self.testAvg))
    	self.assertTrue("10" in str(self.testMin))
    	self.assertTrue("30" in str(self.testMax))
