//
//  CDCStatsViewController.m
//  CardioQuest
//
//  Created by Andrew Konkin on 3/16/13.
//  Copyright (c) 2013 comp4350group5. All rights reserved.
//

#import "CDCStatsViewController.h"
#import "ECGraph.h"

@interface CDCStatsViewController ()
@end

@implementation CDCStatsViewController

- (id)initWithNibName:(NSString *)nibNameOrNil bundle:(NSBundle *)nibBundleOrNil
{
    self = [super initWithNibName:nibNameOrNil bundle:nibBundleOrNil];
    if (self) {
        // Custom initialization
    }
    return self;
}

- (void)viewDidLoad
{
    [super viewDidLoad];
    activityTypes = [[NSArray alloc] initWithObjects:@"Bike", @"Run", @"Walk", nil];
    dateTypes = [[NSArray alloc] initWithObjects:@"Day", @"Week", @"Month", @"Year", nil];
    //CGContextRef _context = UIGraphicsGetCurrentContext();
    [self createHistograph];
    
}

//TODO: force interface orientation to landscape (this code does nothing)
-(BOOL)shouldAutorotateToInterfaceOrientation:(UIInterfaceOrientation)interfaceOrientation {
    return (self.interfaceOrientation == UIInterfaceOrientationLandscapeLeft);
}

- (void)didReceiveMemoryWarning
{
    [super didReceiveMemoryWarning];
    // Dispose of any resources that can be recreated.
}

//set the number of columns
-(NSInteger)numberOfComponentsInPickerView:(UIPickerView *)pickerView
{
    return 1;
}

//set the number of rows
-(NSInteger)pickerView:(UIPickerView *)pickerView numberOfRowsInComponent:(NSInteger)component
{
    if ([pickerView tag] == 1)
    {
        return activityTypes.count;
    }
    
    else //if ([pickerView tag] == 2)
    {
        return dateTypes.count;
    }
}

//set items in the rows
-(NSString *)pickerView:(UIPickerView *)pickerView titleForRow:(NSInteger)row forComponent:(NSInteger)component
{
    if ([pickerView tag] == 1)
    {
        return [activityTypes objectAtIndex:row];
    }
    
    else //if ([pickerView tag] == 2)
    {
        return [dateTypes objectAtIndex:row];
    }
}

-(void)createHistograph{
    //TODO: Current context is nil, must receive one to draw graph
    CGContextRef _context = UIGraphicsGetCurrentContext();
    
    ECGraph *graph = [[ECGraph alloc] initWithFrame:CGRectMake(10,10, 480, 320)
                                        withContext:_context isPortrait:NO];
    
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


@end