//
//  spaceManagementViewController.h
//  Airspress
//
//  Created by Mohamed Kane on 1/24/15.
//
//

#import <UIKit/UIKit.h>
#import "FormTableViewCell.h"
#import "APTrip.h"

@interface spaceManagementViewController : UIViewController<UITableViewDelegate,UITableViewDataSource>
@property (weak, nonatomic) IBOutlet UITableView *spaceForm;
@property (weak, nonatomic) IBOutlet UIButton *registerTrip;
@property APTrip *tripToRegister;

@end
