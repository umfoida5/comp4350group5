//
//  CDQHealthGraphViewController.m
//  CardioQuest
//
//  Created by Andrew Konkin on 3/25/13.
//  Copyright (c) 2013 comp4350group5. All rights reserved.
//

#import "CDQHealthGraphViewController.h"
#import "ECGraph.h"
#import "CDQgraph.h"

@interface CDQHealthGraphViewController ()

@end

@implementation CDQHealthGraphViewController

CDQGraph *graph;
NSString *healthType;
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
    
    graph = [[CDQGraph alloc] initWithFrame: CGRectMake(0, 150, viewWidth, viewHeight-700)];
    graph.backgroundColor = [UIColor colorWithWhite:1.0 alpha:0.0];
    [self.view addSubview:graph];
    
    dateTypes = [[NSArray alloc] initWithObjects:@"Day", @"Week", @"Month", @"Year", nil];
    healthTypes = [[NSArray alloc] initWithObjects:@"Weight", @"Resting Heart Rate", nil];
    
    dateType = @"Day";
    healthType = @"Weight";
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
        return healthTypes.count;
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
        return [healthTypes objectAtIndex:row];
    }
    
    else //if ([pickerView tag] == 2)
    {
        return [dateTypes objectAtIndex:row];
    }
}

- (void)pickerView:(UIPickerView *)pickerView didSelectRow:(NSInteger)row inComponent:(NSInteger)component
{
    //change the UIPicker values
    if ([pickerView tag] == 1)
    {
        healthType = (NSString*)[healthTypes objectAtIndex:row];
    }
    
    else //if ([pickerView tag] == 2)
    {
        dateType = (NSString*)[dateTypes objectAtIndex:row];
    }
    
    ///////////////////////////
    //PREPARE FOR SERVER CALL//
    ///////////////////////////
    
}

@end
