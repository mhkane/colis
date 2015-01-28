//
//  spaceManagementViewController.h
//  Airspress
//
//  Created by Mohamed Kane on 1/24/15.
//
//

#import <UIKit/UIKit.h>
#import "APTrip.h"

@interface spaceManagementViewController : UIViewController<UITextFieldDelegate,UIAlertViewDelegate>

@property (weak, nonatomic) IBOutlet UILabel *header;

@property (weak, nonatomic) IBOutlet UITextField *totalSpaceField;
@property (weak, nonatomic) IBOutlet UITextField *priceField;
@property (weak, nonatomic) IBOutlet UITextField *availableSpaceField;
@property APTrip *tripToRegister;
@property int totalSpace;
@property int availableSpace;
@property int pricePerUnit;
@property (weak, nonatomic) IBOutlet UIView *insideView;


@end
