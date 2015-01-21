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
#import <QuartzCore/QuartzCore.h>

@interface AirspressLoginViewController ()
@property (nonatomic, strong) UIImageView *fieldsBackground;
@end

@implementation AirspressLoginViewController
@synthesize fieldsBackground;

- (void)viewDidLoad {
    [super viewDidLoad];
    
    
    self.delegate=self;
    self.signUpController.delegate=self;
    [self.logInView setBackgroundColor:[UIColor colorWithPatternImage:[UIImage imageNamed:@"suitcase5.png"]]];
    [self.logInView setLogo:[[UIImageView alloc] initWithImage:[UIImage imageNamed:@"Logo.png"]]];
    
    // Set buttons appearance

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
    
    [self.logInView.signUpButton setBackgroundImage:[UIImage imageNamed:@"Signup.png"] forState:UIControlStateNormal];
    [self.logInView.signUpButton setBackgroundImage:[UIImage imageNamed:@"SignupDown.png"] forState:UIControlStateHighlighted];
    [self.logInView.signUpButton setTitle:@"" forState:UIControlStateNormal];
    [self.logInView.signUpButton setTitle:@"" forState:UIControlStateHighlighted];
    
    // Add login field background
   // fieldsBackground = [[UIImageView alloc] initWithImage:[UIImage imageNamed:@"LoginFieldBG.png"]];
    
    [self.logInView addSubview:self.fieldsBackground];
    [self.logInView sendSubviewToBack:self.fieldsBackground];
    
    // Remove text shadow
    CALayer *layer = self.logInView.usernameField.layer;
    layer.shadowOpacity = 0.0f;
    layer = self.logInView.passwordField.layer;
    layer.shadowOpacity = 0.0f;
    
    // Set field text color
    [self.logInView.usernameField setTextColor:[UIColor whiteColor]];
    [self.logInView.passwordField setTextColor:[UIColor blackColor]];
    self.logInView.usernameField.borderStyle = UITextBorderStyleRoundedRect;
    self.logInView.passwordField.borderStyle = UITextBorderStyleRoundedRect;
    
}
- (void)viewDidLayoutSubviews {
    [super viewDidLayoutSubviews];
    
    // Set frame for elements
    [self.logInView.logo setFrame:CGRectMake(66.5f, 70.0f, 187.0f, 58.5f)];
    [self.logInView.facebookButton setFrame:CGRectMake(35.0f, 287.0f, 120.0f, 40.0f)];
    [self.logInView.twitterButton setFrame:CGRectMake(35.0f+130.0f, 287.0f, 120.0f, 40.0f)];
    [self.logInView.signUpButton setFrame:CGRectMake(35.0f, 385.0f, 250.0f, 40.0f)];
    [self.logInView.usernameField setFrame:CGRectMake(35.0f, 145.0f, 250.0f, 50.0f)];
    [self.logInView.passwordField setFrame:CGRectMake(35.0f, 205.0f, 250.0f, 50.0f)];
    [self.fieldsBackground setFrame:CGRectMake(35.0f, 145.0f, 250.0f, 100.0f)];
}
- (void)didReceiveMemoryWarning {
    [super didReceiveMemoryWarning];
    // Dispose of any resources that can be recreated.
}
#pragma mark - PFLogInViewControllerDelegate

// Sent to the delegate to determine whether the log in request should be submitted to the server.
- (BOOL)logInViewController:(PFLogInViewController *)logInController shouldBeginLogInWithUsername:(NSString *)username password:(NSString *)password {
    if (username && password && username.length && password.length) {
        return YES;
    }
    
    [[[UIAlertView alloc] initWithTitle:NSLocalizedString(@"Missing Information", nil) message:NSLocalizedString(@"Make sure you fill out all of the information!", nil) delegate:nil cancelButtonTitle:NSLocalizedString(@"OK", nil) otherButtonTitles:nil] show];
    return NO;
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

// Sent to the delegate when a PFUser is logged in.
- (void)logInViewController:(PFLogInViewController *)logInController didLogInUser:(PFUser *)user {
    
    AirspressTabBarController *menu = [[AirspressTabBarController alloc] init];
    deliveryRequestViewController *delivery = [[deliveryRequestViewController alloc]init];
    tripViewController *trip = [[tripViewController alloc] init];
    deliverersViewController *travelers = [[deliverersViewController alloc]init];
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
    
    
    
    /* AirspressTabBarController *menu = [[AirspressTabBarController alloc] init];
     //Profile
     UIViewController *profile =[[UIViewController alloc]init];
     [[profile tabBarItem] setTitle:@"Profile"];
     [[profile tabBarItem] setImage:[UIImage imageNamed:@"user160.png"]];
     UINavigationController *profileNav = [[UINavigationController alloc]initWithRootViewController:profile];
     
     //Travelers
     deliverersViewController *travelers = [[deliverersViewController alloc]init];
     [[travelers tabBarItem] setTitle:@"Travels"];
     [[travelers tabBarItem] setImage:[UIImage imageNamed:@"air6.png"]];
     UINavigationController *travelersNav = [[UINavigationController alloc] initWithRootViewController:travelers];
     
     //NavRoot
     UIViewController *navRoot = [[UIViewController alloc]init];
     UINavigationController *nav = [[UINavigationController alloc]initWithRootViewController:navRoot];
     NSArray *views = @[travelersNav,nav,profileNav];
     [menu setViewControllers:views];
     [self presentViewController:menu animated:false completion:nil];
     [self _loadData];*/
    
}

// Sent to the delegate when the log in attempt fails.
- (void)logInViewController:(PFLogInViewController *)logInController didFailToLogInWithError:(NSError *)error {
    NSLog(@"Failed to log in...");
}

// Sent to the delegate when the log in screen is dismissed.
- (void)logInViewControllerDidCancelLogIn:(PFLogInViewController *)logInController {
    NSLog(@"User dismissed the logInViewController");
}


#pragma mark - PFSignUpViewControllerDelegate

// Sent to the delegate to determine whether the sign up request should be submitted to the server.
- (BOOL)signUpViewController:(PFSignUpViewController *)signUpController shouldBeginSignUp:(NSDictionary *)info {
    BOOL informationComplete = YES;
    for (id key in info) {
        NSString *field = [info objectForKey:key];
        if (!field || field.length == 0) {
            informationComplete = NO;
            break;
        }
    }
    
    if (!informationComplete) {
        [[[UIAlertView alloc] initWithTitle:NSLocalizedString(@"Missing Information", nil) message:NSLocalizedString(@"Make sure you fill out all of the information!", nil) delegate:nil cancelButtonTitle:NSLocalizedString(@"OK", nil) otherButtonTitles:nil] show];
    }
    
    return informationComplete;
}

// Sent to the delegate when a PFUser is signed up.
- (void)signUpViewController:(PFSignUpViewController *)signUpController didSignUpUser:(PFUser *)user {
    [self dismissViewControllerAnimated:YES completion:NULL];
}

// Sent to the delegate when the sign up attempt fails.
- (void)signUpViewController:(PFSignUpViewController *)signUpController didFailToSignUpWithError:(NSError *)error {
    NSLog(@"Failed to sign up...");
}

// Sent to the delegate when the sign up screen is dismissed.
- (void)signUpViewControllerDidCancelSignUp:(PFSignUpViewController *)signUpController {
    NSLog(@"User dismissed the signUpViewController");
}


#pragma mark - ()

- (IBAction)logOutButtonTapAction:(id)sender {
    [PFUser logOut];
    [self.navigationController popViewControllerAnimated:YES];
}

@end
