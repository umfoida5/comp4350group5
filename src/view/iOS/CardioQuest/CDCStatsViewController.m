//
//  CDCStatsViewController.m
//  CardioQuest
//
//  Created by Andrew Konkin on 3/16/13.
//  Copyright (c) 2013 comp4350group5. All rights reserved.
//

#import "CDCStatsViewController.h"
#import "ECGraph.h"
#import "CDCgraph.h"

@interface CDCStatsViewController ()
@end


@implementation CDCStatsViewController

CDCgraph *graph;
NSString *activity;
NSString *dateType;
NSString *measurementType;

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
    
    CGRect viewBound = [[UIScreen mainScreen] bounds];
    CGSize viewSize = viewBound.size;
    CGFloat viewWidth = viewSize.width;
    CGFloat viewHeight = viewSize.height;
    
    graph = [[CDCgraph alloc] initWithFrame: CGRectMake(10, 150, viewWidth, viewHeight-700)];
    graph.backgroundColor = [UIColor colorWithWhite:1.0 alpha:0.0];
    [self.view addSubview:graph];
    activityTypes = [[NSArray alloc] initWithObjects:@"Bike", @"Run", @"Walk", nil];
    dateTypes = [[NSArray alloc] initWithObjects:@"Day", @"Week", @"Month", @"Year", nil];
    mesurementTypes = [[NSArray alloc] initWithObjects:@"Distance", @"Duration", @"Top Speed", nil];
    
    activity = @"Bike";
    dateType = @"Day";
    measurementType = @"Distance";
    
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
    
    else if ([pickerView tag] == 2)
    {
        return dateTypes.count;
    }
    
    else //if ([pickerView tag] == 3)
    {
        return mesurementTypes.count;
    }
}

//set items in the rows
-(NSString *)pickerView:(UIPickerView *)pickerView titleForRow:(NSInteger)row forComponent:(NSInteger)component
{
    if ([pickerView tag] == 1)
    {
        return [activityTypes objectAtIndex:row];
    }
    
    else if ([pickerView tag] == 2)
    {
        return [dateTypes objectAtIndex:row];
    }
    
    else //if ([pickerView tag] == 3)
    {
        return [mesurementTypes objectAtIndex:row];
    }
}

- (void)pickerView:(UIPickerView *)pickerView didSelectRow:(NSInteger)row inComponent:(NSInteger)component
{
    
    if ([pickerView tag] == 1)
    {
        activity = (NSString*)[activityTypes objectAtIndex:row];
    }
    
    else if ([pickerView tag] == 2)
    {
        dateType = (NSString*)[dateTypes objectAtIndex:row];
    }
               
    else //if ([pickerView tag] == 3)
    {
        measurementType = (NSString*)[mesurementTypes objectAtIndex:row];
    }
    
    //update labels for the graph
    [graph setGraph:activity:dateType:measurementType];
    
    //make the graph update points by calling the server
    [graph triggerServerCall];
}


@end