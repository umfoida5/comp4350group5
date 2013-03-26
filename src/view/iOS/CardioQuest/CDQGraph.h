//
//  CDQGraph.h
//  CardioQuest
//
//  Created by Andrew Konkin on 3/24/13.
//  Copyright (c) 2013 comp4350group5. All rights reserved.
//

#import <UIKit/UIKit.h>
#import "ASIHTTPRequest.h"

@interface CDQGraph : UIView <ASIHTTPRequestDelegate>
-(void)triggerServerCall:(NSString*)query;
@end
