//
//  CDQHomeController.h
//  CardioQuest
//
//  Created by Justin Foidart on 2013-03-08.
//  Copyright (c) 2013 comp4350group5. All rights reserved.
//

#import <UIKit/UIKit.h>

@interface CDQLoginController : UIViewController <UITableViewDelegate, UITableViewDataSource>
    - (IBAction)login:(id)sender;
    - (void)loginRequest:(NSString*)username password:(NSString*)password;
@end
