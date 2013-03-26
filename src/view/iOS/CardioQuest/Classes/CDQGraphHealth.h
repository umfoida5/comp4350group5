//
//  CDQGraph.h
//  CardioQuest
//
//  Created by Andrew Konkin on 3/24/13.
//  Copyright (c) 2013 comp4350group5. All rights reserved.
//

//Class is almost a complete duplicate of CDQGraph. The only difference is with requstFinished
//This class is being created solely beacuase stats and health handle server calls differently
//if time permitted, I would make them both do the same type of calls, and only use one class.
//Alternatively, I could make the caller viewController the delegate for the request.

#import <UIKit/UIKit.h>
#import "ASIHTTPRequest.h"

@interface CDQGraphHealth : UIView <ASIHTTPRequestDelegate>
-(void)triggerServerCall:(NSString*)query;
@end
