//
//  CardioQuestTests.m
//  CardioQuestTests
//
//  Created by Philip Latka on 2013-03-04.
//  Copyright (c) 2013 comp4350group5. All rights reserved.
//

#import "CDQHomeController_test.h"
#import "CDQHomeViewController.h"

@interface CDQHomeController_test ()

@end

@implementation CDQHomeController_test
- (void)setUp
{
    [super setUp];
    
    UIStoryboard *storyboard = [UIStoryboard storyboardWithName:@"MainStoryboard_iPad" bundle:nil];
    
    self.homeController = [storyboard instantiateViewControllerWithIdentifier:@"Home"];
    [self.homeController performSelectorOnMainThread:@selector(loadView) withObject:nil waitUntilDone:YES];

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
// waits for logout completion
//
- (BOOL)waitForCompletion:(NSTimeInterval)timeoutSecs {
    NSDate *timeoutDate = [NSDate dateWithTimeIntervalSinceNow:timeoutSecs];
    
    while (self.homeController.navBar.rightBarButtonItem == nil) {
        [[NSRunLoop currentRunLoop] runMode:NSDefaultRunLoopMode beforeDate:timeoutDate];
        if([timeoutDate timeIntervalSinceNow] < 0.0)
            return NO;
    }
    
    return YES;
}

// -- ASYNCHRONOUS TEST --
//
// testDoLogout()
//
// Tests to see that a do logout request is successful
//
- (void)testDoLogout
{
    // Log user in
    [self.loginController loginRequest:@"ios_unit_test" password:@"ios_unit_test"];

    [self.homeController doLogout:self];
    // Tests the home page to see that logout was successful
    STAssertTrue([self waitForCompletion:3.0], @"Login timed out");
}

//
// testToggleNavBarItems
//
// Tests to ensure that the visible nav bar item is toggled
//
- (void) testToggleNavBarButtons
{
    
    STAssertTrue(self.homeController.navBar.leftBarButtonItem != nil ||
                 self.homeController.navBar.rightBarButtonItem != nil,
                 @"Both buttons displayed");
    
    [self.homeController toggleNavBarButtons:YES];
    
    STAssertTrue(self.homeController.navBar.leftBarButtonItem != nil &&
                 self.homeController.navBar.rightBarButtonItem == nil,
                 @"Logout buttons not displayed");

    [self.homeController toggleNavBarButtons:NO];
    
    STAssertTrue(self.homeController.navBar.leftBarButtonItem == nil &&
                 self.homeController.navBar.rightBarButtonItem != nil,
                 @"Login buttons not displayed");
}

@end