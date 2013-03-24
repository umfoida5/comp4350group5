//
//  CDQHomeViewController.m
//  CardioQuest
//
//  Created by Alex Salomon Thome Da Silva on 3/21/13.
//  Copyright (c) 2013 comp4350group5. All rights reserved.
//

#import "CDQHomeViewController.h"
#import "ASIFormDataRequest.h"

@interface CDQHomeViewController ()

@end

@implementation CDQHomeViewController

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
    
    //By default, show login and hide logout buttons
    self.navBar.leftBarButtonItem = nil;
    self.navBar.rightBarButtonItem = self.loginButton;
    
    self.view.backgroundColor = [[UIColor alloc] initWithPatternImage:[UIImage imageNamed:@"CardioQuestMain.jpeg"]];
}

-(void)viewWillAppear:(BOOL)animated
{
    NSURL *url = [NSURL URLWithString:@"http://ec2-107-21-196-190.compute-1.amazonaws.com:8000/get_current_username"];
    
    ASIFormDataRequest *request = [ASIFormDataRequest requestWithURL:url];
    [request setDelegate:self];
    [request startAsynchronous];
    [request setDidFinishSelector:@selector(get_username:)];
}

- (void)get_username:(ASIHTTPRequest *)request
{
    NSString *username = [request responseString];
    BOOL isLoggedIn = NO;
    
    if(![username isEqualToString:@""])
    {
        isLoggedIn = YES;
    }
    
    [self toggleNavBarButtons: isLoggedIn];
}

- (IBAction)doLogout:(id)sender
{
    NSURL *url = [NSURL URLWithString:@"http://ec2-107-21-196-190.compute-1.amazonaws.com:8000/login/do_logout"];
    
    ASIFormDataRequest *request = [ASIFormDataRequest requestWithURL:url];
    [request setDelegate:self];
    [request startAsynchronous];
    [request setDidFinishSelector:@selector(hideLogoutAndShowLogin:)];
}

- (void)hideLogoutAndShowLogin:(ASIHTTPRequest *)request
{
    [self toggleNavBarButtons: NO];
}

- (void)toggleNavBarButtons:(BOOL)isLoggedIn
{
    if(isLoggedIn)
    {
        self.navBar.leftBarButtonItem = self.logoutButton;
        self.navBar.rightBarButtonItem = nil;
    }
    else
    {
        self.navBar.leftBarButtonItem = nil;
        self.navBar.rightBarButtonItem = self.loginButton;
    }
}

- (void)didReceiveMemoryWarning
{
    [super didReceiveMemoryWarning];
    // Dispose of any resources that can be recreated.
}


@end
