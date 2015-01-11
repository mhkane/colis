//
//  EditProfileViewController.h
//  Airspress
//
//  Created by Mohamed Kane on 12/29/14.
//
//

#import <UIKit/UIKit.h>
#import <MobileCoreServices/MobileCoreServices.h>

@interface EditProfileViewController : UIViewController<UINavigationBarDelegate,UIImagePickerControllerDelegate,UITextFieldDelegate>
@property (weak, nonatomic) IBOutlet UITextView *biography;
@property (weak, nonatomic) IBOutlet UIImageView *profilePic;

@end
