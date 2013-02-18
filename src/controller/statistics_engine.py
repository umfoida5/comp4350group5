#!/usr/bin/python

import cherrypy
from modules import database
from model.activity import Activity
from sqlalchemy import func, Integer
import datetime

class StatisticsEngine:
    	
    """
    total()
    
    finds the sum of values from the given table and column for 
    the through the date range, grouped by the given time period
    """
    def total(
        self, 
        column_name,
        activity_name, 
        athlete_id,
        start_date,
        end_date,
        group_by):

        #determines the search column from the table by name
        search_col = getattr(Activity, column_name);

        # select columns for query
        sum_col = func.sum(search_col).label('sum')

        return self.run_query(sum_col, activity_name, athlete_id, start_date, end_date, group_by)



    """
    average()
    
    finds the average value from the given table and column for 
    the through the date range, grouped by the given time period
    """
    def average(
        self, 
        column_name,
        activity_name,
        athlete_id,
        start_date,
        end_date,
        group_by):

        #determines the search column from the table by name
        search_col = getattr(Activity, column_name);

        # select columns for query
        sum_col = func.avg(search_col).label('avg')

        return self.run_query(sum_col, activity_name, athlete_id, start_date, end_date, group_by)
        
    """
    minimum()
    
    finds the minimum vaue from the given table and column for 
    the through the date range, grouped by the given time period
    """
    def minimum(
        self,
        column_name, 
        activity_name, 
        athlete_id, 
        start_date,
        end_date,
        group_by):

        #determines the search column from the table by name
        search_col = getattr(Activity, column_name);

        # select columns for query
        sum_col = func.min(search_col).label('min')

        return self.run_query(sum_col, activity_name, athlete_id, start_date, end_date, group_by)
    
    """
    maximum()
    
    finds the maximim vaue from the given table and column for 
    the through the date range, grouped by the given time period
    """
    def maximum(
        self, 
        column_name, 
        activity_name, 
        athlete_id, 
        start_date, 
        end_date, 
        group_by):

        #determines the search column from the table by name
        search_col = getattr(Activity, column_name);

        # select columns for query
        max_col = func.max(search_col).label('max')

        return self.run_query(max_col, activity_name, athlete_id, start_date, end_date, group_by)

    """
    count()
    
    performs a count on the given table and column for the 
    through the date range, grouped by the given time period
    """
    def count(
        self,
        column_name, 
        activity_name, 
        athlete_id, 
        start_date, 
        end_date, 
        group_by):

        #determines the search column from the table by name
        search_col = getattr(Activity, column_name);

        # select columns for query
        sum_col = func.count(search_col).label('count')

        return self.run_query(sum_col, activity_name, athlete_id, start_date, end_date, group_by)


    """
    run_query()
    
    Queries the table for the values in the given table and column
    through the given date range, grouped by the given time period
    """
    def run_query(
        self, 
        operator_col, 
        activity_name, 
        athlete_id, 
        start_date, 
        end_date, 
        group_by):

        year_extract  = func.extract("year" , Activity.date).label('year')
        month_extract = func.extract("month", Activity.date).label('month')
        day_extract   = func.extract("day"  , Activity.date).label('day')

        #if a group by has been provided for period, perform groupby
        if group_by is not None:
            if (group_by == "year"):
                all_things = database.session\
                    .query(operator_col, year_extract)\
                    .group_by(year_extract)

            elif (group_by == "month"):
                all_things = database.session\
                    .query(operator_col, year_extract, month_extract)\
                    .group_by(year_extract, month_extract)

            elif (group_by == "day"):
                all_things = database.session\
                    .query(operator_col, year_extract, month_extract, day_extract)\
                    .group_by(year_extract, month_extract, day_extract)

            else:
                raise "Incorrect group_by passed to StatisticsEngine"
        else:
            all_things = database.session.query(operator_col)

        # if an activity has been provided, filter by activity
        if activity_name is not None:
            all_things = all_things.filter(Activity.type == activity_name)

        # if an athlete_id has been provided, filter by athlete_id
        if athlete_id is not None:
            all_things = all_things.filter(Activity.athlete_id == athlete_id)

        # if a starting date has been provided, filter dates earlier than start
        if start_date is not None:
            all_things = all_things.filter(Activity.date >= start_date)

        # if an ending date has been provided, filter dates later than end        
        if end_date is not None:
            all_things = all_things.filter(Activity.date <= end_date)
        
        return all_things.all()
