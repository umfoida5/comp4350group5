//
//  CDQProfileViewController_test.h
//  CardioQuest
//
//  Created by Blake Andrew Beatty on 2013-03-17.
//  Copyright (c) 2013 comp4350group5. All rights reserved.
//

#import <SenTestingKit/SenTestingKit.h>
#import "CDQLoginController.h"
#import "ProfileViewController.h"
#import "CDQHomeViewController.h"
@interface CDQProfileViewController_test : SenTestCase
@property (strong, nonatomic) ProfileViewController *profileController;
@property (strong, nonatomic) CDQLoginController *loginController;
@property (strong, nonatomic) CDQHomeViewController *homeController;

@end
