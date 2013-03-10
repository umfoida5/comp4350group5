//
//  CDQAthlete.m
//  CardioQuest
//
//  Created by Blake Andrew Beatty on 2013-03-08.
//  Copyright (c) 2013 comp4350group5. All rights reserved.
//

#import "CDQAthlete.h"

@implementation CDQAthlete

- (void) login:(NSString *)username :(NSString *)password
{
    RKObjectMapping* articleMapping = [RKObjectMapping mappingForClass:[CDQAthlete class]];
    [articleMapping addAttributeMappingsFromDictionary:@{
     @"username": @"username",
     @"password": @"password",
     @"first_name": @"first_name",
     @"last_name": @"last_name",
     @"email": @"email",
     @"birth_date": @"birth_date",
     @"about_me": @"about_me",
     @"address": @"address"
     }];
    
   
    // Set url of webservice
    NSURL *URL = [NSURL URLWithString:@"http://ec2-107-21-196-190.compute-1.amazonaws.com:8000/login/do_login"];
    
    // Set object manager with base url
    RKObjectManager *objectManager = [[RKObjectManager alloc] init];
    objectManager = [RKObjectManager managerWithBaseURL:URL];
    
    // Set accepted data type
    [objectManager setSerializationMIMEType:@"application/json"];
    [objectManager setAcceptMIMEType:@"application/json"];
    
}

@end
