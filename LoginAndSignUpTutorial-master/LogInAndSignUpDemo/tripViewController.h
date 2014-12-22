//
//  tripViewController.h
//  LogInAndSignUpDemo
//
//  Created by Mohamed Kane on 11/27/14.
//
//

#import <UIKit/UIKit.h>

@interface tripViewController : UIViewController
@property NSArray *options;
//- (NSArray *)locationsFromJSONFile:(NSURL *)url;
@property (weak, nonatomic) IBOutlet UITextField *fromTextField;
@property (weak, nonatomic) IBOutlet UITextField *toTextField;
@property (weak, nonatomic) IBOutlet UIButton *registerButton;
@property (weak, nonatomic) IBOutlet UIButton *addTripButton;
@property (weak, nonatomic) IBOutlet UIDatePicker *tripDate;

@end
