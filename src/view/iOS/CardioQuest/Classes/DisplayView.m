//
//  DisplayView.m
//  ECGraphic
//
//  Created by ris on 10-4-17.
//  Copyright 2010 __MyCompanyName__. All rights reserved.
//

#import "DisplayView.h"
#import "ECCommon.h"
#import "ECGraphPoint.h"
#import "ECGraphLine.h"
#import "ECGraphItem.h"

@implementation DisplayView


- (id)initWithFrame:(CGRect)frame {
    if ((self = [super initWithFrame:frame])) {
        // Initialization code
    }
    return self;
}


// Only override drawRect: if you perform custom drawing.
// An empty implementation adversely affects performance during animation.
- (void)drawRect:(CGRect)rect {
    // Drawing code
	CGContextRef _context = UIGraphicsGetCurrentContext();
	ECGraph *graph = [[ECGraph alloc] initWithFrame:CGRectMake(10,10, 480, 320) withContext:_context isPortrait:NO];
	
	ECGraphPoint *point1 = [[ECGraphPoint alloc] init];
	point1.yValue = 3;
	point1.xDateValue = [ECCommon dOfS:@"2010-4-23 12:00:00" withFormat:kDEFAULT_DATE_TIME_FORMAT];
	
	ECGraphPoint *point2 = [[ECGraphPoint alloc] init];
	point2.yValue = 5;
	point2.xDateValue = [ECCommon dOfS:@"2010-4-25 12:00:00" withFormat:kDEFAULT_DATE_TIME_FORMAT];
	
	ECGraphPoint *point3 = [[ECGraphPoint alloc] init];
	point3.yValue = 3;
	point3.xDateValue = [ECCommon dOfS:@"2010-4-28 12:00:00" withFormat:kDEFAULT_DATE_TIME_FORMAT];
	
	ECGraphPoint *point4 = [[ECGraphPoint alloc] init];
	point4.yValue = 9;
	point4.xDateValue = [ECCommon dOfS:@"2010-4-29 12:00:00" withFormat:kDEFAULT_DATE_TIME_FORMAT];
	
	ECGraphPoint *point5 = [[ECGraphPoint alloc] init];
	point5.yValue = 3;
	point5.xDateValue = [ECCommon dOfS:@"2010-4-30 12:00:00" withFormat:kDEFAULT_DATE_TIME_FORMAT];
	
	ECGraphPoint *point6 = [[ECGraphPoint alloc] init];
	point6.yValue = 12;
	point6.xDateValue = [ECCommon dOfS:@"2010-5-29 12:00:00" withFormat:kDEFAULT_DATE_TIME_FORMAT];
	
	ECGraphPoint *point7 = [[ECGraphPoint alloc] init];
	point7.yValue = 7;
	point7.xDateValue = [ECCommon dOfS:@"2010-4-10 12:00:00" withFormat:kDEFAULT_DATE_TIME_FORMAT];
	
	ECGraphPoint *point8 = [[ECGraphPoint alloc] init];
	point8.yValue = 13;
	point8.xDateValue = [ECCommon dOfS:@"2010-4-11 12:00:00" withFormat:kDEFAULT_DATE_TIME_FORMAT];
	
	ECGraphPoint *point9 = [[ECGraphPoint alloc] init];
	point9.yValue = 1;
	point9.xDateValue = [ECCommon dOfS:@"2010-4-14 12:00:00" withFormat:kDEFAULT_DATE_TIME_FORMAT];
	
	ECGraphPoint *point10 = [[ECGraphPoint alloc] init];
	point10.yValue = 3;
	point10.xDateValue = [ECCommon dOfS:@"2010-4-27 12:00:00" withFormat:kDEFAULT_DATE_TIME_FORMAT];
	
	ECGraphPoint *point11 = [[ECGraphPoint alloc] init];
	point11.yValue = 23;
	point11.xDateValue = [ECCommon dOfS:@"2010-7-29 12:00:00" withFormat:kDEFAULT_DATE_TIME_FORMAT];
	
	
	NSArray *points1 = [[NSArray alloc] initWithObjects:point1,point2,point3,point4,point5,point6,nil];
	ECGraphLine *line1 = [[ECGraphLine alloc] init];
	line1.isXDate = YES;
	line1.points = points1;
	//line1.color = [UIColor blackColor];
	line1.defaultColor = 2;
	NSArray *points2 = [[NSArray alloc] initWithObjects:point7,point8,point9,point10,point11,nil];
	ECGraphLine *line2 = [[ECGraphLine alloc] init];
	line2.isYDate = YES;
	line2.points = points2;
	
	NSArray *lines = [[NSArray alloc] initWithObjects:line1,line2,nil];
	[graph setXaxisTitle:@"Date"];
	[graph setYaxisTitle:@"cummulative no of skills"];
	[graph setGraphicTitle:@"Cummulative Number of imitations acquired"];
	[graph setXaxisDateFormat:@"MM/dd/YY"];
	[graph setDelegate:self];
	[graph setBackgroundColor:[UIColor colorWithRed:220/255.0 green:220/255.0 blue:220/255.0 alpha:1]];
	[graph setPointType:ECGraphPointTypeSquare];
	[graph drawCurveWithLines:lines lineWidth:2 color:[UIColor blackColor]];
	
	//ECGraphItem *item1 = [[ECGraphItem alloc] init];
//	item1.isPercentage = YES;
//	item1.yValue = 80;
//	item1.width = 35;
//	item1.name = @"item1";
//	
//	ECGraphItem *item2 = [[ECGraphItem alloc] init];
//	item2.isPercentage = YES;
//	item2.yValue = 35.3;
//	item2.width = 35;
//	item2.name = @"item2";
//	
//	ECGraphItem *item3 = [[ECGraphItem alloc] init];
//	item3.isPercentage = YES;
//	item3.yValue = 45;
//	item3.width = 35;
//	item3.name = @"item3";
//	
//	ECGraphItem *item4 = [[ECGraphItem alloc] init];
//	item4.isPercentage = YES;
//	item4.yValue = 78.6;
//	item4.width = 35;
//	item4.name = @"item4";
//	
//	ECGraphItem *item5 = [[ECGraphItem alloc] init];
//	item5.isPercentage = YES;
//	item5.yValue = 94.45;
//	item5.width = 35;
//	item5.name = @"item5";
//	
//	NSArray *items = [[NSArray alloc] initWithObjects:item1,item2,item3,item4,item5,nil];
//	[graph setXaxisTitle:@"name"];
//	[graph setYaxisTitle:@"Percentage"];
//	[graph setGraphicTitle:@"Histogram"];
//	[graph setDelegate:self];
//	[graph setBackgroundColor:[UIColor colorWithRed:220/255.0 green:220/255.0 blue:220/255.0 alpha:1]];
//	[graph drawHistogramWithItems:items lineWidth:2 color:[UIColor blackColor]];
	
}


- (void)dealloc {
    //[super dealloc];
}


@end
