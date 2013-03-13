//
//  CardioQuestTests.m
//  CardioQuestTests
//
//  Created by Philip Latka on 2013-03-04.
//  Copyright (c) 2013 comp4350group5. All rights reserved.
//

#import "CDQHomeController_test.h"
#import "CDQHomeController.h"

@implementation CDQHomeController_test

@property (weak, nonatomic) IBOutlet UILabel *loginResponseLabel;

BOOL done;

CDQHomeController *homeController;

- (void)setUp
{
    [super setUp];
    homeController = [CDQHomeController new];
}

- (void)tearDown
{
    [super tearDown];
}

- (BOOL)waitForCompletion:(NSTimeInterval)timeoutSecs {
    NSDate *timeoutDate = [NSDate dateWithTimeIntervalSinceNow:timeoutSecs];
    
    do {
        [[NSRunLoop currentRunLoop] runMode:NSDefaultRunLoopMode beforeDate:timeoutDate];
        if([timeoutDate timeIntervalSinceNow] < 0.0)
            break;
    } while (![self.loginResponseLabel.text isEqualToString:@"Press the Login button to Login :)"]);
}

- (void)testExample
{
    //STFail(@"Unit tests are not implemented yet in CardioQuestTests");
    
    
    
    //id homeController = [[CDQHomeController alloc] init];
    //[homeController login:(NULL)];
    
    [homeController loginRequest:@"test" password:@"test"];
    
    STAssertTrue([self waitForCompletion:90.0], @"Login timed out");
    STAssertFalse([self.loginResponseLabel.text isEqualToString:@"Invalid username."], @"Login failed");
    
}

@end
