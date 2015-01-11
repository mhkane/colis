//
//  cellForTravelTableViewCell.h
//  Airspress
//
//  Created by Mohamed Kane on 1/10/15.
//
//

#import <UIKit/UIKit.h>

@interface cellForTravelTableViewCell : UITableViewCell
@property (weak, nonatomic) IBOutlet UILabel *travelerName;
@property (weak, nonatomic) IBOutlet UILabel *toDestination;
@property (weak, nonatomic) IBOutlet UIImageView *plane;
@property (weak, nonatomic) IBOutlet UILabel *fromDestination;
@property (weak, nonatomic) IBOutlet UILabel *date;

@end
