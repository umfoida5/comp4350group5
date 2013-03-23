//
//  CDQHealthTableViewController.m
//  CardioQuest
//
//  Created by Blake Beatty on 2013-03-23.
//  Copyright (c) 2013 comp4350group5. All rights reserved.
//

#import "CDQHealthTableViewController.h"
#import "ASIHTTPRequest.h"
#import "Classes/SBJson.h"

@interface CDQHealthTableViewController ()

@end

@implementation CDQHealthTableViewController
{
    NSArray *tableData;
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
	
    // Initialize table data
    tableData = [NSArray arrayWithObjects:@"No events have been posted, or you aren't connected to the internet.", nil];
    
    self.view.backgroundColor = [[UIColor alloc] initWithPatternImage:[UIImage imageNamed:@"Ubuntu Orange.jpg"]];
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
    [self populateTable];
}

-(void) populateTable
{
    NSURL *url = [NSURL URLWithString:@"http://ec2-107-21-196-190.compute-1.amazonaws.com:8000/health/update_datatable?iDisplayLength=1000"];
    
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
        
    for (NSMutableDictionary *health_record in dictionary)
    {
        NSMutableString* the_string = [[NSMutableString alloc]init];
        [the_string appendFormat:@"%@: Weight: %@ Resting HR: %@ Comments: %@",
         health_record[@"health_date"],
         health_record[@"weight"],
         health_record[@"resting_heart_rate"],
         [health_record[@"comments"] substringWithRange:NSMakeRange(0, MIN([health_record[@"comments"] length] , 35))]];
        [the_array addObject:the_string];
    }
    tableData = the_array;
    
    [self.healthTable reloadData];
}

- (void)requestFailed:(ASIHTTPRequest *)request
{
}

// hides keyboard
- (void)touchesBegan:(NSSet *)touches withEvent:(UIEvent *)event
{
    [self.view endEditing:YES];
}

@end
