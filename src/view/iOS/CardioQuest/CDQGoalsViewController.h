//
//  CDQGoalsViewController.h
//  CardioQuest
//
//  Created by Blake Andrew Beatty on 2013-03-12.
//  Copyright (c) 2013 comp4350group5. All rights reserved.
//

#import <UIKit/UIKit.h>

@interface CDQGoalsViewController : UIViewController <UITableViewDelegate, UITableViewDataSource>
@property (weak, nonatomic) IBOutlet UITableView *goalsTable;

-(void)populateTable;
@end
