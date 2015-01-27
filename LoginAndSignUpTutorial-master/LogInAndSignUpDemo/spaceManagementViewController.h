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

@interface spaceManagementViewController : UIViewController<UITableViewDelegate,UITableViewDataSource,UITextFieldDelegate,UIAlertViewDelegate>

@property (weak, nonatomic) IBOutlet UILabel *header;

@property (weak, nonatomic) IBOutlet UITextField *totalSpaceField;
@property (weak, nonatomic) IBOutlet UITextField *priceField;
@property (weak, nonatomic) IBOutlet UITextField *availableSpaceField;
@property APTrip *tripToRegister;
@property int totalSpace;
@property int availableSpace;
@property int pricePerUnit;


@end
