//
//  CDQActivity.h
//  CardioQuest
//
//  Created by Blake Andrew Beatty on 2013-03-08.
//  Copyright (c) 2013 comp4350group5. All rights reserved.
//

#import <Foundation/Foundation.h>
#import <RestKit/RestKit.h>

@interface CDQActivity : NSObject
    @property (nonatomic, copy)     NSDate*     date;
    @property (nonatomic, copy)     NSString*   duration;
    @property (nonatomic, copy)     NSString*   max_speed;
    @property (nonatomic, strong)   NSString*   type;
    @property (nonatomic, strong)   NSString*   distance;

- (void) loadActivities;

@end
