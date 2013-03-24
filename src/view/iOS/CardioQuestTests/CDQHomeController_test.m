//
//  CardioQuestTests.m
//  CardioQuestTests
//
//  Created by Philip Latka on 2013-03-04.
//  Copyright (c) 2013 comp4350group5. All rights reserved.
//

#import "CDQHomeController_test.h"
#import "CDQHomeController.h"

@interface CDQHomeController_test ()

@property (strong, nonatomic) CDQHomeController *homeController;

@end

@implementation CDQHomeController_test

BOOL done;

- (void)setUp
{
    [super setUp];
    
    UIStoryboard *storyboard = [UIStoryboard storyboardWithName:@"MainStoryboard_iPad" bundle:nil];
    
    /*
     * To set the identifier string below:
     * - Go to the iPad storyboard
     * - Click the view you are testing
     * - Make sure the right pane is visable by clicking the button in the top right
     * - On the third tab on the right set the "Storyboard ID"
     * - Set the identifier string below to the same
     */
    self.homeController = [storyboard instantiateViewControllerWithIdentifier:@"Home"];
    [self.homeController performSelectorOnMainThread:@selector(loadView) withObject:nil waitUntilDone:YES];
}

- (void)tearDown
{
    [super tearDown];
}

- (BOOL)waitForCompletion:(NSTimeInterval)timeoutSecs {
    NSDate *timeoutDate = [NSDate dateWithTimeIntervalSinceNow:timeoutSecs];
    
    while ([[self.homeController getLoginLabelText] isEqualToString:@"Press the Login button to Login :)"]) {
        [[NSRunLoop currentRunLoop] runMode:NSDefaultRunLoopMode beforeDate:timeoutDate];
        if([timeoutDate timeIntervalSinceNow] < 0.0)
            return NO;
    }
    
    return YES;
}

//
// testBlankLoginFailure
//
// tests to ensure that an blank login results in "Invalid username."
//
- (void)testBlankLoginFailure
{   
    [self.homeController loginRequest:@"" password:@""];
    
    STAssertTrue([self waitForCompletion:3.0], @"Login timed out");
    
    NSLog(@"%@", [self.homeController getLoginLabelText]);
    STAssertTrue([[self.homeController getLoginLabelText] isEqualToString:@"Invalid username."], @"Login succeded but it shouldn't have");
}

//
// testLoginInvalidUserFail
//
// tests to ensure that a login as an invalid user fails
//
- (void)testLoginInvalidUserFail
{
    [self.homeController loginRequest:@"ThisUserShouldNeverExist" password:@"password"];
    
    STAssertTrue([self waitForCompletion:3.0], @"Login timed out");
    
    STAssertTrue([[self.homeController getLoginLabelText] isEqualToString:@"Invalid username."], @"Login succeded but it shouldn't have");
}

//
// testValidSuccess
//
// tests to ensure that a login as an valid user succeeds
//
- (void)testLoginSuccess
{
    [self.homeController loginRequest:@"justin" password:@"justin"];
    
    STAssertTrue([self waitForCompletion:3.0], @"Login timed out");
    
    STAssertTrue([[self.homeController getLoginLabelText] isEqualToString:@"Login was successful."], @"Login should have succeeded");
}

//
// testDoLogout
//
// Tests to ensure that a logout was successful
//
- (void)testDoLogout
{
    [self.homeController loginRequest:@"justin" password:@"justin"];
    
    [self.homeController doLogout];
    STAssertTrue([self waitForCompletion:3.0], @"Logout timed out");
    
    NSLog(@"%@", [self.homeController getLoginLabelText]);
    STAssertTrue([[self.homeController getLoginLabelText] isEqualToString:@"Logout was successful."], @"Logout failed");
}

@end
