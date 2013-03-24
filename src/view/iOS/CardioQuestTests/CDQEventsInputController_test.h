//
//  CDQEventsInputController_test.h
//  CardioQuest
//
//  Created by Blake Beatty on 2013-03-23.
//  Copyright (c) 2013 comp4350group5. All rights reserved.
//

#import <SenTestingKit/SenTestingKit.h>
#import "CDQEventsInputController.h"
#import "CDQEventsController.h"
@interface CDQEventsInputController_test : SenTestCase
@property(strong,nonatomic) CDQEventsController* eventController;
@property(strong,nonatomic) CDQEventsInputController *eiController;
@end
