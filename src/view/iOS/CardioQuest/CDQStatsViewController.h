//
//  CDQStatsViewController.h
//  CardioQuest
//
//  Created by Andrew Konkin on 3/24/13.
//  Copyright (c) 2013 comp4350group5. All rights reserved.
//

#import <UIKit/UIKit.h>
#import "ECGraph.h"

@interface CDQStatsViewController : UIViewController<UIPickerViewDataSource, UIPickerViewDelegate, ECGraphDelegate> {
    NSArray *activityTypes;
    NSArray *dateTypes;
    NSArray *mesurementTypes;
}
@property (weak, nonatomic) IBOutlet UIPickerView *activityPicker;
@property (weak, nonatomic) IBOutlet UIPickerView *measurePicker;
@property (weak, nonatomic) IBOutlet UIPickerView *datePicker;

@end
