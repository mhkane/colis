//
//  AirspressProfileViewController.h
//  Airspress
//
//  Created by Mohamed Kane on 1/5/15.
//
//

#import <UIKit/UIKit.h>

@interface AirspressProfileViewController : UIViewController
@property (weak, nonatomic) IBOutlet UIImageView *profilePicture;
@property (weak, nonatomic) IBOutlet UILabel *username;
@property (weak, nonatomic) IBOutlet UILabel *region;
@property (weak, nonatomic) IBOutlet UILabel *rating;
@property (weak, nonatomic) IBOutlet UITextView *userBio;

@end
