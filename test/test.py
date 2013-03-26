#!/usr/bin/python

import os, sys
import unittest

sys.path.append('../src')

import cherrypy
from modules import database
from controller_tests.achievements_test import AchievementsTest
from controller_tests.activities_test import ActivitiesTest
from controller_tests.statistics_engine_test import StatisticsEngineTest
from controller_tests.goals_test import GoalsTest
from controller_tests.profiles_test import ProfilesTest
from controller_tests.stats_test import StatsTest
from controller_tests.login_test import LoginTest
from controller_tests.events_test import EventsTest
from controller_tests.health_test import HealthTest
from model_tests.achievement_test import AchievementTests
from model_tests.athlete_test import AthleteTests
from model_tests.activity_test import ActivityTests
from model_tests.event_test import EventTests
from model_tests.goal_test import GoalTests
from model_tests.health_test import HealthTests
from modules_tests.jsonable_test import JsonableTests
from modules_tests.transaction_test import TransactionTests
from modules_tests.datatables_test import DatatablesTests

# hack to be able to use sessions in the tests
cherrypy.session = cherrypy.lib.sessions.RamSession()

user = os.environ.get("psql_user", "")
database.init("tracker_test", user)
database.recreate_tables()

if __name__ == '__main__':
    unittest.main()
