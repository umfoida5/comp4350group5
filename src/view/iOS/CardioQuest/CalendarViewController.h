//
//  CalendarViewController.h
//  CardioQuest
//
//  Created by Philip Latka on 2013-03-08.
//  Copyright (c) 2013 comp4350group5. All rights reserved.
//

#import <UIKit/UIKit.h>
#import "Kal.h"

@interface CalendarViewController : UIViewController <UIApplicationDelegate, UITableViewDelegate>
{
    UIWindow *window;
    UINavigationController *navController;
    KalViewController *kal;
    id dataSource;
}

@property (nonatomic, retain) IBOutlet UIWindow *window;

@end
