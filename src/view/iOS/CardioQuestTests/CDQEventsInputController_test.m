//
//  CDQEventsInputController_test.m
//  CardioQuest
//
//  Created by Blake Beatty on 2013-03-23.
//  Copyright (c) 2013 comp4350group5. All rights reserved.
//

#import "CDQEventsInputController_test.h"

@implementation CDQEventsInputController_test

// setUp()
//
// performs initial setup for tests, sets storyboard to the ipad storyboard
// and sets the goalsController to the Goals
//
- (void)setUp
{
    [super setUp];
    
    UIStoryboard *storyboard = [UIStoryboard storyboardWithName:@"MainStoryboard_iPad" bundle:nil];
    
    self.eiController = [storyboard instantiateViewControllerWithIdentifier:@"EventInputController"];
    [self.eiController performSelectorOnMainThread:@selector(loadView) withObject:nil waitUntilDone:YES];
    
    self.eventController = [storyboard instantiateViewControllerWithIdentifier:@"Events"];
    [self.eventController performSelectorOnMainThread:@selector(loadView) withObject:nil waitUntilDone:YES];
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
    while ([[self.eventController eventsTable]numberOfRowsInSection:0] <= 1) {
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
- (void)testCreatingANewHealth
{
    // Tests goals page to see that no records are populated when no user is logged in
    [self.eiController postEvent:@"eventInputController"];
    STAssertFalse([self waitForCompletion:3.0], @"Health Record Creation Timed out");
}

@end
