//
//  CDQEventsViewController_test.h
//  CardioQuest
//
//  Created by Blake Andrew Beatty on 2013-03-17.
//  Copyright (c) 2013 comp4350group5. All rights reserved.
//

#import <SenTestingKit/SenTestingKit.h>
#import "CDQLoginController.h"
#import "CDQEventsController.h"

@interface CDQEventsViewController_test : SenTestCase
@property (strong, nonatomic) CDQEventsController *eventsController;
@property (strong, nonatomic) CDQLoginController   *homeController;
@end
