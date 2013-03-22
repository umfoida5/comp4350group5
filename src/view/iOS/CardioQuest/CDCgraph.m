//
//  CDCgraph.m
//  CardioQuest
//
//  Created by Andrew Konkin on 3/20/13.
//  Copyright (c) 2013 comp4350group5. All rights reserved.
//

#import "CDCgraph.h"
#import "ECCommon.h"
#import "ECGraph.h"
#import "ECGraphItem.h"
#import "ECGraphLine.h"
#import "ECGraphPoint.h"
#import "ASIFormDataRequest.h"
#import "Classes/SBJson.h"

@implementation CDCgraph

CGContextRef context;
NSString* activity;
NSString* dateType;
NSString* measurementType;
NSArray* graphPoints;

- (id)initWithFrame:(CGRect)frame
{
    self = [super initWithFrame:frame];
    if (self) {        
        ECGraphPoint *point1 = [[ECGraphPoint alloc] init];
        point1.yValue = 3;
        point1.xDateValue = [ECCommon dOfS:@"2010-4-23 12:00:00"
                                withFormat:kDEFAULT_DATE_TIME_FORMAT];
        
        ECGraphPoint *point2 = [[ECGraphPoint alloc] init];
        point2.yValue = 5;
        point2.xDateValue = [ECCommon dOfS:@"2010-4-25 12:00:00"
                                withFormat:kDEFAULT_DATE_TIME_FORMAT];
        
        ECGraphPoint *point3 = [[ECGraphPoint alloc] init];
        point3.yValue = 3;
        point3.xDateValue = [ECCommon dOfS:@"2010-4-28 12:00:00"
                                withFormat:kDEFAULT_DATE_TIME_FORMAT];
        
        ECGraphPoint *point4 = [[ECGraphPoint alloc] init];
        point4.yValue = 9;
        point4.xDateValue = [ECCommon dOfS:@"2010-4-29 12:00:00"
                                withFormat:kDEFAULT_DATE_TIME_FORMAT];
        
        ECGraphPoint *point5 = [[ECGraphPoint alloc] init];
        point5.yValue = 3;
        point5.xDateValue = [ECCommon dOfS:@"2010-4-30 12:00:00"
                                withFormat:kDEFAULT_DATE_TIME_FORMAT];
        
        ECGraphPoint *point6 = [[ECGraphPoint alloc] init];
        point6.yValue = 12;
        point6.xDateValue = [ECCommon dOfS:@"2010-5-29 12:00:00"
                                withFormat:kDEFAULT_DATE_TIME_FORMAT];
        
        NSMutableArray *tempArray = [[NSMutableArray alloc] init];
        [tempArray addObject:point1];
        [tempArray addObject:point2];
        [tempArray addObject:point3];
        [tempArray addObject:point4];
        [tempArray addObject:point5];
        [tempArray addObject:point6];
        
        graphPoints = (NSArray*)tempArray;
        //graphPoints = [[NSArray alloc] initWithObjects:point1,point2,point3,point4,point5,point6,nil];
    }
    return self;
}

//THIS IS THE CODE THAT DRAWS TO THE VIEW
- (void)drawRect:(CGRect)rect
{
    context = UIGraphicsGetCurrentContext();
    
    ECGraph *graph = [[ECGraph alloc] initWithFrame:rect withContext:context isPortrait:NO];
    
    ECGraphLine *line1 = [[ECGraphLine alloc] init];
    line1.isXDate = YES;
    line1.points = graphPoints;
    line1.color = [UIColor blackColor];
    
    NSArray *lines = [[NSArray alloc] initWithObjects:line1,nil];
    [graph setXaxisTitle:@"Date"];
    [graph setYaxisTitle:@"cummulative no of skills"];
    [graph setGraphicTitle:@"Cummulative Number of imitations acquired"];
    [graph setXaxisDateFormat:@"MM/dd/YY"];
    [graph setDelegate:self];
    [graph setBackgroundColor:[UIColor colorWithRed:220/255.0 green:220/255.0 blue:220/255.0 alpha:1]];
    [graph setPointType:ECGraphPointTypeSquare];
    [graph drawCurveWithLines:lines lineWidth:2 color:[UIColor blackColor]];
    
}
 

//SetGraph function
//takes: elements from UI pickers for use in the graph labels
//makes a call to the server for graph points
//then sets class variables so that the drawRect function can draw everything correctly
-(void)setGraph:(NSString*)newActivity: (NSString*)newDateType: (NSString*)newMeasurementType
{    
    activity = newActivity;
    dateType = newDateType;
    measurementType = newMeasurementType;
    
    ECGraphPoint *point1 = [[ECGraphPoint alloc] init];
    point1.yValue = 8;
    point1.xDateValue = [ECCommon dOfS:@"2010-4-23 12:00:00"
                            withFormat:kDEFAULT_DATE_TIME_FORMAT];
    
    ECGraphPoint *point2 = [[ECGraphPoint alloc] init];
    point2.yValue = 2;
    point2.xDateValue = [ECCommon dOfS:@"2010-4-25 12:00:00"
                            withFormat:kDEFAULT_DATE_TIME_FORMAT];
    
    ECGraphPoint *point3 = [[ECGraphPoint alloc] init];
    point3.yValue = 10;
    point3.xDateValue = [ECCommon dOfS:@"2010-4-28 12:00:00"
                            withFormat:kDEFAULT_DATE_TIME_FORMAT];
    
    ECGraphPoint *point4 = [[ECGraphPoint alloc] init];
    point4.yValue = 6;
    point4.xDateValue = [ECCommon dOfS:@"2010-4-29 12:00:00"
                            withFormat:kDEFAULT_DATE_TIME_FORMAT];
    
    ECGraphPoint *point5 = [[ECGraphPoint alloc] init];
    point5.yValue = 3;
    point5.xDateValue = [ECCommon dOfS:@"2010-4-30 12:00:00"
                            withFormat:kDEFAULT_DATE_TIME_FORMAT];
    
    ECGraphPoint *point6 = [[ECGraphPoint alloc] init];
    point6.yValue = 1;
    point6.xDateValue = [ECCommon dOfS:@"2010-5-29 12:00:00"
                            withFormat:kDEFAULT_DATE_TIME_FORMAT];
    
    NSMutableArray *tempArray = [[NSMutableArray alloc] init];
    [tempArray addObject:point1];
    [tempArray addObject:point2];
    [tempArray addObject:point3];
    [tempArray addObject:point4];
    [tempArray addObject:point5];
    [tempArray addObject:point6];
    
    graphPoints = (NSArray*)tempArray;
    
    //graphPoints = [[NSArray alloc] initWithObjects:point1,point2,point3,point4,point5,point6,nil];
}

- (void)triggerServerCall
{
    NSURL *url;
    
    //production server
    if ([measurementType isEqual:@"Top Speed"])
    {
        url = [NSURL URLWithString:@"http://ec2-107-21-196-190.compute-1.amazonaws.com:8000/stats/get_maximum"];
    }
    else
    {
        url = [NSURL URLWithString:@"http://ec2-107-21-196-190.compute-1.amazonaws.com:8000/stats/get_total"];
    }
    
    NSString *measureLower = [measurementType lowercaseString];
    NSString *activityLower = [activity lowercaseString];
    
    if ([measureLower isEqual:@"top speed"])
    {
        measureLower = @"max_speed";
    }
    
    NSDateComponents *start = [[NSCalendar currentCalendar] components:NSDayCalendarUnit | NSMonthCalendarUnit | NSYearCalendarUnit fromDate:[NSDate date]];
    NSDateComponents *end = [[NSCalendar currentCalendar] components:NSDayCalendarUnit | NSMonthCalendarUnit | NSYearCalendarUnit fromDate:[NSDate date]];
    
    if ([dateType isEqual:@"Year"])
    {
        [start setYear:[end year]-1];
    }
    
    else if ([dateType isEqual:@"Month"])
    {
        [start setMonth:[end month]-1];
    }
    
    else if ([dateType isEqual:@"Week"])
    {
        [start setDay:[end day]-7];
    }
    
    else //if ([dateType isEqual:@"Day"])
    {
        [start setDay:[end day]-1];
    }
    
    NSCalendar *cal = [NSCalendar currentCalendar];
    NSDate *startDate = [cal dateFromComponents:start];
    NSDate *endDate = [cal dateFromComponents:end];
    
    ASIFormDataRequest *request = [ASIFormDataRequest requestWithURL:url];
    [request addPostValue:measureLower forKey:@"column_name"];
    [request addPostValue:activityLower forKey:@"activity_name"];
    [request addPostValue:@"1" forKey:@"athlete_id"];
    [request addPostValue:startDate forKey:@"start_date"];
    [request addPostValue:endDate forKey:@"end_date"];
    [request addPostValue:@"day" forKey:@"group_by"];
    [request setDelegate:self];
    [request startAsynchronous];
}

- (void)requestFinished:(ASIHTTPRequest *)request
{
    // Use when fetching text data
    NSString *responseString = [request responseString];
    NSLog(@"Info back from the server: %@",responseString);
    
    SBJsonParser *parser = [[SBJsonParser alloc]init];
    NSMutableDictionary* jsonDictionary = [parser objectWithString:responseString];
    /*
    if (jsonDictionary != nil)
    {
        //graphPoints
        
        //jsonDictionary[@"key"];
        
//        for (NSMutableDictionary *achieves in jsonDictionary[@"achievements"]) {
//        }
    }
     */
    
    [self setNeedsDisplay];
}

@end
