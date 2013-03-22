//
//  CalendarViewController.m
//  CardioQuest
//
//  Created by Philip Latka on 2013-03-08.
//  Copyright (c) 2013 comp4350group5. All rights reserved.
//

#import "CalendarViewController.h"

@interface CalendarViewController ()

@end


@implementation CalendarViewController


@synthesize window;


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
	// Do any additional setup after loading the view.
    
    self.view.backgroundColor = [[UIColor alloc] initWithPatternImage:[UIImage imageNamed:@"Ubuntu Orange.jpg"]];
    
    if (kal == nil) {
        kal = [[KalViewController alloc] init];
        kal.navigationItem.title = NSLocalizedString(@"Timetable",@"");
        kal.delegate = self;
        //self.dataSource = [[[MyDataSource alloc] init] autorelease];
        //kal.dataSource = dataSource;
    }
    [[self navigationController] pushViewController:kal animated:YES];
    
    
    
    //KalViewController *calendar = [[KalViewController alloc] init];
    //calendar.title = @"Calendar";
    
    //[self.view addSubview:calendar.view];
    //[self addChildViewController:calendar];
    //[[self navigationController] initWithRootViewController:calendar];
    
    //calendar.navigationItem.rightBarButtonItem = [[UIBarButtonItem alloc] initWithTitle:@"Today" style:UIBarButtonItemStyleBordered target:self action:@selector(showAndSelectToday)];
    
}

















- (void)didReceiveMemoryWarning
{
    [super didReceiveMemoryWarning];
    // Dispose of any resources that can be recreated.
}



// hides keyboard
- (void)touchesBegan:(NSSet *)touches withEvent:(UIEvent *)event
{
    [self.view endEditing:YES];
}



@end
