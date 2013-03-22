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
        
        graphPoints = [[NSArray alloc] initWithObjects:point1,point2,point3,point4,point5,point6,nil];
    }
    return self;
}

//THIS IS THE CODE THAT DRAWS TO THE VIEW
- (void)drawRect:(CGRect)rect
{
    context = UIGraphicsGetCurrentContext();
    
    ECGraph *graph = [[ECGraph alloc] initWithFrame:rect withContext:context isPortrait:NO];
    
    //NSArray *points1 = [[NSArray alloc] initWithArray:graphPoints];
    //NSArray *points1 = graphPoints;
    ECGraphLine *line1 = [[ECGraphLine alloc] init];
    line1.isXDate = YES;
    //line1.points = points1;
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
    printf("DEBUG: setGraph is called\n");
    
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
    
    graphPoints = [[NSArray alloc] initWithObjects:point1,point2,point3,point4,point5,point6,nil];
}

/*
// Only override drawRect: if you perform custom drawing.
// An empty implementation adversely affects performance during animation.
- (void)drawRect:(CGRect)rect
{
    context = UIGraphicsGetCurrentContext();
    
    ECGraph *graph = [[ECGraph alloc] initWithFrame:rect withContext:context isPortrait:NO];
    
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
    
    NSArray *points1 = [[NSArray alloc] initWithObjects:point1,point2,point3,point4,point5,point6,nil];
    ECGraphLine *line1 = [[ECGraphLine alloc] init];
    line1.isXDate = YES;
    line1.points = points1;
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
 */
@end
