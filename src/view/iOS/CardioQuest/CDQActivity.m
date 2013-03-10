//
//  CDQActivity.m
//  CardioQuest
//
//  Created by Blake Andrew Beatty on 2013-03-08.
//  Copyright (c) 2013 comp4350group5. All rights reserved.
//

#import "CDQActivity.h"

@implementation CDQActivity

- (void) loadActivities
{
    RKObjectMapping* articleMapping = [RKObjectMapping mappingForClass:[CDQActivity class]];
    [articleMapping addAttributeMappingsFromDictionary:@{
     @"date": @"date",
     @"duration": @"duration",
     @"max_speed": @"max_speed",
     @"type": @"type",     
     @"distance": @"distance"
     }];
    
    RKResponseDescriptor *responseDescriptor = [RKResponseDescriptor responseDescriptorWithMapping:articleMapping pathPattern:nil keyPath:@"aaData" statusCodes:RKStatusCodeIndexSetForClass(RKStatusCodeClassSuccessful)];
    
    // Specifies URL to request activities json
    NSURL *URL = [NSURL URLWithString:@"http://ec2-107-21-196-190.compute-1.amazonaws.com:8000/activities/update_datatable"];
    
    // creates a request using factory
    NSURLRequest *request = [NSURLRequest requestWithURL:URL];
    
    // creates request object operation
    RKObjectRequestOperation *objectRequestOperation = [[RKObjectRequestOperation alloc] initWithRequest:request responseDescriptors:@[ responseDescriptor ]];
    
    // sets status and failure behaviour
    [objectRequestOperation setCompletionBlockWithSuccess:^(RKObjectRequestOperation *operation, RKMappingResult *mappingResult) {
        //RKLogInfo(@"Load collection of Activities: %@", mappingResult.array);
        NSLog(@"GOOD TO GO");
    } failure:^(RKObjectRequestOperation *operation, NSError *error) {
        //RKLogError(@"Operation failed with Activities: %@", error);
        NSLog(@"ERROR");
    }];
    
    // start operation execution
    [objectRequestOperation start];
}
@end

/*
 date;
 duration;
 max_speed
 type;
 distance;
*/