#!/usr/bin/python

import sys
import unittest

sys.path.append('../src')

from controller_tests.root_test import RootTest
from controller_tests.athletes_test import AthletesTest
from controller_tests.achievements_test import AchievementsTest
from controller_tests.statistics_engine_test import StatisticsEngineTest
from model_tests.achievement_test import AchievementTests
from model_tests.athlete_test import AthleteTests
from model_tests.event_test import EventTests
from modules_tests.jsonable_test import JsonableTests
from modules_tests.transaction_test import TransactionTests

if __name__ == '__main__':
    unittest.main()
