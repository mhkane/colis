// Copyright 2004-present Facebook. All Rights Reserved.

#import <UIKit/UIKit.h>


@interface ProfileViewController : UIViewController <UIActionSheetDelegate, UITextFieldDelegate, UITextViewDelegate>

@property (nonatomic, weak, readwrite) IBOutlet UILabel *username;
@property (nonatomic, weak, readwrite) IBOutlet UIImageView *profilePic;
@property (nonatomic, weak, readwrite) IBOutlet UITextView *biography;
@property (nonatomic, weak, readwrite) IBOutlet UILabel *numberOfStories;
@property (nonatomic, weak, readwrite) IBOutlet UILabel *userRegion;
@property (weak, nonatomic) UIActionSheet *actionSheet;

@end