//
//  ActivityViewController.h
//  CardioQuest
//
//  Created by Philip Latka on 2013-03-08.
//  Copyright (c) 2013 comp4350group5. All rights reserved.
//

#import <UIKit/UIKit.h>

@interface ActivityViewController : UIViewController <UITableViewDelegate, UITableViewDataSource>
@property (weak, nonatomic) IBOutlet UITableView *activityTable;
-(void) populateTable;
@end
