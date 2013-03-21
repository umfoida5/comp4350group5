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
#import "CDQAchievement.h"
#import "ASIFormDataRequest.h"
#import <QuartzCore/QuartzCore.h>

@class ASINetworkQueue;
@interface ProfileViewController (){
	ASINetworkQueue *queue;
	NSArray *tableData;
}

@property (weak, nonatomic) IBOutlet UILabel *nameLabel;
@property (weak, nonatomic) IBOutlet UIImageView *profileImage;

@property (weak, nonatomic) IBOutlet UITextField *dobField;
@property (weak, nonatomic) IBOutlet UITextField *addressField;
@property (weak, nonatomic) IBOutlet UITextField *emailField;
@property (weak, nonatomic) IBOutlet UITextView *aboutTextView;
@property (weak, nonatomic) IBOutlet UITableView *achievementTable;
@property (retain) ASINetworkQueue *queue;
@property NSMutableArray *imgCollection;

@end

@implementation ProfileViewController



-(void)viewWillAppear:(BOOL)animated
{
    if(!self.queue)
        self.queue = [[ASINetworkQueue alloc] init];
    self.aboutTextView.delegate = self;
    //self.aboutTextView.delegate = t;
    [self.profileImage setImage:[UIImage imageNamed:@"default_profile_pic.png"]];
    self.imgCollection = [NSMutableArray array];
    [self setQueue:[ASINetworkQueue queue]];
    
	[[self queue] setDelegate:self];
	[[self queue] setRequestDidFinishSelector:@selector(requestDone:)];
	[[self queue] setRequestDidFailSelector:@selector(requestFailed:)];
	[[self queue] setQueueDidFinishSelector:@selector(queueFinished:)];
    
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
        self.dobField.text = [jsonDictionary[@"birth_date"] isKindOfClass:[NSNull class]]? @"Enter Birth Day" : jsonDictionary[@"birth_date"];
        self.addressField.text = jsonDictionary[@"address"];
        self.emailField.text = [jsonDictionary[@"email"] isKindOfClass:[NSNull class]]? @"Enter Email" : jsonDictionary[@"email"];
        self.aboutTextView.text = jsonDictionary[@"about_me"];
       
        for (NSMutableDictionary *achieves in jsonDictionary[@"achievements"]) {
            
            NSMutableString *url = [[NSMutableString alloc]init];
            [url appendFormat:@"http://ec2-107-21-196-190.compute-1.amazonaws.com:8000%@",achieves[@"image_url"]];
            [url replaceCharactersInRange:[url rangeOfString:@".."] withString:@""];
            
            __strong ASIHTTPRequest *newRequest = [ASIHTTPRequest requestWithURL:[NSURL URLWithString:url]];
            [self.queue addOperation:newRequest];
            newRequest.userInfo = achieves;
            [[self queue] go];
            
        } 
    }
}
- (IBAction)enterDOB:(id)sender {
    
    NSURL *url = [NSURL URLWithString:@"http://ec2-107-21-196-190.compute-1.amazonaws.com:8000/profiles/update_dob"];
    
    ASIFormDataRequest *request = [ASIFormDataRequest requestWithURL:url];
    [request addPostValue:@"" forKey:@"id"];
    [request addPostValue:self.dobField.text forKey:@"birth_date"];

    [request setDelegate:self];
    [request startAsynchronous];
}
- (IBAction)enterAddress:(id)sender {
    NSURL *url = [NSURL URLWithString:@"http://ec2-107-21-196-190.compute-1.amazonaws.com:8000/profiles/update_address"];
    
    ASIFormDataRequest *request = [ASIFormDataRequest requestWithURL:url];
    [request addPostValue:@"" forKey:@"id"];
    [request addPostValue:self.addressField.text forKey:@"address"];
    
    [request setDelegate:self];
    [request startAsynchronous];
}
- (IBAction)enterEmail:(id)sender {
    NSURL *url = [NSURL URLWithString:@"http://ec2-107-21-196-190.compute-1.amazonaws.com:8000/profiles/update_email"];
    
    ASIFormDataRequest *request = [ASIFormDataRequest requestWithURL:url];
    [request addPostValue:@"" forKey:@"id"];
    [request addPostValue:self.emailField.text forKey:@"email"];
    
    [request setDelegate:self];
    [request startAsynchronous];
}


- (void)queueFinished:(ASINetworkQueue *)queue
{
	// You could release the queue here if you wanted
	if ([[self queue] requestsCount] == 0) {
		self.queue = nil;
	}
	NSLog(@"Queue finished");
}

- (void)requestDone:(ASIHTTPRequest*)req
{
    UIImage* image = [UIImage imageWithData:[req responseData]];
    CDQAchievement *achievement = [[CDQAchievement alloc]init];
    achievement.image = image;
    achievement.title = req.userInfo[@"title"];
    achievement.desc = req.userInfo[@"description"];
    [[self imgCollection] addObject:achievement];
        //[self.profileImage setImage:image];
    tableData = self.imgCollection;
    [self.achievementTable reloadData];
    //[[self achievementTable] insert]
    //[[self Achievements] addSubview:temp];
}
- (NSInteger)tableView:(UITableView *)tableView numberOfRowsInSection:(NSInteger)section
{
    return [tableData count];
}
- (UITableViewCell *)tableView:(UITableView *)tableView cellForRowAtIndexPath:(NSIndexPath *)indexPath {
    
    UITableViewCell *cell = [tableView dequeueReusableCellWithIdentifier:@"MyIdentifier"];
    if (cell == nil) {
        cell = [[UITableViewCell alloc] initWithStyle:UITableViewCellStyleSubtitle reuseIdentifier:@"MyIdentifier"];
        cell.selectionStyle = UITableViewCellSelectionStyleNone;
    }
    CDQAchievement *achievement = (CDQAchievement*)[tableData objectAtIndex:indexPath.row];
    cell.imageView.image = achievement.image;
    cell.textLabel.text = achievement.title;
    
    return cell;
}


- (void)requestFailed:(ASIHTTPRequest *)request
{
    NSError *error = [request error];
    NSLog(@"%@",error);
}

- (id)initWithNibName:(NSString *)nibNameOrNil bundle:(NSBundle *)nibBundleOrNil
{
    self = [super initWithNibName:nibNameOrNil bundle:nibBundleOrNil];
    if (self) {
        // Custom initialization
    }
    return self;
}

- (BOOL)textViewShouldEndEditing:(UITextView *)aboutTextView{
    NSURL *url = [NSURL URLWithString:@"http://ec2-107-21-196-190.compute-1.amazonaws.com:8000/profiles/update_about"];
    aboutTextView.editable = YES;
    NSLog(@"%@", aboutTextView.text);
    ASIFormDataRequest *request = [ASIFormDataRequest requestWithURL:url];
    [request addPostValue:@"" forKey:@"id"];
    [request addPostValue: aboutTextView.text forKey:@"about_msg"];
    
    [request setDelegate:self];
    [request startAsynchronous];
    
    return YES;
}

- (void)viewDidLoad
{
    [super viewDidLoad];
    
    //change color of text field placeholder to black
    [self.dobField setValue:[UIColor darkGrayColor] forKeyPath:@"_placeholderLabel.textColor"];
    [self.addressField setValue:[UIColor darkGrayColor] forKeyPath:@"_placeholderLabel.textColor"];
    [self.emailField setValue:[UIColor darkGrayColor] forKeyPath:@"_placeholderLabel.textColor"];
    
    //Insert border to text view
    self.aboutTextView.layer.borderWidth = 1;
    
    self.view.backgroundColor = [[UIColor alloc] initWithPatternImage:[UIImage imageNamed:@"Ubuntu Orange.jpg"]];
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
