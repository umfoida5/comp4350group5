//
//  ProfileViewController.m
//  CardioQuest
//
//  Created by Philip Latka on 2013-03-08.
//  Copyright (c) 2013 comp4350group5. All rights reserved.
//

#import "ProfileViewController.h"
#import "ASIHTTPRequest.h"
#import "Classes/SBJson.h"
#import "ASINetworkQueue.h"
@interface ProfileViewController (){
    ASINetworkQueue *networkQueue;
}

@property (weak, nonatomic) IBOutlet UILabel *nameLabel;
@property (weak, nonatomic) IBOutlet UIImageView *profileImage;

@property (weak, nonatomic) IBOutlet UITextField *dobField;
@property (weak, nonatomic) IBOutlet UITextField *addressField;
@property (weak, nonatomic) IBOutlet UITextField *emailField;
@property (weak, nonatomic) IBOutlet UITextView *aboutTextView;
@property (retain) ASINetworkQueue *networkQueue;

@end

@implementation ProfileViewController


-(void)viewWillAppear:(BOOL)animated
{
    [self.profileImage setImage:[UIImage imageNamed:@"default_profile_pic.png"]];
    
    NSURL *url = [NSURL URLWithString:@"http://ec2-107-21-196-190.compute-1.amazonaws.com:8000/profiles/athlete"];
    [self sendRequest:url:@"start"];
   
    //[[self networkQueue]go];
}

- (void)sendRequest:(NSURL *)url : (NSString *) userInfo
{
    ASIHTTPRequest *request = [ASIHTTPRequest requestWithURL:url];
    //[[self networkQueue] addOperation:request];
    [request addRequestHeader:@"Accept" value:@"application/json"];
    [request addRequestHeader:@"Content-Type" value:@"application/json"];
    [request setUserInfo:[NSDictionary dictionaryWithObject:@"next" forKey:@"type"]];
    [request setDelegate:self];
    [request startAsynchronous];
    
}

- (void)requestFinished:(ASIHTTPRequest *)request
{
    // Use when fetching text data
    NSString *responseString = [request responseString];
    NSLog(@"%@",responseString);
    SBJsonParser *parser = [[SBJsonParser alloc]init];
    NSMutableDictionary* jsonDictionary = [parser objectWithString:responseString];
    NSMutableString* name = [[NSMutableString alloc]init];
    if (jsonDictionary != nil) {
        
    
        
        [name appendFormat:@"%@ %@",jsonDictionary[@"first_name"],jsonDictionary[@"last_name"]];
        self.nameLabel.text = name;
        self.dobField.text = jsonDictionary[@"birth_date"];
        self.addressField.text = jsonDictionary[@"address"];
        self.emailField.text = jsonDictionary[@"email"];
        self.aboutTextView.text = jsonDictionary[@"about_me"];
       
        for (NSMutableDictionary *achieves in jsonDictionary[@"achievements"]) {
            NSLog(@"%@", achieves[@"image_url"]);
        }

            
            
        
        
    }
    //BOOL stop = YES;
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

// hides keyboard
- (void)touchesBegan:(NSSet *)touches withEvent:(UIEvent *)event
{
    [self.view endEditing:YES];
}



@end
