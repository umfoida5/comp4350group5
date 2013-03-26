//
//  CDQHealthGraphViewController.h
//  CardioQuest
//
//  Created by Andrew Konkin on 3/25/13.
//  Copyright (c) 2013 comp4350group5. All rights reserved.
//

#import <UIKit/UIKit.h>
#import "ECGraph.h"

@interface CDQHealthGraphViewController : UIViewController <UIPickerViewDataSource, UIPickerViewDelegate, ECGraphDelegate>{
    NSArray *dateTypes;
}
@property (weak, nonatomic) IBOutlet UIPickerView *datePicker;
@end
