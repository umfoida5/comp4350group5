//
//  CDQHealthTableViewController.h
//  CardioQuest
//
//  Created by Blake Beatty on 2013-03-23.
//  Copyright (c) 2013 comp4350group5. All rights reserved.
//

#import <UIKit/UIKit.h>

@interface CDQHealthTableViewController : UIViewController
@property (weak, nonatomic) IBOutlet UITableView *healthTable;
-(void) populateTable;
@end
