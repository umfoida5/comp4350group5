//
//  CDQHomeViewController.h
//  CardioQuest
//
//  Created by Alex Salomon Thome Da Silva on 3/21/13.
//  Copyright (c) 2013 comp4350group5. All rights reserved.
//

#import <UIKit/UIKit.h>

@interface CDQHomeViewController : UIViewController
@property (strong, nonatomic) IBOutlet UIBarButtonItem *logoutButton;
@property (strong, nonatomic) IBOutlet UIBarButtonItem *loginButton;
@property (strong, nonatomic) IBOutlet UINavigationItem *navBar;

- (IBAction)doLogout:(id)sender;
- (void)toggleNavBarButtons:(BOOL)isLoggedIn;
@end
