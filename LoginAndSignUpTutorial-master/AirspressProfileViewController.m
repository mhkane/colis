//
//  AirspressProfileViewController.m
//  Airspress
//
//  Created by Mohamed Kane on 1/5/15.
//
//

#import "AirspressProfileViewController.h"
#import "EditProfileViewController.h"

@interface AirspressProfileViewController ()

@end

@implementation AirspressProfileViewController
-(void)viewWillAppear:(BOOL)animated{
    self.username.text = [[PFUser currentUser] username];
    self.userBio.text = [[PFUser currentUser] objectForKey:@"userBio"];
    self.rating.text = [[PFUser currentUser] objectForKey:@"userRating"];
}
- (void)viewDidLoad {
    [super viewDidLoad];
    // Do any additional setup after loading the view from its nib.
}

- (void)didReceiveMemoryWarning {
    [super didReceiveMemoryWarning];
    // Dispose of any resources that can be recreated.
}
- (IBAction)editProfile:(id)sender {
    [self.navigationController pushViewController:[[EditProfileViewController alloc] init] animated:false];
}

/*
#pragma mark - Navigation

// In a storyboard-based application, you will often want to do a little preparation before navigation
- (void)prepareForSegue:(UIStoryboardSegue *)segue sender:(id)sender {
    // Get the new view controller using [segue destinationViewController].
    // Pass the selected object to the new view controller.
}
*/

@end
