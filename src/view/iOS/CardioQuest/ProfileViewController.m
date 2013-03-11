//
//  ProfileViewController.m
//  CardioQuest
//
//  Created by Philip Latka on 2013-03-08.
//  Copyright (c) 2013 comp4350group5. All rights reserved.
//

#import "ProfileViewController.h"
#import "ASIHTTPRequest.h"

@interface ProfileViewController ()

@property (weak, nonatomic) IBOutlet UILabel *nameLabel;
@property (weak, nonatomic) IBOutlet UIImageView *profileImage;

@end

@implementation ProfileViewController


-(void)viewWillAppear:(BOOL)animated
{
    NSURL *url = [NSURL URLWithString:@"http://ec2-107-21-196-190.compute-1.amazonaws.com:8000/profile/athlete"];
    ASIHTTPRequest *request = [ASIHTTPRequest requestWithURL:url];
    [request setDelegate:self];
    [request startAsynchronous];
}

- (void)requestFinished:(ASIHTTPRequest *)request
{
    // Use when fetching text data
    NSString *responseData = [request responseString];
    
    
}

- (void)requestFailed:(ASIHTTPRequest *)request
{
    NSError *error = [request error];
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
}

- (void)didReceiveMemoryWarning
{
    [super didReceiveMemoryWarning];
    // Dispose of any resources that can be recreated.
}

@end
