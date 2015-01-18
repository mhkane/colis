//
//  deliverersViewController.h
//  Airspress
//
//  Created by Mohamed Kane on 11/30/14.
//
//

#import <Parse/Parse.h>
#import "AirspressTripDetailViewController.h"


@interface deliverersViewController : PFQueryTableViewController
@property(weak,nonatomic) PFQuery *query;

@end
