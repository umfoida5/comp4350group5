//
//  CDQHomeController.m
//  CardioQuest
//
//  Created by Justin Foidart on 2013-03-08.
//  Copyright (c) 2013 comp4350group5. All rights reserved.
//

#import <Foundation/Foundation.h>
#import "CDQLoginController.h"
#import "ASIHTTPRequest.h"
#import "ASIFormDataRequest.h"
@interface CDQLoginController ()

//Login Stuff:
@property (weak, nonatomic) IBOutlet UILabel *loginTitle;
@property (weak, nonatomic) IBOutlet UITextField *loginUsernameField;
@property (weak, nonatomic) IBOutlet UITextField *loginPasswordField;
@property (weak, nonatomic) IBOutlet UILabel *loginUsernameLabel;
@property (weak, nonatomic) IBOutlet UILabel *loginPasswordLabel;
@property (weak, nonatomic) IBOutlet UIButton *loginButton;
@property (weak, nonatomic) IBOutlet UILabel *loginResponseLabel;

//Signup Stuff:
@property (weak, nonatomic) IBOutlet UILabel *signupTitle;
@property (weak, nonatomic) IBOutlet UITextField *signupUsernameField;
@property (weak, nonatomic) IBOutlet UITextField *signupPasswordField;
@property (weak, nonatomic) IBOutlet UITextField *signupFirstnameField;
@property (weak, nonatomic) IBOutlet UITextField *signupLastnameField;
@property (weak, nonatomic) IBOutlet UILabel *signupUsernameLabel;
@property (weak, nonatomic) IBOutlet UILabel *signupPasswordLabel;
@property (weak, nonatomic) IBOutlet UILabel *signupFirstnameLabel;
@property (weak, nonatomic) IBOutlet UITextField *signupLastnameLabel;
@property (weak, nonatomic) IBOutlet UIButton *signupButton;
@property (weak, nonatomic) IBOutlet UILabel *signupResponseLabel;


@end

@implementation CDQLoginController

- (IBAction)login:(id)sender
{
    [self loginRequest:self.loginUsernameField.text password:self.loginPasswordField.text];
}

- (void)loginRequest:(NSString*)username password:(NSString*)password
{
    NSURL *url = [NSURL URLWithString:@"http://ec2-107-21-196-190.compute-1.amazonaws.com:8000/login/do_login"];
    
    ASIFormDataRequest *request = [ASIFormDataRequest requestWithURL:url];
    [request addPostValue:username forKey:@"username"];
    [request addPostValue:password forKey:@"pw"];
    [request setUseKeychainPersistence:YES];
    [request setUsername:username];
    [request setPassword:password];
    [request setUseSessionPersistence:YES];
    [request setDelegate:self];
    [request startAsynchronous];
}

- (void)requestFinished:(ASIHTTPRequest *)request
{
    // Use when fetching text data
    NSString *responseString = [request responseString];
    
    if([responseString isEqual: @"Incorrect password."]
       || [responseString isEqual: @"Invalid username."])
    {        
        self.signupResponseLabel.text = @"Press the Sign Up button to Sign Up :)";
        self.loginResponseLabel.text = responseString;
    }
    else
    {
        self.loginResponseLabel.text = @"Press the Login button to Login :)";     
        self.signupResponseLabel.text = responseString;
    }
    
    //Navigate back to Home if login is successful
    if([responseString isEqual: @"Login was successful."])
    {
        [self.navigationController popToRootViewControllerAnimated:YES];        
    }
}

- (void)requestFailed:(ASIHTTPRequest *)request
{
    NSError *error = [request error];
    self.loginResponseLabel.text = [error localizedDescription];
}

- (IBAction)signup:(id)sender
{
    NSURL *url = [NSURL URLWithString:@"http://ec2-107-21-196-190.compute-1.amazonaws.com:8000/login/signup"];
    ASIFormDataRequest *request = [ASIFormDataRequest requestWithURL:url];
    [request addPostValue:self.signupUsernameField.text forKey:@"username"];
    [request addPostValue:self.signupPasswordField.text forKey:@"pw"];
    [request addPostValue:self.signupFirstnameField.text forKey:@"firstName"];
    [request addPostValue:self.signupLastnameField.text forKey:@"lastName"];
    [request setDelegate:self];
    [request startAsynchronous];
}

- (IBAction)logout:(id)sender
{
    NSURL *url = [NSURL URLWithString:@"http://ec2-107-21-196-190.compute-1.amazonaws.com:8000/login/do_logout"];
    
    ASIFormDataRequest *request = [ASIFormDataRequest requestWithURL:url];
    [request setDelegate:self];
    [request startAsynchronous];
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
    
    NSURL *url = [NSURL URLWithString:@"http://ec2-107-21-196-190.compute-1.amazonaws.com:8000/get_current_username"];
    
    ASIFormDataRequest *request = [ASIFormDataRequest requestWithURL:url];
    [request setDelegate:self];
    [request startAsynchronous];
    [request setDidFinishSelector:@selector(get_username:)];
    
    self.view.backgroundColor = [[UIColor alloc] initWithPatternImage:[UIImage imageNamed:@"Ubuntu Orange.jpg"]];  
}

- (void)get_username:(ASIHTTPRequest *)request
{
    NSString *username = [request responseString];
    
    //If we are already logged in, we want to toggle to logout.
    if(![username isEqualToString:@""])
    {
        [self.navigationController popToRootViewControllerAnimated:YES];
    }
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
