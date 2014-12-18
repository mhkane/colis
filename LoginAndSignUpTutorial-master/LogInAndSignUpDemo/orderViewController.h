//
//  orderViewController.h
//  Airspress
//
//  Created by Mohamed Kane on 11/30/14.
//
//

#import <UIKit/UIKit.h>

@interface orderViewController : UIViewController <UIPickerViewDelegate,UIPickerViewDataSource>
@property (weak, nonatomic) IBOutlet UIPickerView *paymentMethod;
@property (weak, nonatomic) IBOutlet UITextField *productName;
@property (weak, nonatomic) IBOutlet UITextField *urlString;
@property (weak, nonatomic) IBOutlet UITextField *productLocation;

@end
