//
//  CDQHealthTableViewController_test.m
//  CardioQuest
//
//  Created by Blake Beatty on 2013-03-23.
//  Copyright (c) 2013 comp4350group5. All rights reserved.
//

#import "CDQHealthTableViewController_test.h"

@implementation CDQHealthTableViewController_test

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
    
    self.healthController = [storyboard instantiateViewControllerWithIdentifier:@"HealthView"];
    [self.healthController performSelectorOnMainThread:@selector(loadView) withObject:nil waitUntilDone:YES];
    
    self.loginController = [storyboard instantiateViewControllerWithIdentifier:@"Authentication"];
    [self.loginController performSelectorOnMainThread:@selector(loadView) withObject:nil waitUntilDone:YES];
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
    
    while ([[self.healthController healthTable]numberOfRowsInSection:0] <= 0) {
        [[NSRunLoop currentRunLoop] runMode:NSDefaultRunLoopMode beforeDate:timeoutDate];
        if([timeoutDate timeIntervalSinceNow] < 0.0)
            return NO;
    }
    
    return YES;
}

// -- ASYNCHRONOUS TEST --
//
// testHealthEmpty()
//
// Tests to see that without a login the asynchronous call returns no objects
//
- (void)testHealthEmpty
{
    // Tests goals page to see that no records are populated when no user is logged in
    STAssertFalse([self waitForCompletion:3.0], @"Login timed out");
    [self.healthController populateTable];
    STAssertTrue([[self.healthController healthTable]numberOfRowsInSection:0] <= 0, @"ERROR: Records retrieved from health database without login");
}

// -- ASYNCHRONOUS TEST --
//
// testHealthPopulated()
//
// Tests to see that without a login the asynchronous call returns valid objects
//
- (void)testHealthPopulated
{
    
    // Log user in
    [self.loginController loginRequest:@"ios_unit_test" password:@"ios_unit_test"];
    
    // test that goals page populates
    [self.healthController populateTable];
    STAssertTrue([self waitForCompletion:3.0], @"Login timed out");
    
    STAssertTrue([[self.healthController healthTable]numberOfRowsInSection:0] > 0, @"ERROR: Health table is empty after login");
}

@end
