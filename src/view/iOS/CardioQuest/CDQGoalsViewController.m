//
//  CDQGoalsViewController.m
//  CardioQuest
//
//  Created by Blake Andrew Beatty on 2013-03-12.
//  Copyright (c) 2013 comp4350group5. All rights reserved.
//

#import "CDQGoalsViewController.h"
#import "ASIHTTPRequest.h"
#import "Classes/SBJson.h"

@interface CDQGoalsViewController ()
    
@end

@implementation CDQGoalsViewController

NSArray *tableData;

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
    
    // Initialize table data
    tableData = [NSArray arrayWithObjects:@"NO RECORDS", nil];
}

- (void)didReceiveMemoryWarning
{
    [super didReceiveMemoryWarning];
    // Dispose of any resources that can be recreated.
}

- (NSInteger)tableView:(UITableView *)tableView numberOfRowsInSection:(NSInteger)section
{
    return [tableData count];
}

- (UITableViewCell *)tableView:(UITableView *)tableView cellForRowAtIndexPath:(NSIndexPath *)indexPath
{
    static NSString *simpleTableIdentifier = @"SimpleTableItem";
    
    UITableViewCell *cell = [tableView dequeueReusableCellWithIdentifier:simpleTableIdentifier];
    
    if (cell == nil) {
        cell = [[UITableViewCell alloc] initWithStyle:UITableViewCellStyleDefault reuseIdentifier:simpleTableIdentifier];
    }
    
    cell.textLabel.text = [tableData objectAtIndex:indexPath.row];
    return cell;
}

-(void)viewWillAppear:(BOOL)animated
{
    NSURL *url = [NSURL URLWithString:@"http://ec2-107-21-196-190.compute-1.amazonaws.com:8000/goals/update_datatable"];
    
    ASIHTTPRequest *request = [ASIHTTPRequest requestWithURL:url];
    [request addRequestHeader:@"Accept" value:@"application/json"];
    [request addRequestHeader:@"Content-Type" value:@"application/json"];
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
    NSMutableDictionary *dictionary = jsonDictionary[@"aaData"];
    NSMutableArray *the_array = [NSMutableArray array];
    
    for (NSMutableDictionary *activity in dictionary)
    {   
        NSMutableString* the_string = [[NSMutableString alloc]init];
        [the_string appendFormat:@"%@! %@ %@ (Between: %@ and %@)",
        (activity[@"completed"]== NULL)? @"ONGOING" : @"COMPLETED",
        activity[@"activity"],
        activity[@"quantity"],
        activity[@"start_date"],
        activity[@"end_date"]];
        [the_array addObject:the_string];
    }
    tableData = the_array;
    
    [self.goalsTable reloadData];
}

- (void)requestFailed:(ASIHTTPRequest *)request
{
    NSError *error = [request error];
}

@end
