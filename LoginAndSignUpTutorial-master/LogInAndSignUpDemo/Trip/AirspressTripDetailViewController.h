//
//  RouteTableViewController.h
//  FoxtrotiOS
//
//  Created by Mohamed Kane on 1/13/15.
//  Copyright (c) 2015 Mohamed Kane. All rights reserved.
//

#import <UIKit/UIKit.h>
#import "AirspressTripDetailCell.h"




@interface AirspressTripDetailViewController : UITableViewController <UITableViewDataSource,UITableViewDelegate>
@property (strong,nonatomic) PFObject *tripObject;
@end
