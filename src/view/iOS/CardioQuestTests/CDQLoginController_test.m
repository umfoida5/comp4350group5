//
//  CDQLoginController_test.m
//  CardioQuest
//
//  Created by Blake Beatty on 2013-03-23.
//  Copyright (c) 2013 comp4350group5. All rights reserved.
//

#import "CDQLoginController_test.h"
#import "CDQLoginController.h"

@interface CDQLoginController_test ()

@property (strong, nonatomic) CDQLoginController *loginController;

@end

@implementation CDQLoginController_test

BOOL done;

- (void)setUp
{
    [super setUp];
    
    UIStoryboard *storyboard = [UIStoryboard storyboardWithName:@"MainStoryboard_iPad" bundle:nil];
    
    self.loginController = [storyboard instantiateViewControllerWithIdentifier:@"Authentication"];
    [self.loginController performSelectorOnMainThread:@selector(loadView) withObject:nil waitUntilDone:YES];
}

- (void)tearDown
{
    [super tearDown];
}

- (BOOL)waitForCompletion:(NSTimeInterval)timeoutSecs {
    NSDate *timeoutDate = [NSDate dateWithTimeIntervalSinceNow:timeoutSecs];
    
    
    while ([self.loginController.loginResponseLabel.text isEqualToString:@"Press the Login button to Login :)"]) {
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
    [self.loginController loginRequest:@"" password:@""];
    
    STAssertTrue([self waitForCompletion:3.0], @"Login timed out");
    
    //NSLog(@"%@", [self.loginController getLoginLabelText]);
    //STAssertTrue([[self.loginController getLoginLabelText] isEqualToString:@"Invalid username."], @"Login succeded but it shouldn't have");
}

//
// testLoginInvalidUserFail
//
// tests to ensure that a login as an invalid user fails
//
- (void)testLoginInvalidUserFail
{
    [self.loginController loginRequest:@"ThisUserShouldNeverExist" password:@"password"];
    
    STAssertTrue([self waitForCompletion:3.0], @"Login timed out");
    
    //STAssertTrue([[self.loginController getLoginLabelText] isEqualToString:@"Invalid username."], @"Login succeded but it shouldn't have");
}

//
// testValidSuccess
//
// tests to ensure that a login as an valid user succeeds
//
- (void)testLoginSuccess
{
    [self.loginController loginRequest:@"ios_unit_test" password:@"ios_unit_test"];
    //BOOL result = [self.loginController isUserLoggedIn];
    STAssertTrue([self waitForCompletion:3.0], @"Login timed out");
    
    STAssertTrue([self.loginController.loginResponseLabel.text isEqualToString:@"Login was successful."], @"Login should have succeeded");
}

//
// testDoLogout
//
// Tests to ensure that a logout was successful
//
- (void)testDoLogout
{
    [self.loginController loginRequest:@"ios_unit_test" password:@"ios_unit_test"];
    
    //[self.loginController doLogout];
    STAssertTrue([self waitForCompletion:3.0], @"Logout timed out");
    
    //NSLog(@"%@", [self.loginController getLoginLabelText]);
    //STAssertTrue([[self.loginController getLoginLabelText] isEqualToString:@"Logout was successful."], @"Logout failed");
}

@end