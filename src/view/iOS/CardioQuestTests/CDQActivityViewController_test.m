//
//  CDQActivityViewController_test.m
//  CardioQuest
//
//  Created by Blake Andrew Beatty on 2013-03-17.
//  Copyright (c) 2013 comp4350group5. All rights reserved.
//

#import "CDQActivityViewController_test.h"

@implementation CDQActivityViewController_test

//
// setUp()
//
// performs initial setup for tests, sets storyboard to the ipad storyboard
// and sets the goalsController to the Goals
//
- (void)setUp
{
    [super setUp];
    
    UIStoryboard *storyboard = [UIStoryboard storyboardWithName:@"MainStoryboard_iPad" bundle:nil];
    
    self.activitiesController = [storyboard instantiateViewControllerWithIdentifier:@"Activities"];
    [self.activitiesController performSelectorOnMainThread:@selector(loadView) withObject:nil waitUntilDone:YES];
    
    self.homeController = [storyboard instantiateViewControllerWithIdentifier:@"Home"];
    [self.homeController performSelectorOnMainThread:@selector(loadView) withObject:nil waitUntilDone:YES];
}

//
// tearDown()
//
// performs tear down functionality
//
- (void)tearDown
{
    [super tearDown];
}

//
// waitForCompletion()
//
// checks checks goals table for data
//
- (BOOL)waitForCompletion:(NSTimeInterval)timeoutSecs {
    NSDate *timeoutDate = [NSDate dateWithTimeIntervalSinceNow:timeoutSecs];
    
    while ([[self.activitiesController activityTable]numberOfRowsInSection:0] <= 0) {
        [[NSRunLoop currentRunLoop] runMode:NSDefaultRunLoopMode beforeDate:timeoutDate];
        if([timeoutDate timeIntervalSinceNow] < 0.0)
            return NO;
    }
    
    return YES;
}

// -- ASYNCHRONOUS TEST --
//
// testEventsBeforeLogin()
//
// Tests to see that without a login the asynchronous call returns valid objects
//
- (void)testEventsBeforeLogin
{
    // Tests goals page to see that no records are populated when no user is logged in
    STAssertFalse([self waitForCompletion:3.0], @"Login timed out");
    STAssertTrue([[self.activitiesController activityTable]numberOfRowsInSection:0] <= 0, @"ERROR: Records retrieved from activities events before login");
}

// -- ASYNCHRONOUS TEST --
//
// testEventsAfterLogin()
//
// Tests to see that without a login the asynchronous call returns valid objects
//
- (void)testEventsAfterLogin
{
    
    // Log user in
    [self.homeController loginRequest:@"justin" password:@"justin"];
    
    // test that goals page populates
    [self.activitiesController populateTable];
    STAssertTrue([self waitForCompletion:3.0], @"Login timed out");
    
    STAssertTrue([[self.activitiesController activityTable]numberOfRowsInSection:0] > 0, @"ERROR: No records retrieved from activities database after login");
}

@end
