//
//  APTrip.h
//  Airspress
//
//  Created by Mohamed Kane on 1/24/15.
//
//

#import <Foundation/Foundation.h>

@interface APTrip : NSObject
@property NSString *fromLocation;
@property NSString *toLocation;
@property NSDate *departureDate;
@property NSDate *arrivalDate;
@property int availCapacity;
@property int totalCapacity;
@property int unitPriceUsd;

@end
