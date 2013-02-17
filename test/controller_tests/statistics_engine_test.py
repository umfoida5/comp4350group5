import unittest
from modules import database
from controller.statistics_engine import StatisticsEngine
from sqlalchemy import Column, Integer, ForeignKey, Table
from model.activity import Activity
from model.athlete import Athlete
import datetime 

class StatisticsEngineTest(unittest.TestCase):

    statseng = StatisticsEngine()
    test_athlete = None
 
    def setUp(self):
        """
        This method is run before tests to provide setup
        """
        database.init("tracker_test")      
        stats_eng = StatisticsEngine() 

        # cleans athletes and activities table
        Activity.query.delete()
        Athlete.query.delete()

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
        self.test_athlete = Athlete.query.filter_by(first_name = "Test").first()

        # initialize the Activity table with known values
        for num in range(1, 4):

            database.session.add(            
                Activity(
                    self.test_athlete.id, 
                    "run",
                    datetime.date(1111, num, num),                    
                    num * 10, 
                    num * 10, 
                    num * 10))

            database.session.add(            
                Activity(
                    self.test_athlete.id, 
                    "run",
                    datetime.date(1111, num, num),                    
                    num * 10, 
                    num * 10, 
                    num * 10))

            database.session.add(
                Activity(
                    self.test_athlete.id, 
                    "ride",
                    datetime.date(1111, num, num),                    
                    num * 10, 
                    num * 10, 
                    num * 10))

            database.session.add(
                Activity(
                    self.test_athlete.id, 
                    "ride",
                    datetime.date(1111, num, num),                    
                    num * 10, 
                    num * 10, 
                    num * 10))

        database.session.commit()
        

    def tearDown(self):
        """
        This method is run before tests to provide setup
        """

    '''
    Test the group_by statistical aggregation for each method by
    day, month and year groupings
    '''
        
    def test_total_distance_groupbyyear(self):
        """
        """

        result = self.statseng.total(
            "distance",
            "run", 
            self.test_athlete.id,
            datetime.date(1000,01,01),
            datetime.date(3000,01,01),
            "year")

        self.assertTrue(len(result) == 1)
        self.assertTrue(result[0].sum == 120)


    def test_total_distance_groupbymonth(self):
        """
        """

        result = self.statseng.total(
            "distance",
            "run", 
            self.test_athlete.id,
            datetime.date(1000,01,01),
            datetime.date(3000,01,01),
            "month")

        self.assertTrue(len(result) == 3)
        for num in range(0,len(result)):        
            self.assertTrue(result[num].sum == result[num].month * 20)

    def test_total_distance_groupbyday(self):
        """
        """

        result = self.statseng.total(
            "distance",
            "run", 
            self.test_athlete.id,
            datetime.date(1000,01,01),
            datetime.date(3000,01,01),
            "day")

        self.assertTrue(len(result) == 3)
        for num in range(0,len(result)):        
            self.assertTrue(result[num].sum == result[num].day * 20)

    def test_avg_distance_groupbyyear(self):
        """
        """

        result = self.statseng.average(
            "distance",
            "run", 
            self.test_athlete.id,
            datetime.date(1000,01,01),
            datetime.date(3000,01,01),
            "year")

        self.assertTrue(len(result) == 1)
        self.assertTrue(result[0].avg == 20)

    def test_avg_distance_groupbymonth(self):
        """
        """

        result = self.statseng.average(
            "distance",
            "run", 
            self.test_athlete.id,
            datetime.date(1000,01,01),
            datetime.date(3000,01,01),
            "month")

        self.assertTrue(len(result) == 3)
        for num in range(0,len(result)):        
            self.assertTrue(result[num].avg == result[num].month * 10)

    def test_avg_distance_groupbyday(self):
        """
        """

        result = self.statseng.average(
            "distance",
            "run", 
            self.test_athlete.id,
            datetime.date(1000,01,01),
            datetime.date(3000,01,01),
            "day")

        self.assertTrue(len(result) == 3)
        for num in range(0,len(result)):        
            self.assertTrue(result[num].avg == result[num].day * 10)

    def test_max_distance_groupbyyear(self):
        """
        """

        result = self.statseng.maximum(
            "distance",
            "run", 
            self.test_athlete.id,
            datetime.date(1000,01,01),
            datetime.date(3000,01,01),
            "year")

        self.assertTrue(len(result) == 1)
        self.assertTrue(result[0].max == 30)

    def test_max_distance_groupbymonth(self):
        """
        """

        result = self.statseng.maximum(
            "distance",
            "run", 
            self.test_athlete.id,
            datetime.date(1000,01,01),
            datetime.date(3000,01,01),
            "month")

        self.assertTrue(len(result) == 3)
        for num in range(0,len(result)):        
            self.assertTrue(result[num].max == result[num].month * 10)

    def test_max_distance_groupbyday(self):
        """
        """

        result = self.statseng.maximum(
            "distance",
            "run", 
            self.test_athlete.id,
            datetime.date(1000,01,01),
            datetime.date(3000,01,01),
            "day")

        self.assertTrue(len(result) == 3)
        for num in range(0,len(result)):        
            self.assertTrue(result[num].max == result[num].day * 10)

    def test_min_distance_groupbyyear(self):
        """
        """

        result = self.statseng.minimum(
            "distance",
            "run", 
            self.test_athlete.id,
            datetime.date(1000,01,01),
            datetime.date(3000,01,01),
            "year")

        self.assertTrue(len(result) == 1)
        self.assertTrue(result[0].min == 10)

    def test_min_distance_groupbymonth(self):
        """
        """

        result = self.statseng.minimum(
            "distance",
            "run", 
            self.test_athlete.id,
            datetime.date(1000,01,01),
            datetime.date(3000,01,01),
            "month")

        self.assertTrue(len(result) == 3)
        for num in range(0,len(result)):        
            self.assertTrue(result[num].min == result[num].month * 10)

    def test_min_distance_groupbyday(self):
        """
        """

        result = self.statseng.minimum(
            "distance",
            "run", 
            self.test_athlete.id,
            datetime.date(1000,01,01),
            datetime.date(3000,01,01),
            "day")

        self.assertTrue(len(result) == 3)
        for num in range(0,len(result)):        
            self.assertTrue(result[num].min == result[num].day * 10)

    def test_count_distance_groupbyyear(self):
        """
        """

        result = self.statseng.count(
            "distance",
            "run", 
            self.test_athlete.id,
            datetime.date(1000,01,01),
            datetime.date(3000,01,01),
            "year")

        self.assertTrue(len(result) == 1)
        self.assertTrue(result[0].count == 6)

    def test_count_distance_groupbymonth(self):
        """
        """

        result = self.statseng.count(
            "distance",
            "run", 
            self.test_athlete.id,
            datetime.date(1000,01,01),
            datetime.date(3000,01,01),
            "month")

        self.assertTrue(len(result) == 3)
        for num in range(0,len(result)):        
            self.assertTrue(result[num].count == 2)

    def test_count_distance_groupbyday(self):
        """
        """

        result = self.statseng.count(
            "distance",
            "run", 
            self.test_athlete.id,
            datetime.date(1000,01,01),
            datetime.date(3000,01,01),
            "day")

        self.assertTrue(len(result) == 3)
        for num in range(0,len(result)):        
            self.assertTrue(result[num].count == 2)
