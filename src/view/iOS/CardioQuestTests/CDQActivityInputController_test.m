//
//  CDQActivityInputController_test.m
//  CardioQuest
//
//  Created by Blake Beatty on 2013-03-23.
//  Copyright (c) 2013 comp4350group5. All rights reserved.
//

#import "CDQActivityInputController_test.h"

@implementation CDQActivityInputController_test
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
    
    self.aiController = [storyboard instantiateViewControllerWithIdentifier:@"ActivityInputController"];
    [self.aiController performSelectorOnMainThread:@selector(loadView) withObject:nil waitUntilDone:YES];
    
    self.avController = [storyboard instantiateViewControllerWithIdentifier:@"Activities"];
    [self.avController performSelectorOnMainThread:@selector(loadView) withObject:nil waitUntilDone:YES];
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
    while ([[self.avController activityTable]numberOfRowsInSection:0] <= 1) {
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
- (void)testCreatingANewActivity
{
    // Tests goals page to see that no records are populated when no user is logged in
    [self.aiController createActivity:@"ActivityInputController"];
    STAssertFalse([self waitForCompletion:3.0], @"Activity Creation Timed out");
    
}
@end
