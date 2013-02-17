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
        database.session.add(Athlete("Test", "Athlete"))
        database.session.commit()
        self.test_athlete = Athlete.query.filter_by(first_name = "Test").first()

        # initialize the Activity table with known values
        for num in range(1, 4):

            database.session.add(            
                Activity(
                    self.test_athlete.id, 
                    num * 10, 
                    num * 10, 
                    datetime.date(1111, num, num), 
                    "run" ))

            database.session.add(            
                Activity(
                    self.test_athlete.id, 
                    num * 10, 
                    num * 10, 
                    datetime.date(1111, num, num), 
                    "run" ))

            database.session.add(
                Activity(
                    self.test_athlete.id, 
                    num * 10, 
                    num * 10, 
                    datetime.date(1111, num, num), 
                    "ride" ))

            database.session.add(
                Activity(
                    self.test_athlete.id, 
                    num * 10, 
                    num * 10, 
                    datetime.date(1111, num, num), 
                    "ride" ))

        database.session.commit()
        

    def tearDown(self):
        """
        This method is run before tests to provide setup
        """
        
    def test_total_distance_year(self):
        """
        """

        result = self.statseng.total(
            "distance",
            "run", 
            self.test_athlete.id,
            "01/01/1000",
            "01/01/3000",
            "year")

        self.assertTrue(len(result) == 1)
        self.assertTrue(result[0]['sum'] == 120)


    def test_total_distance_month(self):
        """
        """

        result = self.statseng.total(
            "distance",
            "run", 
            self.test_athlete.id,
            "01/01/1000",
            "01/01/3000",
            "month")

        self.assertTrue(len(result) == 3)
        for num in range(0,len(result)):        
            self.assertTrue(result[num]['sum'] == result[num]['period'] * 20)

    def test_total_distance_day(self):
        """
        """

        result = self.statseng.total(
            "distance",
            "run", 
            self.test_athlete.id,
            "01/01/1000",
            "01/01/3000",
            "day")

        self.assertTrue(len(result) == 3)
        for num in range(0,len(result)):        
            self.assertTrue(result[num]['sum'] == result[num]['period'] * 20)

    def test_max_distance_year(self):
        """
        """

        result = self.statseng.maximum(
            "distance",
            "run", 
            self.test_athlete.id,
            "01/01/1000",
            "01/01/3000",
            "year")

        self.assertTrue(len(result) == 1)
        self.assertTrue(result[0]['max'] == 30)

    def test_max_distance_month(self):
        """
        """

        result = self.statseng.maximum(
            "distance",
            "run", 
            self.test_athlete.id,
            "01/01/1000",
            "01/01/3000",
            "month")

        self.assertTrue(len(result) == 3)
        for num in range(0,len(result)):        
            self.assertTrue(result[num]['max'] == result[num]['period'] * 10)

    def test_max_distance_day(self):
        """
        """

        result = self.statseng.maximum(
            "distance",
            "run", 
            self.test_athlete.id,
            "01/01/1000",
            "01/01/3000",
            "day")

        self.assertTrue(len(result) == 3)
        for num in range(0,len(result)):        
            self.assertTrue(result[num]['max'] == result[num]['period'] * 10)

    def test_min_distance_year(self):
        """
        """

        result = self.statseng.minimum(
            "distance",
            "run", 
            self.test_athlete.id,
            "01/01/1000",
            "01/01/3000",
            "year")

        self.assertTrue(len(result) == 1)
        self.assertTrue(result[0]['min'])

    def test_min_distance_month(self):
        """
        """

        result = self.statseng.minimum(
            "distance",
            "run", 
            self.test_athlete.id,
            "01/01/1000",
            "01/01/3000",
            "month")

        self.assertTrue(len(result) == 3)
        for num in range(0,len(result)):        
            self.assertTrue(result[num]['min'] == result[num]['period'] * 10)

    def test_min_distance_day(self):
        """
        """

        result = self.statseng.minimum(
            "distance",
            "run", 
            self.test_athlete.id,
            "01/01/1000",
            "01/01/3000",
            "month")

        self.assertTrue(len(result) == 3)
        for num in range(0,len(result)):        
            self.assertTrue(result[num]['min'] == result[num]['period'] * 10)

    def test_avg_distance_year(self):
        """
        """

        result = self.statseng.average(
            "distance",
            "run", 
            self.test_athlete.id,
            "01/01/1000",
            "01/01/3000",
            "year")

        self.assertTrue(len(result) == 1)
        self.assertTrue(result[0]['avg'] == 20)

    def test_avg_distance_month(self):
        """
        """

        result = self.statseng.average(
            "distance",
            "run", 
            self.test_athlete.id,
            "01/01/1000",
            "01/01/3000",
            "month")

        self.assertTrue(len(result) == 3)
        for num in range(0,len(result)):        
            self.assertTrue(result[num]['avg'] == result[num]['period'] * 10)

    def test_avg_distance_day(self):
        """
        """

        result = self.statseng.average(
            "distance",
            "run", 
            self.test_athlete.id,
            "01/01/1000",
            "01/01/3000",
            "day")

        self.assertTrue(len(result) == 3)
        for num in range(0,len(result)):        
            self.assertTrue(result[num]['avg'] == result[num]['period'] * 10)

    def test_max_distance_month(self):
        """
        """

        result = self.statseng.maximum(
            "distance",
            "run", 
            self.test_athlete.id,
            "01/01/1000",
            "01/01/3000",
            "month")

        self.assertTrue(len(result) == 3)
        for num in range(0,len(result)):        
            self.assertTrue(result[num]['max'] == result[num]['period'] * 10)

    def test_count_distance_year(self):
        """
        """

        result = self.statseng.count(
            "distance",
            "run", 
            self.test_athlete.id,
            "01/01/1000",
            "01/01/3000",
            "year")

        self.assertTrue(len(result) == 1)
        self.assertTrue(result[0]['count'] == 6)

    def test_count_distance_month(self):
        """
        """

        result = self.statseng.count(
            "distance",
            "run", 
            self.test_athlete.id,
            "01/01/1000",
            "01/01/3000",
            "month")

        self.assertTrue(len(result) == 3)
        for num in range(0,len(result)):        
            self.assertTrue(result[num]['count'] == 2)

    def test_count_distance_day(self):
        """
        """

        result = self.statseng.count(
            "distance",
            "run", 
            self.test_athlete.id,
            "01/01/1000",
            "01/01/3000",
            "day")

        self.assertTrue(len(result) == 3)
        for num in range(0,len(result)):        
            self.assertTrue(result[num]['count'] == 2)
