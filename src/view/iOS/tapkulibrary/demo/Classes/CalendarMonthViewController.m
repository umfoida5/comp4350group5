//
//  DemoCalendarMonth.m
//  Created by Devin Ross on 10/31/09.
//
/*
 
 tapku.com || https://github.com/devinross/tapkulibrary
 
 Permission is hereby granted, free of charge, to any person
 obtaining a copy of this software and associated documentation
 files (the "Software"), to deal in the Software without
 restriction, including without limitation the rights to use,
 copy, modify, merge, publish, distribute, sublicense, and/or sell
 copies of the Software, and to permit persons to whom the
 Software is furnished to do so, subject to the following
 conditions:
 
 The above copyright notice and this permission notice shall be
 included in all copies or substantial portions of the Software.
 
 THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
 EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
 OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
 NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
 HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
 WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
 FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
 OTHER DEALINGS IN THE SOFTWARE.
 
 */

#import "CalendarMonthViewController.h"
#import "AppDelegate.h"

@implementation CalendarMonthViewController

#pragma mark - View Lifecycle

-(IBAction)CancelClicked:(id)sender
{
    if([self respondsToSelector:@selector(dismissViewControllerAnimated:completion:)])
    {
        [self dismissViewControllerAnimated:YES completion:Nil];
    }
    else
    {
        [self dismissModalViewControllerAnimated:YES];
    } 
    
}
- (void) viewDidLoad{
	[super viewDidLoad];
	[self.monthView selectDate:[NSDate month]];
    UIButton *cancelBtn = [UIButton buttonWithType:UIButtonTypeCustom];
    [cancelBtn setFrame:CGRectMake(0, 0, 60, 40)];
    [cancelBtn setTitle:@"Cancel" forState:UIControlStateNormal];
    [cancelBtn addTarget:self action:@selector(CancelClicked:) forControlEvents:UIControlEventTouchUpInside];
    UIBarButtonItem *cancelButtonItem = [[UIBarButtonItem alloc] initWithCustomView:cancelBtn];
    self.navigationItem.leftBarButtonItem = cancelButtonItem;
}



#pragma mark - MonthView Delegate & DataSource
- (NSArray*) calendarMonthView:(TKCalendarMonthView*)monthView marksFromDate:(NSDate*)startDate toDate:(NSDate*)lastDate{
	[self generateRandomDataForStartDate:startDate endDate:lastDate];
	return self.dataArray;
}
- (void) calendarMonthView:(TKCalendarMonthView*)monthView didSelectDate:(NSDate*)date{
	
	// CHANGE THE DATE TO YOUR TIMEZONE
	TKDateInformation info = [date dateInformationWithTimeZone:[NSTimeZone timeZoneForSecondsFromGMT:0]];
	NSDate *myTimeZoneDay = [NSDate dateFromDateInformation:info timeZone:[NSTimeZone systemTimeZone]];
	
	NSLog(@"Date Selected: %@",myTimeZoneDay);
	
	[self.tableView reloadData];
}
- (void) calendarMonthView:(TKCalendarMonthView*)mv monthDidChange:(NSDate*)d animated:(BOOL)animated{
	[super calendarMonthView:mv monthDidChange:d animated:animated];
	[self.tableView reloadData];
}


#pragma mark - UITableView Delegate & DataSource

- (NSInteger) numberOfSectionsInTableView:(UITableView *)tableView {
	return 1;
	
}

- (UIView *) tableView:(UITableView *)tableView viewForHeaderInSection:(NSInteger)section
{
    if ([[UIDevice currentDevice] userInterfaceIdiom]==UIUserInterfaceIdiomPad)
    {
        NSArray *views =[[NSBundle mainBundle] loadNibNamed:@"CalendarTableHeader" owner:nil options:nil];
        UIView *headerView=[views objectAtIndex:0];
        return headerView;
    }
    else
    {
        return nil;
    }
}

- (CGFloat) tableView:(UITableView *) tableView heightForHeaderInSection:(NSInteger) section {
    if ([[UIDevice currentDevice] userInterfaceIdiom] == UIUserInterfaceIdiomPad) {
        return 25;
    } else {
        return 0;
    }
}


- (NSInteger) tableView:(UITableView *)tableView numberOfRowsInSection:(NSInteger)section {	
	NSArray *ar = [self.dataDictionary objectForKey:[self.monthView dateSelected]];
	if(ar == nil) return 0;
	return [ar count];
}
- (UITableViewCell *) tableView:(UITableView *)tv cellForRowAtIndexPath:(NSIndexPath *)indexPath {
    
    static NSString *CellIdentifier = @"Cell";
    UITableViewCell *cell = [tv dequeueReusableCellWithIdentifier:CellIdentifier];
    if (cell == nil) cell = [[UITableViewCell alloc] initWithStyle:UITableViewCellStyleDefault reuseIdentifier:CellIdentifier];
    
	
    
	NSArray *ar = [self.dataDictionary objectForKey:[self.monthView dateSelected]];
	cell.textLabel.text = [ar objectAtIndex:indexPath.row];
	
    return cell;
	
}


- (void) generateRandomDataForStartDate:(NSDate*)start endDate:(NSDate*)end{
	// this function sets up dataArray & dataDictionary
	// dataArray: has boolean markers for each day to pass to the calendar view (via the delegate function)
	// dataDictionary: has items that are associated with date keys (for tableview)
	
	
	NSLog(@"Delegate Range: %@ %@ %d",start,end,[start daysBetweenDate:end]);
	
	self.dataArray = [NSMutableArray array];
	self.dataDictionary = [NSMutableDictionary dictionary];
	
	NSDate *d = start;
	while(YES){
		
		int r = arc4random();
		if(r % 3==1){
			[self.dataDictionary setObject:[NSArray arrayWithObjects:@"Item one",@"Item two",nil] forKey:d];
			[self.dataArray addObject:[NSNumber numberWithBool:YES]];
			
		}else if(r%4==1){
			[self.dataDictionary setObject:[NSArray arrayWithObjects:@"Item one",nil] forKey:d];
			[self.dataArray addObject:[NSNumber numberWithBool:YES]];
			
		}else
			[self.dataArray addObject:[NSNumber numberWithBool:NO]];
		
		
		TKDateInformation info = [d dateInformationWithTimeZone:[NSTimeZone timeZoneForSecondsFromGMT:0]];
		info.day++;
		d = [NSDate dateFromDateInformation:info timeZone:[NSTimeZone timeZoneForSecondsFromGMT:0]];
		if([d compare:end]==NSOrderedDescending) break;
	}
	
}

-(void) didRotateFromInterfaceOrientation:(UIInterfaceOrientation)fromInterfaceOrientation
{
    [self updateTableOffset:YES];
}


- (BOOL) shouldAutorotateToInterfaceOrientation:(UIInterfaceOrientation)interfaceOrientation {
	return YES;
}


@end
