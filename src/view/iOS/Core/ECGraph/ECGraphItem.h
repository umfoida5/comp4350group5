//
// ECGraphItem.h
//
// Create By ECGenerateCode
// Date:2010-05-12 02:27:50
//
//!--
//This is generated by code generater automatic,pls check the type of variables.
//Change them to other suitable type(NSString is by default) if needed.
//--

#import <Foundation/Foundation.h>

@interface ECGraphItem : NSObject {
	NSString	*name;
	UIColor	*color;
	float			yValue;
	NSDate		*yDateValue;
	BOOL		isYDate;
	BOOL		isPercentage;
	float			width;
	int			defaultColor;
}

@property(nonatomic,retain) NSString *name;
@property(nonatomic,retain) UIColor *color;
@property(nonatomic,assign) float yValue;
@property(nonatomic,retain) NSDate *yDateValue;
@property(nonatomic,assign) BOOL isYDate;
@property(nonatomic,assign) BOOL isPercentage;
@property(nonatomic,assign) float width;
@property(nonatomic,assign) int defaultColor;

@end