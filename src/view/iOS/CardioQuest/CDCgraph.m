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
NSArray* graphPoints;

//initialize the graph with dumy values
//
- (id)initWithFrame:(CGRect)frame
{
    self = [super initWithFrame:frame];
    if (self) {
        
        //init graph points with dummy values
        
        ECGraphPoint *point1 = [[ECGraphPoint alloc] init];
        point1.yValue = 0;
        point1.xDateValue = [ECCommon dOfS:@"2010-4-24"
                                withFormat:kDEFAULT_DATE_FORMAT];
        
        ECGraphPoint *point2 = [[ECGraphPoint alloc] init];
        point2.yValue = 0;
        point2.xDateValue = [ECCommon dOfS:@"2010-4-25"
                                withFormat:kDEFAULT_DATE_FORMAT];
        
        NSMutableArray *tempArray = [[NSMutableArray alloc] init];
        [tempArray addObject:point1];
        [tempArray addObject:point2];
        
        graphPoints = (NSArray*)tempArray;
    }
    return self;
}

//THIS IS THE CODE THAT DRAWS TO THE VIEW
//no code should call this method directly
//it is called automatically when you use [view SetNeedsDisplay]
- (void)drawRect:(CGRect)rect
{
    context = UIGraphicsGetCurrentContext();
    
    //create the graph
    ECGraph *graph = [[ECGraph alloc] initWithFrame:rect withContext:context isPortrait:NO];
    
    ECGraphLine *line1 = [[ECGraphLine alloc] init];
    line1.isXDate = YES;
    line1.points = graphPoints;
    line1.color = [UIColor blackColor];
    
    NSArray *lines = [[NSArray alloc] initWithObjects:line1,nil];
    [graph setXaxisTitle:@""];
    [graph setYaxisTitle:@""];
    [graph setGraphicTitle:@""];
    [graph setXaxisDateFormat:@"MM/dd/YY"];
    [graph setDelegate:self];
    [graph setBackgroundColor:[UIColor colorWithRed:220/255.0 green:220/255.0 blue:220/255.0 alpha:1]];
    [graph setPointType:ECGraphPointTypeSquare];
    
    //draw the graph
    [graph drawCurveWithLines:lines lineWidth:2 color:[UIColor blackColor]];
}

//triggerServerCall method
// query - the string used for the GET request
// (this should include the URL followed by any query parameters)
- (void)triggerServerCall:(NSString*)query
{       
    NSURL *url = [NSURL URLWithString:[query stringByAddingPercentEscapesUsingEncoding: NSUTF8StringEncoding]];
    
    NSLog(@"url = %@",url);
    
    ASIHTTPRequest *request = [ASIHTTPRequest requestWithURL:url];
    [request addRequestHeader:@"Accept" value:@"application/json"];
    [request addRequestHeader:@"Content-Type" value:@"application/json"];
    [request setDelegate:self];
    [request startAsynchronous];
}

- (void)requestFinished:(ASIHTTPRequest *)request
{
    NSString *responseString = [request responseString];
    NSLog(@"%@",responseString);
    
    SBJsonParser *parser = [[SBJsonParser alloc]init];
    NSMutableArray *points = [parser objectWithString:responseString];
    NSMutableArray *tempArray = [[NSMutableArray alloc] init];
    
    for (NSInteger i=0;i<points.count;i++)
    {
        NSMutableArray *point = [points objectAtIndex:i];
        
        ECGraphPoint *graphPoint = [[ECGraphPoint alloc] init];
        graphPoint.yValue = [[point objectAtIndex:0] integerValue];
        NSString *pointDate = [[NSString alloc] initWithFormat:@"%@-%@-%@",[point objectAtIndex:1],[point objectAtIndex:2],[point objectAtIndex:3]];
        graphPoint.xDateValue = [ECCommon dOfS:pointDate
                                withFormat:kDEFAULT_DATE_FORMAT];
        
        [tempArray addObject:graphPoint];
    }
    
    //sort the array
    NSSortDescriptor *sortDescriptor;
    sortDescriptor = [[NSSortDescriptor alloc] initWithKey:@"xDateValue" ascending:YES];
    NSArray *sortDescriptors = [NSArray arrayWithObject:sortDescriptor];
    
    graphPoints = (NSArray*)[tempArray sortedArrayUsingDescriptors:sortDescriptors];
    
    if (graphPoints.count > 0)
    {
        [self setNeedsDisplay];
    }
}

@end
