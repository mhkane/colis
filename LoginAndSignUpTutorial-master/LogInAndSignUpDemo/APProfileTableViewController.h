//
//  APProfileTableViewController.h
//  Airspress
//
//  Created by Mohamed Kane on 1/31/15.
//
//

#import <UIKit/UIKit.h>

@interface APProfileTableViewController : UITableViewController<UITableViewDataSource,UITableViewDelegate>
@property (strong,nonatomic) PFUser *user;
@end
