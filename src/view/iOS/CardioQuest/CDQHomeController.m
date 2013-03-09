//
//  CDQHomeController.m
//  CardioQuest
//
//  Created by Justin Foidart on 2013-03-08.
//  Copyright (c) 2013 comp4350group5. All rights reserved.
//

#import "CDQHomeController.h"

@interface CDQHomeController ()

@property (weak, nonatomic) IBOutlet UIButton *loginBtn;
@property (weak, nonatomic) IBOutlet UIButton *signupBtn;
@property (weak, nonatomic) IBOutlet UIButton *logoutBtn;
@property (weak, nonatomic) IBOutlet UITextField *loginUsername;
@property (weak, nonatomic) IBOutlet UITextField *loginPassword;
@property (weak, nonatomic) IBOutlet UITextField *signupUsername;
@property (weak, nonatomic) IBOutlet UITextField *signupPassword;
@property (weak, nonatomic) IBOutlet UITextField *signupFirstName;
@property (weak, nonatomic) IBOutlet UITextField *signupLastName;

@end

@implementation CDQHomeController
- (IBAction)login:(id)sender
{
    //Add login code.
}

- (IBAction)signup:(id)sender
{
    //Add signup code.
}

- (IBAction)changeUser:(id)sender
{
    // Add logout code.
}

- (id)initWithNibName:(NSString *)nibNameOrNil bundle:(NSBundle *)nibBundleOrNil
{
    self = [super initWithNibName:nibNameOrNil bundle:nibBundleOrNil];
    if (self) {
        // Custom initialization
    }
    return self;
}

- (void)viewDidLoad
{
    [super viewDidLoad];
    
	[self.logoutBtn setHidden:YES];
    self.view.backgroundColor = [[UIColor alloc] initWithPatternImage:[UIImage imageNamed:@"CardioQuestMain.jpeg"]];
    
}

- (void)didReceiveMemoryWarning
{
    [super didReceiveMemoryWarning];
    // Dispose of any resources that can be recreated.
}

@end
