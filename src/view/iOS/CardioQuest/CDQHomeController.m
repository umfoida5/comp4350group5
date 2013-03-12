//
//  CDQHomeController.m
//  CardioQuest
//
//  Created by Justin Foidart on 2013-03-08.
//  Copyright (c) 2013 comp4350group5. All rights reserved.
//

#import "CDQHomeController.h"
#import "ASIHTTPRequest.h"
#import "ASIFormDataRequest.h"
@interface CDQHomeController ()

@property (weak, nonatomic) IBOutlet UIButton *loginBtn;
@property (weak, nonatomic) IBOutlet UIButton *signupBtn;
@property (weak, nonatomic) IBOutlet UIButton *logoutBtn;
@property (weak, nonatomic) IBOutlet UITextField *loginUsername;
@property (weak, nonatomic) IBOutlet UITextField *loginPassword;
@property (weak, nonatomic) IBOutlet UITextField *signupUsername;
@property (weak, nonatomic) IBOutlet UITextField *signupPassword;
@property (weak, nonatomic) IBOutlet UITextField *signupFirstName;
@property (weak, nonatomic) IBOutlet UITextField *signupLastName;

@property (weak, nonatomic) IBOutlet UILabel *loginUsernameLabel;
@property (weak, nonatomic) IBOutlet UILabel *loginPasswordLabel;
@property (weak, nonatomic) IBOutlet UILabel *signupUsernameLabel;
@property (weak, nonatomic) IBOutlet UILabel *signupPasswordLabel;
@property (weak, nonatomic) IBOutlet UILabel *signupFirstNameLabel;
@property (weak, nonatomic) IBOutlet UILabel *signupLastNameLabel;
@property (weak, nonatomic) IBOutlet UILabel *loginLabel;
@property (weak, nonatomic) IBOutlet UILabel *signupLabel;
@property (weak, nonatomic) IBOutlet UILabel *loginResponseLabel;
@property (weak, nonatomic) IBOutlet UILabel *loggedInUsernameLabel;

@end

@implementation CDQHomeController
- (IBAction)login:(id)sender
{
    NSURL *url = [NSURL URLWithString:@"http://ec2-107-21-196-190.compute-1.amazonaws.com:8000/login/do_login"];
    
    ASIFormDataRequest *request = [ASIFormDataRequest requestWithURL:url];
    [request addPostValue:_loginUsername.text forKey:@"username"];
    [request addPostValue:_loginPassword.text forKey:@"pw"];
    [request setDelegate:self];
    [request startAsynchronous];
}

- (void)requestFinished:(ASIHTTPRequest *)request
{
    // Use when fetching text data
    NSString *responseString = [request responseString];
    
    // Display server response about login/logout validity
    self.loginResponseLabel.text = responseString;
    
    // Toggle visibility for all UI elements for login/logout if successful
    if([responseString isEqual: @"Login was successful."] || [responseString isEqualToString:@"Logout was successful."]) {
        
        [self.loginBtn setHidden:![self.loginBtn isHidden]];
        [self.signupBtn setHidden:![self.signupBtn isHidden]];
        [self.logoutBtn setHidden:![self.logoutBtn isHidden]];
        [self.loginUsername setHidden:![self.loginUsername isHidden]];
        [self.loginPassword setHidden:![self.loginPassword isHidden]];
        [self.signupFirstName setHidden:![self.signupFirstName isHidden]];
        [self.signupLastName setHidden:![self.signupLastName isHidden]];
        [self.signupUsername setHidden:![self.signupUsername isHidden]];
        [self.signupPassword setHidden:![self.signupPassword isHidden]];
        
        [self.loginUsernameLabel setHidden:![self.loginUsernameLabel isHidden]];
        [self.loginPasswordLabel setHidden:![self.loginPasswordLabel isHidden]];
        [self.signupUsernameLabel setHidden:![self.signupUsernameLabel isHidden]];
        [self.signupPasswordLabel setHidden:![self.signupPasswordLabel isHidden]];
        [self.signupFirstNameLabel setHidden:![self.signupFirstNameLabel isHidden]];
        [self.signupLastNameLabel setHidden:![self.signupLastNameLabel isHidden]];
        [self.loginLabel setHidden:![self.loginLabel isHidden]];
        [self.signupLabel setHidden:![self.signupLabel isHidden]];
        [self.loginResponseLabel setHidden:![self.loginResponseLabel isHidden]];
        [self.loggedInUsernameLabel setHidden:![self.loggedInUsernameLabel isHidden]];
    }
    
}

- (void)requestFailed:(ASIHTTPRequest *)request
{
    // TODO: handle error
    NSError *error = [request error];
}

- (IBAction)signup:(id)sender
{
    NSURL *url = [NSURL URLWithString:@"http://ec2-107-21-196-190.compute-1.amazonaws.com:8000/login/signup"];
    ASIFormDataRequest *request = [ASIFormDataRequest requestWithURL:url];
    [request addPostValue:_signupUsername.text forKey:@"username"];
    [request addPostValue:_signupPassword.text forKey:@"pw"];
    [request addPostValue:_signupFirstName.text forKey:@"firstName"];
    [request addPostValue:_signupLastName.text forKey:@"lastName"];
    [request setDelegate:self];
    [request startAsynchronous];
}

- (IBAction)logout:(id)sender
{
    NSURL *url = [NSURL URLWithString:@"http://ec2-107-21-196-190.compute-1.amazonaws.com:8000/login/do_logout"];
    
    ASIFormDataRequest *request = [ASIFormDataRequest requestWithURL:url];
    [request setDelegate:self];
    [request startAsynchronous];
    
    // TODO: remove login cookies on iOS side?
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
    
    [self.loggedInUsernameLabel setHidden:YES];
	[self.logoutBtn setHidden:YES];
    self.view.backgroundColor = [[UIColor alloc] initWithPatternImage:[UIImage imageNamed:@"CardioQuestMain.jpeg"]];
    
}

- (void)didReceiveMemoryWarning
{
    [super didReceiveMemoryWarning];
    // Dispose of any resources that can be recreated.
}

@end
