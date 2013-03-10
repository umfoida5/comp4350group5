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
@property (weak, nonatomic) IBOutlet UILabel *signupFitsNameLabel;
@property (weak, nonatomic) IBOutlet UILabel *signupLastNameLabel;
@property (weak, nonatomic) IBOutlet UILabel *loginLabel;
@property (weak, nonatomic) IBOutlet UILabel *signupLabel;
@property (weak, nonatomic) IBOutlet UIButton *changeUserButton;

@end

@implementation CDQHomeController
- (IBAction)login:(id)sender
{
    //Add login code.
    NSURL *url = [NSURL URLWithString:@"http://ec2-107-21-196-190.compute-1.amazonaws.com:8000/login/do_login"];
    ASIFormDataRequest *request = [ASIFormDataRequest requestWithURL:url];
    [request addPostValue:_loginUsername.text forKey:@"username"];
    [request addPostValue:_loginPassword.text forKey:@"pw"];
    [request setDelegate:self];
    [request startAsynchronous];
}

//GET CODE:
//NSURL *url = [NSURL URLWithString:@"http://ec2-107-21-196-190.compute-1.amazonaws.com:8000/login/do_login?username=testme&pw=testme"];
//ASIHTTPRequest *request = [ASIHTTPRequest requestWithURL:url];
//[request setDelegate:self];
//[request startAsynchronous];


- (void)requestFinished:(ASIHTTPRequest *)request
{
    // Use when fetching text data
    NSString *responseString = [request responseString];
    
    if ([responseString isEqual: @"Incorrect password."] || [responseString isEqual: @"Invalid username."]) {
        
    }
    else {
        [self.loginBtn setHidden:YES];
        [self.signupBtn setHidden:YES];
        [self.logoutBtn setHidden:YES];
        [self.loginUsername setHidden:YES];
        [self.loginPassword setHidden:YES];
        [self.signupFirstName setHidden:YES];
        [self.signupLastName setHidden:YES];
        [self.signupUsername setHidden:YES];
        [self.signupPassword setHidden:YES];
        
        [self.loginUsernameLabel setHidden:YES];
        [self.loginPasswordLabel setHidden:YES];
        [self.signupUsernameLabel setHidden:YES];
        [self.signupPasswordLabel setHidden:YES];
        [self.signupFitsNameLabel setHidden:YES];
        [self.signupLastNameLabel setHidden:YES];
        [self.loginLabel setHidden:YES];
        [self.signupLabel setHidden:YES];
        
        [self.changeUserButton setHidden:NO];
    }
}
//
//- (void)requestFailed:(ASIHTTPRequest *)request
//{
//    NSError *error = [request error];
//}

- (IBAction)signup:(id)sender
{
    //Add signup code.

}

- (IBAction)changeUser:(id)sender
{
    // Add logout code.
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
    
	[self.logoutBtn setHidden:YES];
    self.view.backgroundColor = [[UIColor alloc] initWithPatternImage:[UIImage imageNamed:@"CardioQuestMain.jpeg"]];
    
}

- (void)didReceiveMemoryWarning
{
    [super didReceiveMemoryWarning];
    // Dispose of any resources that can be recreated.
}

@end
