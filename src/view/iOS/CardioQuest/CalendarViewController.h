//
//  CalendarViewController.h
//  CardioQuest
//
//  Created by Philip Latka on 2013-03-08.
//  Copyright (c) 2013 comp4350group5. All rights reserved.
//

#import <UIKit/UIKit.h>
#import <TapkuLibrary.h>

@interface CalendarViewController : TKCalendarMonthTableViewController

@property (strong,nonatomic) NSMutableArray *activitiesArray;
@property (strong,nonatomic) NSMutableArray *dataArray;
@property (strong,nonatomic) NSMutableDictionary *dataDictionary;

- (void) getActivitiesData:(NSDate*)start endDate:(NSDate*)end;

@end

