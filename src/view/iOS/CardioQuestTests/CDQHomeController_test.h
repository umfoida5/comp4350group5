//
//  CardioQuestTests.h
//  CardioQuestTests
//
//  Created by Philip Latka on 2013-03-04.
//  Copyright (c) 2013 comp4350group5. All rights reserved.
//

#import <SenTestingKit/SenTestingKit.h>
#import "CDQHomeViewController.h"
#import "CDQLoginController.h"

@interface CDQHomeController_test : SenTestCase
@property (strong, nonatomic) CDQHomeViewController *homeController;
@property (strong, nonatomic) CDQLoginController *loginController;
@end
