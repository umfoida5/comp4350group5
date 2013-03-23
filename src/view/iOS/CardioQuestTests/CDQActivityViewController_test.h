//
//  CDQActivityViewController_test.h
//  CardioQuest
//
//  Created by Blake Andrew Beatty on 2013-03-17.
//  Copyright (c) 2013 comp4350group5. All rights reserved.
//

#import <SenTestingKit/SenTestingKit.h>
#import "ActivityViewController.h"
#import "CDQLoginController.h"

@interface CDQActivityViewController_test : SenTestCase
@property (strong, nonatomic) ActivityViewController  *activitiesController;
@property (strong, nonatomic) CDQLoginController      *homeController;
@end
