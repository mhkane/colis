//
//  ProfileViewController.m
//  Airspress
//
//  Created by Mohamed Kane on 12/17/14.
//
//

#import "ProfileViewController.h"
#import "EditProfileViewController.h"

@interface ProfileViewController ()

@end

@implementation ProfileViewController

- (void)viewDidLoad {
    [super viewDidLoad];
    // Do any additional setup after loading the view from its nib.
}

- (void)didReceiveMemoryWarning {
    [super didReceiveMemoryWarning];
    // Dispose of any resources that can be recreated.
}
- (IBAction)editProfile:(id)sender {
    EditProfileViewController *edit = [[EditProfileViewController alloc] init];
    [self.navigationController pushViewController:edit animated:false];
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
