//
//  CDQHealthInputController.h
//  CardioQuest
//
//  Created by Blake Beatty on 2013-03-23.
//  Copyright (c) 2013 comp4350group5. All rights reserved.
//

#import <UIKit/UIKit.h>

@interface CDQHealthInputController : UIViewController
@property (weak, nonatomic) IBOutlet UIDatePicker *healthDate;
@property (weak, nonatomic) IBOutlet UITextField *healthWeight;
@property (weak, nonatomic) IBOutlet UITextField *healthHeartRate;
@property (weak, nonatomic) IBOutlet UITextField *healthComments;
- (IBAction)postHealthRecord:(id)sender;


@end
