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
@property (weak, nonatomic) IBOutlet UILabel *validationLabel;

@end

@implementation CDQEventsInputController

- (IBAction)postEvent:(id)sender
{
    //Checking if distance is a number
    NSRegularExpression *isDigitRegex = [NSRegularExpression regularExpressionWithPattern:@"^[0-9]+$" options:0 error:NULL];
    NSTextCheckingResult *match = [isDigitRegex firstMatchInString:self.distanceInput.text options:0 range:NSMakeRange(0, [self.distanceInput.text length])];
    
    if ( match )
    {
        self.validationLabel.hidden = YES;        
        
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
    else
    {
        self.validationLabel.hidden = NO;
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
    
    self.validationLabel.hidden = YES;  
    
    self.view.backgroundColor = [[UIColor alloc] initWithPatternImage:[UIImage imageNamed:@"Ubuntu Orange.jpg"]];
    self.descriptionInput.layer.borderWidth = 1;
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
