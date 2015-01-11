//
//  cellForTravelTableViewCell.m
//  Airspress
//
//  Created by Mohamed Kane on 1/10/15.
//
//

#import "cellForTravelTableViewCell.h"

@implementation cellForTravelTableViewCell
@synthesize travelerName;
@synthesize toDestination;
@synthesize plane;
@synthesize fromDestination;
@synthesize date;

- (void)awakeFromNib {
    // Initialization code
}

- (void)setSelected:(BOOL)selected animated:(BOOL)animated {
    [super setSelected:selected animated:animated];

    // Configure the view for the selected state
}

@end
