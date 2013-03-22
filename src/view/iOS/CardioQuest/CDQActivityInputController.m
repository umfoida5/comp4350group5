//
//  CDQActivityInputController.m
//  CardioQuest
//
//  Created by Alex Salomon Thome Da Silva on 3/20/13.
//  Copyright (c) 2013 comp4350group5. All rights reserved.
//

#import "CDQActivityInputController.h"
#import "ASIFormDataRequest.h"

@interface CDQActivityInputController ()
@property (weak, nonatomic) IBOutlet UIDatePicker *dateInput;
@property (weak, nonatomic) IBOutlet UITextField *durationInput;
@property (weak, nonatomic) IBOutlet UITextField *distanceInput;
@property (weak, nonatomic) IBOutlet UITextField *maxSpeedInput;
@property (weak, nonatomic) IBOutlet UILabel *validationLabel;

@end

@implementation CDQActivityInputController

- (IBAction)createActivity:(id)sender
{
    //Checking if distance, duration andmax speed are a number
    NSRegularExpression *isDigitRegex = [NSRegularExpression regularExpressionWithPattern:@"^[0-9]+$" options:0 error:NULL];
    NSTextCheckingResult *matchDistance = [isDigitRegex firstMatchInString:self.distanceInput.text options:0 range:NSMakeRange(0, [self.distanceInput.text length])];
    NSTextCheckingResult *matchDuration = [isDigitRegex firstMatchInString:self.durationInput.text options:0 range:NSMakeRange(0, [self.durationInput.text length])];
    NSTextCheckingResult *matchMaxSpeedInput = [isDigitRegex firstMatchInString:self.maxSpeedInput.text options:0 range:NSMakeRange(0, [self.maxSpeedInput.text length])];
    
    if ( matchDistance && matchDuration && matchMaxSpeedInput )
    {
        self.validationLabel.hidden = YES;
        
        NSDateFormatter *dateFormatter = [[NSDateFormatter alloc] init];
        [dateFormatter setDateFormat:@"dd-MM-yyyy"];
        NSString *date = [dateFormatter stringFromDate:self.dateInput.date];
        
        NSString *activityType = [self.typeContentArray objectAtIndex:[self.typeInput selectedRowInComponent:0]];
        
        NSURL *url = [NSURL URLWithString:@"http://ec2-107-21-196-190.compute-1.amazonaws.com:8000/activities/create"];
        
        ASIFormDataRequest *request = [ASIFormDataRequest requestWithURL:url];
        [request addPostValue: activityType forKey:@"type"];
        [request addPostValue: date forKey:@"date"];
        [request addPostValue: self.distanceInput.text forKey:@"distance"];
        [request addPostValue: self.durationInput.text forKey:@"duration"];
        [request addPostValue: self.maxSpeedInput.text forKey:@"max_speed"];
        
        [request setDelegate:self];
        [request startAsynchronous];
    }
    else if(!matchDuration)
    {
        self.validationLabel.text = @"Invalid duration";
        self.validationLabel.hidden = NO;
    }
    else if(!matchDistance)
    {
        self.validationLabel.text = @"Invalid distance";        
        self.validationLabel.hidden = NO;
    }
    else if(!matchMaxSpeedInput)
    {
        self.validationLabel.text = @"Invalid maximum speed";        
        self.validationLabel.hidden = NO;
    }
}

- (NSInteger)numberOfComponentsInPickerView:(UIPickerView *)thePickerView
{
    return 1;
}

- (NSInteger)pickerView:(UIPickerView *)thePickerView numberOfRowsInComponent:(NSInteger)component
{
    return [self.typeContentArray count];
}

- (NSString *)pickerView:(UIPickerView *)thePickerView titleForRow:(NSInteger)row forComponent:(NSInteger)component
{
    return [self.typeContentArray objectAtIndex:row];
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
    
    self.validationLabel.hidden = YES;
    
    self.view.backgroundColor = [[UIColor alloc] initWithPatternImage:[UIImage imageNamed:@"Ubuntu Orange.jpg"]];
	
    self.typeContentArray = [[NSMutableArray alloc] init];
    [self.typeContentArray addObject:@"Run"];
    [self.typeContentArray addObject:@"Walk"];
    [self.typeContentArray addObject:@"Bike"];
    
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
