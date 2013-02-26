#!/usr/bin/python

import os, sys
import unittest

sys.path.append('../src')

from modules import database
from controller_tests.achievements_test import AchievementsTest
from controller_tests.statistics_engine_test import StatisticsEngineTest
from controller_tests.goals_test import GoalsTest
from controller_tests.profiles_test import Profiles
from controller_tests.calendar_test import CalendarTest
from model_tests.achievement_test import AchievementTests
from model_tests.athlete_test import AthleteTests
from model_tests.activity_test import ActivityTests
from model_tests.event_test import EventTests
from model_tests.goal_test import GoalTests
from modules_tests.jsonable_test import JsonableTests
from modules_tests.transaction_test import TransactionTests
from modules_tests.datatables_test import DatatablesTests

user = os.environ.get("psql_user", "")
database.init("tracker_test", user, False)
database.recreate_tables()

if __name__ == '__main__':
    unittest.main()
