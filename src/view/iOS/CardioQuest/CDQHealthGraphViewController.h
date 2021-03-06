//
//  CDQHealthGraphViewController.h
//  CardioQuest
//
//  Created by Andrew Konkin on 3/25/13.
//  Copyright (c) 2013 comp4350group5. All rights reserved.
//

#import <UIKit/UIKit.h>
#import "ECGraph.h"

@interface CDQHealthGraphViewController : UIViewController <ECGraphDelegate>{
}

@property (weak, nonatomic) IBOutlet UIDatePicker *startDatePicker;
@property (weak, nonatomic) IBOutlet UIDatePicker *endDatePicker;

@end
