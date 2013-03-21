//
//  CDCgraph.h
//  CardioQuest
//
//  Created by Andrew Konkin on 3/20/13.
//  Copyright (c) 2013 comp4350group5. All rights reserved.
//

#import <UIKit/UIKit.h>

@interface CDCgraph : UIView
- (void)drawGraph;
- (void)drawRect:(CGRect)rect: (NSString*)athlete_id: (NSString*)activity: (NSString*)dateType: (NSString*)measurementType;
@end