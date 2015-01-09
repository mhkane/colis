//
//  EditProfileViewController.m
//  Airspress
//
//  Created by Mohamed Kane on 12/29/14.
//
//

#import "EditProfileViewController.h"

@interface EditProfileViewController ()

@end

@implementation EditProfileViewController
-(void)viewWillAppear:(BOOL)animated{
    PFUser *currentUser = [PFUser currentUser];
    self.biography.text = [currentUser objectForKey:@"userBio"];
    
}
- (void)viewDidLoad {
    [super viewDidLoad];
    // Do any additional setup after loading the view from its nib.
}

- (void)didReceiveMemoryWarning {
    [super didReceiveMemoryWarning];
    // Dispose of any resources that can be recreated.
}
- (IBAction)doneButton:(id)sender {
    PFUser *currentUser = [PFUser currentUser];
    [currentUser setObject:self.biography.text forKey:@"userBio"];
    [currentUser saveInBackground];
[[self navigationController] popViewControllerAnimated:YES];
}




@end
