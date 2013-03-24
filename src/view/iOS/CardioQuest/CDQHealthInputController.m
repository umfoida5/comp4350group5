//
//  CDQHealthInputController.m
//  CardioQuest
//
//  Created by Blake Beatty on 2013-03-23.
//  Copyright (c) 2013 comp4350group5. All rights reserved.
//

#import "CDQHealthInputController.h"
#import "ASIFormDataRequest.h"
#import <QuartzCore/QuartzCore.h>

@interface CDQHealthInputController ()

@end

/*
@implementation CDQHealthInputController

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
	// Do any additional setup after loading the view.
}

- (void)didReceiveMemoryWarning
{
    [super didReceiveMemoryWarning];
    // Dispose of any resources that can be recreated.
}

@end
*/

@implementation CDQHealthInputController
- (IBAction)postHealthRecord:(id)sender {
    //Checking if weight and heart rate are numbers
    NSRegularExpression *isDigitRegex = [NSRegularExpression regularExpressionWithPattern:@"^[0-9]+$" options:0 error:NULL];
    NSTextCheckingResult *matchWeight = [isDigitRegex firstMatchInString:self.healthWeight.text options:0 range:NSMakeRange(0, [self.healthWeight.text length])];
    NSTextCheckingResult *matchHeartRate = [isDigitRegex firstMatchInString:self.healthHeartRate.text options:0 range:NSMakeRange(0, [self.healthHeartRate.text length])];
    if ( matchWeight && matchHeartRate )
    {
        //self.validationLabel.hidden = YES;
            
        NSDateFormatter *dateFormatter = [[NSDateFormatter alloc] init];
        [dateFormatter setDateFormat:@"dd-MM-yyyy"];
        NSString *date = [dateFormatter stringFromDate:self.healthDate.date];
    
        NSURL *url = [NSURL URLWithString:@"http://ec2-107-21-196-190.compute-1.amazonaws.com:8000/health/create"];
        
        ASIFormDataRequest *request = [ASIFormDataRequest requestWithURL:url];
        [request addPostValue: date forKey:@"health_date"];
        [request addPostValue: self.healthHeartRate.text forKey:@"resting_heart_rate"];
        [request addPostValue: self.healthWeight.text forKey:@"weight"];
        [request addPostValue: self.healthComments.text forKey:@"comment"];
    
        [request setDelegate:self];
        [request startAsynchronous];
    }
    else
    {
    //    self.validationLabel.hidden = NO;
    }
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
    
    //self.validationLabel.hidden = YES;
    
    self.view.backgroundColor = [[UIColor alloc] initWithPatternImage:[UIImage imageNamed:@"Ubuntu Orange.jpg"]];
}

- (void)viewDidDisappear:(BOOL)animated
{
    [super viewDidDisappear:(BOOL)animated];
    
    [self.navigationController popToRootViewControllerAnimated:YES];
}

- (void)didReceiveMemoryWarning
{
    [super didReceiveMemoryWarning];
    // Dispose of any resources that can be recreated.
}

// hides keyboard
- (void)touchesBegan:(NSSet *)touches withEvent:(UIEvent *)event
{
    [self.view endEditing:YES];
}

@end