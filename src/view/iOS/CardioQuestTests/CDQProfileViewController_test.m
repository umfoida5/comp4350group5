//
//  CDQProfileViewController_test.m
//  CardioQuest
//
//  Created by Blake Andrew Beatty on 2013-03-17.
//  Copyright (c) 2013 comp4350group5. All rights reserved.
//

#import "CDQProfileViewController_test.h"

@implementation CDQProfileViewController_test

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
    
    self.profileController = [storyboard instantiateViewControllerWithIdentifier:@"Profile"];
    [self.profileController performSelectorOnMainThread:@selector(loadView) withObject:nil waitUntilDone:YES];
    
    self.loginController = [storyboard instantiateViewControllerWithIdentifier:@"Authentication"];
    [self.loginController performSelectorOnMainThread:@selector(loadView) withObject:nil waitUntilDone:YES];
    
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
    
    while ([self.profileController.nameLabel.text isEqualToString :@"Connection Failure"]) {
        [[NSRunLoop currentRunLoop] runMode:NSDefaultRunLoopMode beforeDate:timeoutDate];
        if([timeoutDate timeIntervalSinceNow] < 0.0)
            return NO;
    }
    
    return YES;
}

// -- ASYNCHRONOUS TEST --
//
// testProfileBeforeLogin()
//
// Tests to see that without a login the asynchronous call returns valid objects
//
- (void)testProfileBeforeLogin
{
    NSURL *url = [NSURL URLWithString:@"http://ec2-107-21-196-190.compute-1.amazonaws.com:8000/profiles/athlete"];
    
    // Timeout test for profile page request
    [self.profileController sendRequest: url : @""];
    STAssertTrue([self waitForCompletion:3.0], @"Login timed out");
}

// -- ASYNCHRONOUS TEST --
//
// testProfileBeforeLogin()
//
// Tests to see that without a login the asynchronous call returns valid objects
//
- (void)testProfileAfterLogin
{
    NSURL *url = [NSURL URLWithString:@"http://ec2-107-21-196-190.compute-1.amazonaws.com:8000/profiles/athlete"];
    
    [self.loginController loginRequest:@"ios_unit_test" password:@"ios_unit_test"];

    // Timeout test for profile page request
    [self.profileController sendRequest: url : @""];
    STAssertTrue([self waitForCompletion:8.0], @"Login timed out");
}
              
@end