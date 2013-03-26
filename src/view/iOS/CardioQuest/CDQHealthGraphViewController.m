//
//  CDQHealthGraphViewController.m
//  CardioQuest
//
//  Created by Andrew Konkin on 3/25/13.
//  Copyright (c) 2013 comp4350group5. All rights reserved.
//

#import "CDQHealthGraphViewController.h"
#import "ECGraph.h"
#import "CDQGraphHealth.h"

@interface CDQHealthGraphViewController ()

@end

@implementation CDQHealthGraphViewController

CDQGraphHealth *graph;
NSString *dateType;

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
    
	//add graph to the view as a subview
    
    CGRect viewBound = [[UIScreen mainScreen] bounds];
    CGSize viewSize = viewBound.size;
    CGFloat viewWidth = viewSize.width;
    CGFloat viewHeight = viewSize.height;
    
    graph = [[CDQGraphHealth alloc] initWithFrame: CGRectMake(0, 150, viewWidth, viewHeight-700)];
    graph.backgroundColor = [UIColor colorWithWhite:1.0 alpha:0.0];
    [self.view addSubview:graph];
    
    dateTypes = [[NSArray alloc] initWithObjects:@"Month", @"Year", nil];
    
    dateType = @"Month";
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
        return dateTypes.count;
}

//set items in the rows
-(NSString *)pickerView:(UIPickerView *)pickerView titleForRow:(NSInteger)row forComponent:(NSInteger)component
{
        return [dateTypes objectAtIndex:row];
}

- (void)pickerView:(UIPickerView *)pickerView didSelectRow:(NSInteger)row inComponent:(NSInteger)component
{
    dateType = (NSString*)[dateTypes objectAtIndex:row];
    
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
    
    ///////////////////////////
    //PREPARE FOR SERVER CALL//
    ///////////////////////////
    
    NSString *query;
    
    query = [NSString stringWithFormat:@"http://ec2-107-21-196-190.compute-1.amazonaws.com:8000/health/json?start_date=%ld-%ld-%ld&end_date=%ld-%ld-%ld",(long)start.day,(long)start.month,(long)start.year,(long)end.day,(long)end.month,(long)end.year];
    
    
    //make the graph update points by calling the server
    [graph triggerServerCall:query];
}

@end
