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
    PFUser *currentUser = [PFUser currentUser];
    PFFile *imageFile =[currentUser objectForKey:@"profilePicture"];
    [imageFile getDataInBackgroundWithBlock:^(NSData *data, NSError *error) {
        UIImage *image = [[UIImage alloc] init];
        if(data!=nil){
            image = [UIImage imageWithData:data];
        }
        else{
            image = [UIImage imageNamed:@"userProfile.png"];
        }
        self.profilePicture.image = image;
    }];
}
- (void)viewDidLoad {
    [super viewDidLoad];
    // Do any additional setup after loading the view from its nib.
    self.profilePicture.layer.cornerRadius = self.profilePicture.frame.size.width / 2;
    self.profilePicture.clipsToBounds = YES;
    self.profilePicture.layer.borderWidth = 3.0f;
    self.profilePicture.layer.borderColor = [UIColor whiteColor].CGColor;
    
}

- (void)didReceiveMemoryWarning {
    [super didReceiveMemoryWarning];
    // Dispose of any resources that can be recreated.
}
- (IBAction)editProfile:(id)sender {
    [self.navigationController pushViewController:[[EditProfileViewController alloc] init] animated:true];
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
