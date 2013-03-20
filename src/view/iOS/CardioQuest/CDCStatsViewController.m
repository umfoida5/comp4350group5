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
@property (weak) IBOutlet CDCgraph *graph;
@property (weak) CGRect *dimensions;
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

- (void)pickerView:(UIPickerView *)pickerView didSelectRow:(NSInteger)row inComponent:(NSInteger)component
{
    if ([pickerView tag] == 1)
    {
        [self.graph drawRect:dimensions];
    }
    
    else //if ([pickerView tag] == 2)
    {
        
    }
}


@end