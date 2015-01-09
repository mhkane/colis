//
//  AirspressViewController.m
//  Anypic
//
//  Created by Mohamed Kane on 12/23/14.
//
//

#import "AirspressLoginViewController.h"
#import "AirspressTabBarController.h"
#import "deliverersViewController.h"
#import "deliveryRequestViewController.h"
#import "tripViewController.h"
#import "orderViewController.h"
#import "AirspressProfileViewController.h"

@interface AirspressLoginViewController ()
@property (nonatomic, strong) UIImageView *fieldsBackground;
@end

@implementation AirspressLoginViewController
@synthesize fieldsBackground;

- (void)viewDidLoad {
    [super viewDidLoad];
    // Do any additional setup after loading the view.
    
    
    [self.logInView setBackgroundColor:[UIColor colorWithPatternImage:[UIImage imageNamed:@"MainBG.png"]]];
    UIImage *logo = [UIImage imageNamed:@"logo.png"];
    CGRect rect = CGRectMake(0,0,150,150);
    UIGraphicsBeginImageContext( rect.size );
    [logo drawInRect:rect];
    UIImage *picture1 = UIGraphicsGetImageFromCurrentImageContext();
    UIGraphicsEndImageContext();
    
    NSData *imageData = UIImagePNGRepresentation(picture1);
    UIImage *img=[UIImage imageWithData:imageData];
    [self.logInView setLogo:[[UIImageView alloc] initWithImage:img]];
    
    // Set buttons appearance
    //[self.logInView.dismissButton setImage:[UIImage imageNamed:@"Exit.png"] forState:UIControlStateNormal];
    //[self.logInView.dismissButton setImage:[UIImage imageNamed:@"ExitDown.png"] forState:UIControlStateHighlighted];
    
    [self.logInView.facebookButton setImage:nil forState:UIControlStateNormal];
    [self.logInView.facebookButton setImage:nil forState:UIControlStateHighlighted];
    [self.logInView.facebookButton setBackgroundImage:[UIImage imageNamed:@"FacebookDown.png"] forState:UIControlStateHighlighted];
    [self.logInView.facebookButton setBackgroundImage:[UIImage imageNamed:@"Facebook.png"] forState:UIControlStateNormal];
    [self.logInView.facebookButton setTitle:@"" forState:UIControlStateNormal];
    [self.logInView.facebookButton setTitle:@"" forState:UIControlStateHighlighted];
    
    [self.logInView.twitterButton setImage:nil forState:UIControlStateNormal];
    [self.logInView.twitterButton setImage:nil forState:UIControlStateHighlighted];
    [self.logInView.twitterButton setBackgroundImage:[UIImage imageNamed:@"Twitter.png"] forState:UIControlStateNormal];
    [self.logInView.twitterButton setBackgroundImage:[UIImage imageNamed:@"TwitterDown.png"] forState:UIControlStateHighlighted];
    [self.logInView.twitterButton setTitle:@"" forState:UIControlStateNormal];
    [self.logInView.twitterButton setTitle:@"" forState:UIControlStateHighlighted];
    
    [self.logInView.signUpButton setBackgroundImage:[UIImage imageNamed:@"SignUp.png"] forState:UIControlStateNormal];
    [self.logInView.signUpButton setBackgroundImage:[UIImage imageNamed:@"SignUpDown.png"] forState:UIControlStateHighlighted];
    [self.logInView.signUpButton setTitle:@"" forState:UIControlStateNormal];
    [self.logInView.signUpButton setTitle:@"" forState:UIControlStateHighlighted];
    

    
    // Add login field background
    fieldsBackground = [[UIImageView alloc] initWithImage:[UIImage imageNamed:@""]];
    [self.logInView insertSubview:fieldsBackground atIndex:1];
    
    
    // Remove text shadow
    CALayer *layer = self.logInView.usernameField.layer;
    layer.shadowOpacity = 0.0;
    layer = self.logInView.passwordField.layer;
    layer.shadowOpacity = 0.0;
    
    // Set field text color
    [self.logInView.usernameField setTextColor:[UIColor whiteColor]];
    [self.logInView.passwordField setTextColor:[UIColor whiteColor]];
}

- (void)didReceiveMemoryWarning {
    [super didReceiveMemoryWarning];
    // Dispose of any resources that can be recreated.
}
-(void)logInViewController:(PFLogInViewController *)logInController didLogInUser:(PFUser *)user{
    [self dismissViewControllerAnimated:YES completion:NULL];
    AirspressTabBarController *menu = [[AirspressTabBarController alloc] init];
    deliverersViewController *deliverer = [[deliverersViewController alloc] init
                                           ] ;
    deliveryRequestViewController *delivery = [[deliveryRequestViewController alloc]init];
    
    tripViewController *trip = [[tripViewController alloc] init];
    orderViewController *order = [[orderViewController alloc] init];
    deliverersViewController *travelers = [[deliverersViewController alloc]init];
    UINavigationController *tripNav = [[UINavigationController alloc] initWithRootViewController:trip];
    AirspressProfileViewController *profile = [[AirspressProfileViewController alloc] init];
    [[travelers tabBarItem] setTitle:@"Travels"];
    [[travelers tabBarItem] setImage:[UIImage imageNamed:@"air6.png"]];
    [[profile tabBarItem] setTitle:@"Profile"];
    [[profile tabBarItem] setImage:[UIImage imageNamed:@"user16.png"]];
    UINavigationController *travelNav = [[UINavigationController alloc]initWithRootViewController:travelers];
    UINavigationController *profileNav = [[UINavigationController alloc] initWithRootViewController:profile];
    
    
    [[trip tabBarItem] setTitle:@"trip"];
    NSArray *views = @[travelNav,delivery,profileNav];
    [menu setViewControllers:views];
    [self presentViewController:menu animated:false completion:nil];
    [self _loadData];
    
    
}
- (void)_loadData {
    // ...
    FBRequest *request = [FBRequest requestForMe];
    [request startWithCompletionHandler:^(FBRequestConnection *connection, id result, NSError *error) {
        if (!error) {
            // result is a dictionary with the user's Facebook data
            PFUser *currentUser = [PFUser currentUser];
            NSString *currentName = [currentUser valueForKey:@"username"];
            
            NSDictionary *userData = (NSDictionary *)result;
            
            NSString *facebookID = userData[@"id"];
            NSString *name = userData[@"name"];
            NSString *location = userData[@"location"][@"name"];
            if(![currentName isEqualToString:name]){
                [currentUser setObject:name forKey:@"username"];
            }
            [currentUser saveInBackground];
            NSString *gender = userData[@"gender"];
            NSString *birthday = userData[@"birthday"];
            NSString *relationship = userData[@"relationship_status"];
            NSLog(@"%@",name);
            
            NSURL *pictureURL = [NSURL URLWithString:[NSString stringWithFormat:@"https://graph.facebook.com/%@/picture?type=large&return_ssl_resources=1", facebookID]];
            
            // Now add the data to the UI elements
            // ...
        }
    }];
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
