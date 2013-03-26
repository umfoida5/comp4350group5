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
- (void)do_signup:(NSString*)username password:(NSString*)password firstname:(NSString*)firstname lastname:(NSString*)lastname;
- (IBAction)signup:(id)sender;
- (IBAction)logout:(id)sender;
    //Login Stuff:
    @property (weak, nonatomic) IBOutlet UILabel *loginTitle;
    @property (weak, nonatomic) IBOutlet UITextField *loginUsernameField;
    @property (weak, nonatomic) IBOutlet UITextField *loginPasswordField;
    @property (weak, nonatomic) IBOutlet UILabel *loginUsernameLabel;
    @property (weak, nonatomic) IBOutlet UILabel *loginPasswordLabel;
    @property (weak, nonatomic) IBOutlet UIButton *loginButton;
    @property (weak, nonatomic) IBOutlet UILabel *loginResponseLabel;

    //Signup Stuff:
    @property (weak, nonatomic) IBOutlet UILabel *signupTitle;
    @property (weak, nonatomic) IBOutlet UITextField *signupUsernameField;
    @property (weak, nonatomic) IBOutlet UITextField *signupPasswordField;
    @property (weak, nonatomic) IBOutlet UITextField *signupFirstnameField;
    @property (weak, nonatomic) IBOutlet UITextField *signupLastnameField;
    @property (weak, nonatomic) IBOutlet UILabel *signupUsernameLabel;
    @property (weak, nonatomic) IBOutlet UILabel *signupPasswordLabel;
    @property (weak, nonatomic) IBOutlet UILabel *signupFirstnameLabel;
    @property (weak, nonatomic) IBOutlet UITextField *signupLastnameLabel;
    @property (weak, nonatomic) IBOutlet UIButton *signupButton;
    @property (weak, nonatomic) IBOutlet UILabel *signupResponseLabel;
@end
