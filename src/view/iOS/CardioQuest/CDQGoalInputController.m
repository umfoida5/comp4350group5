//
//  CDQGoalInputController.m
//  CardioQuest
//
//  Created by Justin Foidart on 2013-03-20.
//  Copyright (c) 2013 comp4350group5. All rights reserved.
//

#import "CDQGoalInputController.h"
#import "ASIFormDataRequest.h"

@interface CDQGoalInputController ()

@end

@implementation CDQGoalInputController

- (IBAction)createGoal:(id)sender
{
    NSDateFormatter *dateFormatter = [[NSDateFormatter alloc] init];
    [dateFormatter setDateFormat:@"dd-MM-yyyy"];
    NSString *startDate = [dateFormatter stringFromDate:self.startDateInput.date];
    NSString *endDate = [dateFormatter stringFromDate:self.endDateInput.date];
    
    NSString *activityType = [self.typeContentArray objectAtIndex:[self.typeOperatorMetricInput selectedRowInComponent:0]];
    NSString *goalOperator = [self.operatorContentArray objectAtIndex:[self.typeOperatorMetricInput selectedRowInComponent:1]];
    NSString *goalMetric = [self.metricContentArray objectAtIndex:[self.typeOperatorMetricInput selectedRowInComponent:2]];
    
    NSURL *url = [NSURL URLWithString:@"http://ec2-107-21-196-190.compute-1.amazonaws.com:8000/goals/create"];
    
    ASIFormDataRequest *request = [ASIFormDataRequest requestWithURL:url];
    [request addPostValue: activityType forKey:@"activity"];
    [request addPostValue: goalOperator forKey:@"operator"];
    [request addPostValue: self.quantityInput.text forKey:@"quantity"];
    [request addPostValue: goalMetric forKey:@"metric"];
    [request addPostValue: startDate forKey:@"start_date"];
    [request addPostValue: endDate forKey:@"end_date"];
    
    [request setDelegate:self];
    [request startAsynchronous];
}

- (NSInteger)numberOfComponentsInPickerView:(UIPickerView *)thePickerView
{
    return 3;
}

- (NSInteger)pickerView:(UIPickerView *)thePickerView numberOfRowsInComponent:(NSInteger)component
{
    if(component == 0)
    {
        return [self.typeContentArray count];
    }
    else if(component == 1)
    {
        return [self.operatorContentArray count];
    }
    else
    {
        return [self.metricContentArray count];
    }
}

- (NSString *)pickerView:(UIPickerView *)thePickerView titleForRow:(NSInteger)row forComponent:(NSInteger)component
{
    if(component == 0)
    {
        return [self.typeContentArray objectAtIndex:row];
    }
    else if(component == 1)
    {
        return [self.operatorContentArray objectAtIndex:row];
    }
    else
    {
        return [self.metricContentArray objectAtIndex:row];
    }
}

- (void)requestFinished:(ASIHTTPRequest *)request
{
    [self.navigationController popToRootViewControllerAnimated:YES];
}

- (void)pickerView:(UIPickerView *)thePickerView didSelectRow:(NSInteger)row inComponent:(NSInteger)component
{
    //Interface requires method, but we don't need to do anything.
}

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
    
    self.view.backgroundColor = [[UIColor alloc] initWithPatternImage:[UIImage imageNamed:@"Ubuntu Orange.jpg"]];
    self.navigationController.navigationBar.tintColor = [UIColor orangeColor];
	
    self.typeContentArray = [[NSMutableArray alloc] init];
    [self.typeContentArray addObject:@"Run"];
    [self.typeContentArray addObject:@"Walk"];
    [self.typeContentArray addObject:@"Bike"];
    
    self.operatorContentArray = [[NSMutableArray alloc] init];
    [self.operatorContentArray addObject:@"Total"];
    [self.operatorContentArray addObject:@"Min"];
    [self.operatorContentArray addObject:@"Max"];
    [self.operatorContentArray addObject:@"Average"];
    
    self.metricContentArray = [[NSMutableArray alloc] init];
    [self.metricContentArray addObject:@"Distance"];
    [self.metricContentArray addObject:@"Max Speed"];
}

- (void)didReceiveMemoryWarning
{
    [super didReceiveMemoryWarning];
    // Dispose of any resources that can be recreated.
}

@end