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
 
    @classmethod
    def setUpClass(cls):
        database.init("tracker_test")

    def setUp(self):
        """
        This method is run before tests to provide setup
        """  
        stats_eng = StatisticsEngine() 

        database.empty_database()

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
                    "ride",
                    datetime.date(1111, num, num),                    
                    num * 10, 
                    num * 5, 
                    num * 10))

            database.session.add(
                Activity(
                    self.test_athlete.id, 
                    "ride",
                    datetime.date(2222, num, num),                    
                    num * 10, 
                    num * 5, 
                    num * 10))

        database.session.commit()
        
    '''
    Test the group_by statistical aggregation for each method by
    day, month and year groupings
    '''

    def test_total_distance(self):
        """
        """

        result = self.statseng.total(
            "distance",
            "run", 
            self.test_athlete.id,
            datetime.date(1000,01,01),
            datetime.date(3000,01,01),
            None)

        self.assertTrue(len(result) == 1)
        self.assertTrue(result[0].value == 120)

    def test_total_duration(self):
        """
        """

        result = self.statseng.total(
            "duration",
            "run", 
            self.test_athlete.id,
            datetime.date(1000,01,01),
            datetime.date(3000,01,01),
            None)

        self.assertTrue(len(result) == 1)
        self.assertTrue(result[0].value == 60)

    def test_total_ride(self):
        """
        """

        result = self.statseng.total(
            "distance",
            "ride", 
            self.test_athlete.id,
            datetime.date(1000,01,01),
            datetime.date(3000,01,01),
            None)

        self.assertTrue(len(result) == 1)
        self.assertTrue(result[0].value == 120)

    def test_total_run(self):
        """
        """

        result = self.statseng.total(
            "distance",
            "ride", 
            self.test_athlete.id,
            datetime.date(1000,01,01),
            datetime.date(3000,01,01),
            None)

        self.assertTrue(len(result) == 1)
        self.assertTrue(result[0].value == 120)
        
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

        self.assertTrue(len(result) == 2)
        self.assertTrue(result[0].value == 60)
        self.assertTrue(result[1].value == 60)


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

        self.assertTrue(len(result) == 6)
        for num in range(0,len(result)):        
            self.assertTrue(result[num].value == result[num].month * 10)

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

        self.assertTrue(len(result) == 6)
        for num in range(0,len(result)):        
            self.assertTrue(result[num].value == result[num].day * 10)

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

        self.assertTrue(len(result) == 2)
        self.assertTrue(result[0].value == 20)
        self.assertTrue(result[1].value == 20)

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

        self.assertTrue(len(result) == 6)
        for num in range(0,len(result)):        
            self.assertTrue(result[num].value == result[num].month * 10)

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

        self.assertTrue(len(result) == 6)
        for num in range(0,len(result)):        
            self.assertTrue(result[num].value == result[num].day * 10)

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

        self.assertTrue(len(result) == 2)
        self.assertTrue(result[0].value == 30)
        self.assertTrue(result[1].value == 30)

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

        self.assertTrue(len(result) == 6)
        for num in range(0,len(result)):        
            self.assertTrue(result[num].value == result[num].month * 10)

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

        self.assertTrue(len(result) == 6)
        for num in range(0,len(result)):        
            self.assertTrue(result[num].value == result[num].day * 10)

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

        self.assertTrue(len(result) == 2)
        self.assertTrue(result[0].value == 10)
        self.assertTrue(result[1].value == 10)

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

        self.assertTrue(len(result) == 6)
        for num in range(0,len(result)):        
            self.assertTrue(result[num].value == result[num].month * 10)

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

        self.assertTrue(len(result) == 6)
        for num in range(0,len(result)):        
            self.assertTrue(result[num].value == result[num].day * 10)

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

        self.assertTrue(len(result) == 2)
        self.assertTrue(result[0].value == 3)
        self.assertTrue(result[1].value == 3)

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

        self.assertTrue(len(result) == 6)
        for num in range(0,len(result)):        
            self.assertTrue(result[num].value == 1)

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

        self.assertTrue(len(result) == 6)
        for num in range(0,len(result)):        
            self.assertTrue(result[num].value == 1)
