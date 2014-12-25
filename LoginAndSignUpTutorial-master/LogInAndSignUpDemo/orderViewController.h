//
//  orderViewController.h
//  Airspress
//
//  Created by Mohamed Kane on 11/30/14.
//
//

#import <UIKit/UIKit.h>

@interface orderViewController : UIViewController <UITextFieldDelegate, UIPickerViewDelegate,UIPickerViewDataSource>
@property (weak, nonatomic) IBOutlet UITextField *itemName;
@property (weak, nonatomic) IBOutlet UITextField *placeName;
@property (weak, nonatomic) IBOutlet UITextField *city;
@property (weak, nonatomic) IBOutlet UITextField *country;
@property (weak, nonatomic) IBOutlet UIPickerView *paymentMethod;



@end
