//
//  TripDetailTableViewController.h
//  
//
//  Created by Mohamed Kane on 1/16/15.
//
//

#import <UIKit/UIKit.h>
#import "tripDetailCell.h"

@interface TripDetailTableViewController : UITableViewController
@property(strong,nonatomic) PFObject *tripObject;
@end
