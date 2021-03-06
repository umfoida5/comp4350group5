//
//  CDQHealthTableViewController_test.h
//  CardioQuest
//
//  Created by Blake Beatty on 2013-03-23.
//  Copyright (c) 2013 comp4350group5. All rights reserved.
//

#import <SenTestingKit/SenTestingKit.h>
#import "CDQHealthTableViewController.h"
#import "CDQLoginController.h"

@interface CDQHealthTableViewController_test : SenTestCase
@property (strong, nonatomic) CDQHealthTableViewController *healthController;
@property (strong, nonatomic) CDQLoginController *loginController;
@end
