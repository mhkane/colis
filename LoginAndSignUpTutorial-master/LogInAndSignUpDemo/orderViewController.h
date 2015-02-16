//
//  orderViewController.h
//  Airspress
//
//  Created by Mohamed Kane on 11/30/14.
//
//

#import <UIKit/UIKit.h>

@interface orderViewController : UIViewController <UITextFieldDelegate, UIPickerViewDelegate,UIPickerViewDataSource>
@property (weak, nonatomic) IBOutlet UIPickerView *paymentMethod;
@property (weak, nonatomic) IBOutlet UITextField *productDescription;
@property int weight;
@property (weak, nonatomic) IBOutlet UILabel *weightLabel;
@property (strong,nonatomic) PFObject *tripObject;
@property (strong,nonatomic) PFUser *traveler;



@end
