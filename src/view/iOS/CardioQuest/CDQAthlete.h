//
//  CDQAthlete.h
//  CardioQuest
//
//  Created by Blake Andrew Beatty on 2013-03-08.
//  Copyright (c) 2013 comp4350group5. All rights reserved.
//

#import <Foundation/Foundation.h>
#import "RestKit/RestKit.h"

@interface CDQAthlete : NSObject
    @property (nonatomic, copy)     NSString*   username;
    @property (nonatomic, copy)     NSString*   password;
    @property (nonatomic, copy)     NSString*   first_name;
    @property (nonatomic, copy)     NSString*   last_name;
    @property (nonatomic, copy)     NSString*   email;
    @property (nonatomic, copy)     NSDate*     birth_date;
    @property (nonatomic, copy)     NSString*   about_me;
    @property (nonatomic, copy)     NSString*   address;

- (void) login:(NSString *)username :(NSString *)password;

@end
