//
//  APLoginViewController.h
//  Airspress
//
//  Created by Mohamed Kane on 1/23/15.
//
//

#import <Parse/Parse.h>

@interface APLoginViewController : PFLogInViewController<PFLogInViewControllerDelegate,PFSignUpViewControllerDelegate>
@property (weak, nonatomic) IBOutlet UIButton *logInButton;
@property (weak, nonatomic) IBOutlet UIButton *signUpButton;

@end
