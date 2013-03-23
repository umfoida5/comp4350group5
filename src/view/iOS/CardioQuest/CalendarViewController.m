//
//  CalendarViewController.m
//  CardioQuest
//
//  Created by Philip Latka on 2013-03-08.
//  Copyright (c) 2013 comp4350group5. All rights reserved.
//

#import "CalendarViewController.h"
#import "CDQAppDelegate.h"
#import "ASIHTTPRequest.h"
#import "Classes/SBJson.h"

@interface CalendarViewController ()

@end


@implementation CalendarViewController

- (id)initWithNibName:(NSString *)nibNameOrNil bundle:(NSBundle *)nibBundleOrNil
{
    self = [super initWithNibName:nibNameOrNil bundle:nibBundleOrNil];
    if (self) {
        // Custom initialization
    }
    return self;
}

- (void) viewDidLoad
{
    self.activitiesArray = [NSMutableArray array];
    
	[super viewDidLoad];
	[self.monthView selectDate:[NSDate month]];
    //UIButton *cancelBtn = [UIButton buttonWithType:UIButtonTypeCustom];
    //[cancelBtn setFrame:CGRectMake(0, 0, 60, 40)];
    //[cancelBtn setTitle:@"Cancel" forState:UIControlStateNormal];
    //[cancelBtn addTarget:self action:@selector(CancelClicked:) forControlEvents:UIControlEventTouchUpInside];
    //UIBarButtonItem *cancelButtonItem = [[UIBarButtonItem alloc] initWithCustomView:cancelBtn];
    //self.navigationItem.leftBarButtonItem = cancelButtonItem;
}

-(void)viewWillAppear:(BOOL)animated
{
    [self.activitiesArray removeAllObjects];
    [self getActivitiesList];
    
}

- (void) getActivitiesList
{
    NSURL *url = [NSURL URLWithString:@"http://ec2-107-21-196-190.compute-1.amazonaws.com:8000/activities/update_datatable?iDisplayLength=1000"];
    
    ASIHTTPRequest *request = [ASIHTTPRequest requestWithURL:url];
    [request addRequestHeader:@"Accept" value:@"application/json"];
    [request addRequestHeader:@"Content-Type" value:@"application/json"];
    [request setDelegate:self];
    [request startAsynchronous];
}

- (void)requestFinished:(ASIHTTPRequest *)request
{
    NSString *responseString = [request responseString];
    
    SBJsonParser *parser = [[SBJsonParser alloc]init];
    NSMutableDictionary* jsonDictionary = [parser objectWithString:responseString];
    
    if (jsonDictionary != nil)
    {
        NSRange range = NSMakeRange(0, [jsonDictionary[@"aaData"] count]);
        NSIndexSet *indexSet = [NSIndexSet indexSetWithIndexesInRange:range];
        [self.activitiesArray insertObjects:jsonDictionary[@"aaData"] atIndexes:indexSet];
        [self.monthView reload];
    }
}

#pragma mark - MonthView Delegate & DataSource
- (NSArray*) calendarMonthView:(TKCalendarMonthView*)monthView marksFromDate:(NSDate*)startDate toDate:(NSDate*)lastDate
{
    [self getActivitiesData:startDate endDate:lastDate];
	return self.dataArray;
}

- (void) calendarMonthView:(TKCalendarMonthView*)monthView didSelectDate:(NSDate*)date
{	
	// CHANGE THE DATE TO YOUR TIMEZONE
	TKDateInformation info = [date dateInformationWithTimeZone:[NSTimeZone timeZoneForSecondsFromGMT:0]];
	NSDate *myTimeZoneDay = [NSDate dateFromDateInformation:info timeZone:[NSTimeZone systemTimeZone]];
	
	NSLog(@"Date Selected: %@",myTimeZoneDay);
	
	[self.tableView reloadData];
}

- (void) calendarMonthView:(TKCalendarMonthView*)mv monthDidChange:(NSDate*)d animated:(BOOL)animated
{
	[super calendarMonthView:mv monthDidChange:d animated:animated];
	[self.tableView reloadData];
}

#pragma mark - UITableView Delegate & DataSource

- (NSInteger) numberOfSectionsInTableView:(UITableView *)tableView
{
	return 1;	
}

- (UIView *) tableView:(UITableView *)tableView viewForHeaderInSection:(NSInteger)section
{
    return nil;
}

- (CGFloat) tableView:(UITableView *) tableView heightForHeaderInSection:(NSInteger) section
{
    if ([[UIDevice currentDevice] userInterfaceIdiom] == UIUserInterfaceIdiomPad)
    {
        return 25;
    }
    else
    {
        return 0;
    }
}

- (NSInteger) tableView:(UITableView *)tableView numberOfRowsInSection:(NSInteger)section
{
	NSArray *ar = [self.dataDictionary objectForKey:[self.monthView dateSelected]];
	if(ar == nil) return 0;
	return [ar count];
}

- (UITableViewCell *) tableView:(UITableView *)tv cellForRowAtIndexPath:(NSIndexPath *)indexPath
{
    
    static NSString *CellIdentifier = @"Cell";
    UITableViewCell *cell = [tv dequeueReusableCellWithIdentifier:CellIdentifier];
    if (cell == nil) cell = [[UITableViewCell alloc] initWithStyle:UITableViewCellStyleDefault reuseIdentifier:CellIdentifier];

	NSArray *ar = [self.dataDictionary objectForKey:[self.monthView dateSelected]];
	cell.textLabel.text = [ar objectAtIndex:indexPath.row];
	
    return cell;
	
}

- (void) getActivitiesData:(NSDate*)start endDate:(NSDate*)end
{
	NSLog(@"Delegate Range: %@ %@ %d",start,end,[start daysBetweenDate:end]);
    
	self.dataArray = [NSMutableArray array];
	self.dataDictionary = [NSMutableDictionary dictionary];
	
	while(YES)
    {
        NSArray *nameOfActivitiesOccuringOnStartDate = [self getListOfActivitiesForDate:start];
        
        if ( [nameOfActivitiesOccuringOnStartDate count ] > 0 )
        {
			[self.dataDictionary setObject:nameOfActivitiesOccuringOnStartDate forKey:start];
			[self.dataArray addObject:[NSNumber numberWithBool:YES]];
		}
        else
        {
			[self.dataArray addObject:[NSNumber numberWithBool:NO]];
        }
		
		TKDateInformation info = [start dateInformationWithTimeZone:[NSTimeZone timeZoneForSecondsFromGMT:0]];
		info.day++;
		start = [NSDate dateFromDateInformation:info timeZone:[NSTimeZone timeZoneForSecondsFromGMT:0]];        
		if([start compare:end]==NSOrderedDescending)
            break;
	}
}

- (NSArray*) getListOfActivitiesForDate:(NSDate*)startDate
{
    NSMutableArray *temp = [NSMutableArray array];
    NSDateFormatter *formatter = [[NSDateFormatter alloc]init];
    [formatter setDateFormat:@"yyyy-MM-dd"];
    NSString *strStartDate = [formatter stringFromDate:[startDate dateByAddingTimeInterval:60*60*24*1]];
    
    for(NSMutableDictionary *activity in self.activitiesArray)
    {
        if([activity[@"date"] isEqual:strStartDate])
        {
            NSMutableString *activityName = [[NSMutableString alloc] init];
            [activityName appendFormat:@"%@ %@ kilometers for %@ minutes (Maximum speed: %@ km/h)", activity[@"type"], activity[@"distance"], activity[@"duration"], activity[@"max_speed"]];
            [temp addObject:activityName];
        }
    }
    
    NSArray *result = temp;
    
    return result;
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
