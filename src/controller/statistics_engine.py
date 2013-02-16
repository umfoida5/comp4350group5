#!/usr/bin/python

import cherrypy
from modules.database import db_session

class StatisticsEngine:
    	
    sql_template = \
            """
            SELECT
                {0}({1}) AS {0}
            FROM
                activities
            WHERE
                activities.athlete_id    = {2}   AND
                activities.activity_type = '{3}' AND
                activities.date BETWEEN    to_date('{4}', 'mm/dd/yyyy') AND to_date('{5}', 'mm/dd/yyyy')
            GROUP BY
                EXTRACT ({6} FROM activities.date)
            """

    """
    total()
    
    finds the sum of values from the given table and column for 
    the through the date range, grouped by the given time period
    """
    def total(self, 
        column,
        activity, 
        athlete,
        start_date,
        end_date,
        group_by):

        return self.run_query(
            "sum", 
            column, 
            activity, 
            athlete, 
            start_date, 
            end_date, 
            group_by)

    """
    average()
    
    finds the average value from the given table and column for 
    the through the date range, grouped by the given time period
    """
    def average(self, 
        column,
        activity,
        athlete,
        start_date,
        end_date,
        group_by):

        if (column      is None or
            activity    is None or
            athlete     is None or
            start_date  is None or
            end_date    is None or 
            group_by    is None):
            
            raise Exception("NULL PARAMTER PASSED to StatisticsEngine::average()")

        return self.run_query(
            "avg", 
            column, 
            activity, 
            athlete, 
            start_date, 
            end_date, 
            group_by)
        
    """
    minimum()
    
    finds the minimum vaue from the given table and column for 
    the through the date range, grouped by the given time period
    """
    def minimum(self,
        column, 
        activity, 
        athlete, 
        start_date,
        end_date,
        group_by):

        if (column      is None or
            activity    is None or
            athlete     is None or
            start_date  is None or
            end_date    is None or 
            group_by    is None):
            
            raise Exception("NULL PARAMTER PASSED to StatisticsEngine::minimum()")

        return self.run_query(
            "min", 
            column, 
            activity, 
            athlete, 
            start_date, 
            end_date, 
            group_by)

    
    """
    maximum()
    
    finds the maximim vaue from the given table and column for 
    the through the date range, grouped by the given time period
    """
    def maximum(self, 
        column, 
        activity, 
        athlete, 
        start_date, 
        end_date, 
        group_by):

        if (column      is None or
            activity    is None or
            athlete     is None or
            start_date  is None or
            end_date    is None or 
            group_by    is None):
            
            raise Exception("NULL PARAMTER PASSED to StatisticsEngine::maximum()")
         
        return self.run_query(
            "max", 
            column, 
            activity, 
            athlete, 
            start_date, 
            end_date, 
            group_by)

    """
    count()
    
    performs a count on the given table and column for the 
    through the date range, grouped by the given time period
    """
    def count(self,
        column, 
        activity, 
        athlete, 
        start_date, 
        end_date, 
        group_by):

        if (column     is None or
            activity   is None or
            athlete    is None or
            start_date is None or
            end_date   is None or 
            group_by   is None):
            
            raise Exception("NULL PARAMTER PASSED to StatisticsEngine::count()")

        return self.run_query(
            "sum", 
            column, 
            activity, 
            athlete, 
            start_date, 
            end_date, 
            group_by)


    """
    run_query()
    
    Queries the table for the values in the given table and column
    through the given date range, grouped by the given time period
    """
    def run_query(self, 
        operator, 
        column, 
        activity, 
        athlete, 
        start_date, 
        end_date, 
        group_by):

        if (operator   is None or 
            column     is None or
            activity   is None or
            athlete    is None or
            start_date is None or
            end_date   is None or 
            group_by   is None):
            
            raise Exception("NULL PARAMTER PASSED to StatisticsEngine::run_query()")

        sql = self.sql_template.format(
            operator, 
            column, 
            athlete, 
            activity, 
            start_date,
            end_date,
            group_by)

        result = db_session.execute(sql)
        print sql
        print result.fetchall()
        return "good to go"     
