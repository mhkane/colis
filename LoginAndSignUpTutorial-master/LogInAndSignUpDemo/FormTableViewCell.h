//
//  FormTableViewCell.h
//  Airspress
//
//  Created by Mohamed Kane on 1/24/15.
//
//

#import <UIKit/UIKit.h>

@interface FormTableViewCell : UITableViewCell
@property (weak, nonatomic) IBOutlet UILabel *titleLabel;
@property (weak, nonatomic) IBOutlet UITextField *value;
@property (weak, nonatomic) IBOutlet UIStepper *stepper;

@end
