//
//  CDCStatsViewController.h
//  CardioQuest
//
//  Created by Andrew Konkin on 3/16/13.
//  Copyright (c) 2013 comp4350group5. All rights reserved.
//

#import <UIKit/UIKit.h>
#import "ECGraph.h"

@interface CDCStatsViewController : UIViewController<UIPickerViewDataSource, UIPickerViewDelegate, ECGraphDelegate> {
    NSArray *activityTypes;
    NSArray *dateTypes;
    NSArray *mesurementTypes;
}
@property (weak, nonatomic) IBOutlet UIPickerView *activitySelector;
@property (weak, nonatomic) IBOutlet UIPickerView *dateSelector;
@property (weak, nonatomic) IBOutlet UIPickerView *mesurementSelector;

@end
