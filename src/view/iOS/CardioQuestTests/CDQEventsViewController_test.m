//
//  CDQEventsViewController_test.m
//  CardioQuest
//
//  Created by Blake Andrew Beatty on 2013-03-17.
//  Copyright (c) 2013 comp4350group5. All rights reserved.
//

#import "CDQEventsViewController_test.h"

@implementation CDQEventsViewController_test

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
    
    self.eventsController = [storyboard instantiateViewControllerWithIdentifier:@"Events"];
    [self.eventsController performSelectorOnMainThread:@selector(loadView) withObject:nil waitUntilDone:YES];
    
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
    
    while ([[self.eventsController eventsTable]numberOfRowsInSection:0] <= 0) {
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
    [self.eventsController populateTable];
    STAssertTrue([self waitForCompletion:3.0], @"Login timed out");
    STAssertTrue([[self.eventsController eventsTable]numberOfRowsInSection:0] > 0, @"ERROR: No records retrieved from events events before login");
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
    [self.homeController loginRequest:@"ios_test_user" password:@"ios"];
    
    // test that goals page populates
    [self.eventsController populateTable];
    STAssertTrue([self waitForCompletion:3.0], @"Login timed out");
    
    STAssertTrue([[self.eventsController eventsTable]numberOfRowsInSection:0] > 0, @"ERROR: No records retrieved from events database after login");
}
@end
