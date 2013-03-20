//
//  CDQActivityInputController.h
//  CardioQuest
//
//  Created by Alex Salomon Thome Da Silva on 3/20/13.
//  Copyright (c) 2013 comp4350group5. All rights reserved.
//

#import <UIKit/UIKit.h>

@interface CDQActivityInputController : UIViewController <UIPickerViewDataSource, UIPickerViewDelegate>
@property (weak, nonatomic) IBOutlet UIPickerView *typeInput;
@property (strong, nonatomic) NSMutableArray *typeContentArray;

@end
