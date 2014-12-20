//
//  tripDetailViewController.h
//  Airspress
//
//  Created by Mohamed Kane on 12/18/14.
//
//

#import <UIKit/UIKit.h>

@interface tripDetailViewController : UIViewController
@property (weak,nonatomic) NSString *message;
@property (weak, nonatomic) IBOutlet UITextView *tripDetails;
@property (weak, nonatomic) IBOutlet UIImageView *travelerPicture;
-(id)initWithMessage:(NSString *)message;
@end
