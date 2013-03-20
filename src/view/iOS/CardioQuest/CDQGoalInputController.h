//
//  CDQGoalInputController.h
//  CardioQuest
//
//  Created by Justin Foidart on 2013-03-20.
//  Copyright (c) 2013 comp4350group5. All rights reserved.
//

#import <UIKit/UIKit.h>

@interface CDQGoalInputController : UIViewController <UIPickerViewDataSource, UIPickerViewDelegate>
@property (weak, nonatomic) IBOutlet UIPickerView *typeOperatorMetricInput;
@property (weak, nonatomic) IBOutlet UITextField *quantityInput;
@property (weak, nonatomic) IBOutlet UIDatePicker *startDateInput;
@property (weak, nonatomic) IBOutlet UIDatePicker *endDateInput;

@property (strong, nonatomic) NSMutableArray *typeContentArray;
@property (strong, nonatomic) NSMutableArray *operatorContentArray;
@property (strong, nonatomic) NSMutableArray *metricContentArray;
@end
