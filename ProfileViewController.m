// Copyright 2004-present Facebook. All Rights Reserved.

#import "ProfileViewController.h"
#import "EditProfileViewController.h"
#import "TMMUser.h"
#import <Parse/Parse.h>
#import  "TMMMyStoriesViewController.h"
#import "TMMStoriesLayout.h"


@interface ProfileViewController ()


@end

@implementation ProfileViewController

- (IBAction)EditProfile:(id)sender {
    EditProfileViewController *editProfile = [[EditProfileViewController alloc]initWithNibName:nil bundle:nil];
    // Push onto the top of the navigation controller's stack
    [self.navigationController pushViewController:editProfile animated:YES];
}

- (void)pullInfoFromUser
{
    TMMUser *user = (TMMUser *) [PFUser currentUser];
    self.username.text = user[@"username"];
    self.biography.text = user[@"userBio"];
    self.userRegion.text = user[@"userRegion"];
    self.numberOfStories.text = [NSString stringWithFormat:@"%d", [user.userStories count]];
    
    // Picture
    
    PFFile *theImage = user[@"userProfilePic"];
    
    [theImage getDataInBackgroundWithBlock:^(NSData *data, NSError *error) {
        if (!error) {
            UIImage *image = [UIImage imageWithData:data];
            self.profilePic.image =image;
        }
    }];
    
    
}

- (id)initWithNibName:(NSString *)nibNameOrNil bundle:(NSBundle *)nibBundleOrNil
{
    self = [super initWithNibName:nibNameOrNil bundle:nibBundleOrNil];
    
    return self;
}

- (IBAction)viewUserStories:(id)sender
{
    // Not implemented yet. Waiting for Muhammad's view controller.
    TMMStoriesLayout *layout = [[TMMStoriesLayout alloc] init];
    TMMMyStoriesViewController *myStories = [[TMMMyStoriesViewController alloc] initWithCollectionViewLayout:layout];
    [self.navigationController pushViewController:myStories animated:YES];
        
    
}

- (void)viewDidLoad
{
    [super viewDidLoad];
}

- (void)viewWillAppear:(BOOL)animated
{
    [super viewWillAppear:animated];
    [self pullInfoFromUser];
    self.navigationItem.title = self.username.text;
}

#pragma mark - <UITextFieldDelegate>

- (BOOL)textFieldShouldReturn:(UITextField *)textField
{
    [textField resignFirstResponder];
    return NO;
}

#pragma mark - <UITextViewDelegate>

-(BOOL)textView:(UITextView *)textView shouldChangeTextInRange:(NSRange)range replacementText:(NSString *)text
{
    if([text isEqualToString:@"\n"])
        [textView resignFirstResponder];
    return YES;
}

#pragma mark - ()

- (void)dismissKeyboard
{
    [self.biography resignFirstResponder];
}


@end
