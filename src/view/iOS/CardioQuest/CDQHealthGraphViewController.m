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
NSString *startDate;
NSString *endDate;

- (id)initWithNibName:(NSString *)nibNameOrNil bundle:(NSBundle *)nibBundleOrNil
{
    self = [super initWithNibName:nibNameOrNil bundle:nibBundleOrNil];
    if (self) {
        // Custom initialization
    }
    return self;
}

- (IBAction)startDateChanged:(id)sender {
    
    NSDateFormatter *dateFormatter = [[NSDateFormatter alloc] init];
    [dateFormatter setDateFormat:@"dd-MM-yyyy"];
    NSString *tempDate = [dateFormatter stringFromDate:self.startDatePicker.date];
    
    startDate = tempDate;
    
    ///////////////////////////
    //PREPARE FOR SERVER CALL//
    ///////////////////////////
    
    NSString *query;
    
    query = [NSString stringWithFormat:@"http://ec2-107-21-196-190.compute-1.amazonaws.com:8000/health/json?start_date=%@&end_date=%@",startDate,endDate];
    
    
    //make the graph update points by calling the server
    [graph triggerServerCall:query];
}

- (IBAction)endDateChanged:(id)sender {
    
    NSDateFormatter *dateFormatter = [[NSDateFormatter alloc] init];
    [dateFormatter setDateFormat:@"dd-MM-yyyy"];
    NSString *tempDate = [dateFormatter stringFromDate:self.endDatePicker.date];
    
    endDate = tempDate;
    
    ///////////////////////////
    //PREPARE FOR SERVER CALL//
    ///////////////////////////
    
    NSString *query;
    
    query = [NSString stringWithFormat:@"http://ec2-107-21-196-190.compute-1.amazonaws.com:8000/health/json?start_date=%@&end_date=%@",startDate,endDate];
    
    
    //make the graph update points by calling the server
    [graph triggerServerCall:query];
}

- (void)viewDidLoad
{
    [super viewDidLoad];
    
    self.view.backgroundColor = [[UIColor alloc] initWithPatternImage:[UIImage imageNamed:@"Ubuntu Orange.jpg"]];
    
	//add graph to the view as a subview
    
    CGRect viewBound = [[UIScreen mainScreen] bounds];
    CGSize viewSize = viewBound.size;
    CGFloat viewWidth = viewSize.width;
    CGFloat viewHeight = viewSize.height;
    
    graph = [[CDQGraphHealth alloc] initWithFrame: CGRectMake(0, 150, viewWidth, viewHeight-700)];
    graph.backgroundColor = [UIColor colorWithWhite:1.0 alpha:0.0];
    [self.view addSubview:graph];
    
    NSCalendar *cal = [NSCalendar currentCalendar];
    NSDateComponents *dt = [[NSCalendar currentCalendar] components:NSDayCalendarUnit | NSMonthCalendarUnit | NSYearCalendarUnit fromDate:[NSDate date]];
    NSDate *date = [cal dateFromComponents:dt];
    
    [self.startDatePicker setDate:date];
    
    [dt setYear:[dt year]-1];
    
    [self.endDatePicker setDate:date];
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

@end
