//
//  CDQGoalsViewController_test.m
//  CardioQuest
//
//  Created by Blake Andrew Beatty on 2013-03-17.
//  Copyright (c) 2013 comp4350group5. All rights reserved.
//

#import "CDQGoalsViewController_test.h"

@implementation CDQGoalsViewController_test

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
    
    self.goalsController = [storyboard instantiateViewControllerWithIdentifier:@"Goals"];
    [self.goalsController performSelectorOnMainThread:@selector(loadView) withObject:nil waitUntilDone:YES];
    
    self.loginController = [storyboard instantiateViewControllerWithIdentifier:@"Login"];
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
    
    while ([[self.goalsController goalsTable]numberOfRowsInSection:0] <= 0) {
        [[NSRunLoop currentRunLoop] runMode:NSDefaultRunLoopMode beforeDate:timeoutDate];
        if([timeoutDate timeIntervalSinceNow] < 0.0)
            return NO;
    }
    
    return YES;
}

// -- ASYNCHRONOUS TEST --
//
// testGoalsEmpty()
//
// Tests to see that without a login the asynchronous call returns no objects
//
- (void)testGoalsEmpty
{
    // Tests goals page to see that no records are populated when no user is logged in
    STAssertFalse([self waitForCompletion:3.0], @"Login timed out");
    [self.goalsController populateTable];
    STAssertTrue([[self.goalsController goalsTable]numberOfRowsInSection:0] <= 0, @"ERROR: Records retrieved from goals database without login");
}

// -- ASYNCHRONOUS TEST --
//
// testGoalsPopulated()
//
// Tests to see that without a login the asynchronous call returns valid objects
//
- (void)testGoalsPopulated
{
    
    // Log user in
    [self.loginController loginRequest:@"ios_unit_test" password:@"ios_unit_test"];
    
    // test that goals page populates
    [self.goalsController populateTable];
    STAssertTrue([self waitForCompletion:3.0], @"Login timed out");
    
    STAssertTrue([[self.goalsController goalsTable]numberOfRowsInSection:0] > 0, @"ERROR: Goals table is empty after login");
}

@end
