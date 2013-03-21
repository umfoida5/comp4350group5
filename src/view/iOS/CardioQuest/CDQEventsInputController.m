//
//  CDQEventsInputController.m
//  CardioQuest
//
//  Created by Alex Salomon Thome Da Silva on 3/20/13.
//  Copyright (c) 2013 comp4350group5. All rights reserved.
//

#import "CDQEventsInputController.h"
#import "ASIFormDataRequest.h"
#import <QuartzCore/QuartzCore.h>

@interface CDQEventsInputController ()
@property (weak, nonatomic) IBOutlet UITextView *descriptionInput;
@property (weak, nonatomic) IBOutlet UITextField *cityInput;
@property (weak, nonatomic) IBOutlet UIDatePicker *dateInput;
@property (weak, nonatomic) IBOutlet UITextField *distanceInput;

@end

@implementation CDQEventsInputController

- (IBAction)postEvent:(id)sender
{
    NSDateFormatter *dateFormatter = [[NSDateFormatter alloc] init];
    [dateFormatter setDateFormat:@"dd-MM-yyyy"];
    NSString *date = [dateFormatter stringFromDate:self.dateInput.date];    
    
    NSURL *url = [NSURL URLWithString:@"http://ec2-107-21-196-190.compute-1.amazonaws.com:8000/events/create"];
    
    ASIFormDataRequest *request = [ASIFormDataRequest requestWithURL:url];
    [request addPostValue: date forKey:@"date"];
    [request addPostValue: self.cityInput.text forKey:@"location"];
    [request addPostValue: self.distanceInput.text forKey:@"distance"];
    [request addPostValue: self.descriptionInput.text forKey:@"description"];
    
    [request setDelegate:self];
    [request startAsynchronous];
}


- (void)requestFinished:(ASIHTTPRequest *)request
{
    [self.navigationController popToRootViewControllerAnimated:YES];
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
	
    self.descriptionInput.layer.borderWidth = 1;
    //self.descriptionInput.layer.borderWidth= 5.0f;
}

- (void)didReceiveMemoryWarning
{
    [super didReceiveMemoryWarning];
    // Dispose of any resources that can be recreated.
}

@end