//
//  APLoginViewController.m
//  Airspress
//
//  Created by Mohamed Kane on 1/23/15.
//
//

#import "APLoginViewController.h"
#import "deliverersViewController.h"
#import "AirspressProfileViewController.h"
#import "AirspressTabBarController.h"
#import "tripViewController.h"
#import "deliveryRequestViewController.h"
#import "APProfileTableViewController.h"
#import "SPGooglePlacesAutocompleteViewController.h"

@interface APLoginViewController ()

@end

@implementation APLoginViewController

- (void)viewDidLoad {
    [super viewDidLoad];
    // Do any additional setup after loading the view from its nib.
    self.delegate=self;
    self.signUpController.delegate=self;
    
    
    self.signUpController.fields = PFSignUpFieldsUsernameAndPassword|PFSignUpFieldsEmail|PFSignUpFieldsAdditional|PFSignUpFieldsSignUpButton|PFSignUpFieldsDismissButton;
    
    self.signUpController.signUpView.additionalField.placeholder=@"Phone Number";
    self.signUpController.signUpView.backgroundColor = [UIColor colorWithPatternImage:[UIImage imageNamed:@"desert"]];
    self.signUpController.signUpView.additionalField.keyboardType=UIKeyboardTypeDecimalPad;
    self.logInView.backgroundColor = [UIColor colorWithPatternImage:[UIImage imageNamed:@"map"]];
    self.logInView.usernameField.backgroundColor=[UIColor whiteColor];
    self.logInView.passwordField.backgroundColor=[UIColor whiteColor];
    self.logInView.usernameField.borderStyle = UITextBorderStyleRoundedRect;
    self.logInView.passwordField.borderStyle= UITextBorderStyleRoundedRect;
    self.logInView.usernameField.textColor=[UIColor grayColor];
    self.logInView.passwordField.textColor=[UIColor blackColor];
    self.logInView.signUpButton.backgroundColor=nil;
    [self.logInView.signUpButton setBackgroundImage:nil forState:UIControlStateHighlighted];
    [self.logInView.signUpButton setBackgroundImage:nil forState:UIControlStateNormal];
    [self.logInView.signUpButton setImage:[UIImage imageNamed:@"signUp"] forState:UIControlStateNormal];
    [self.signUpController.signUpView.signUpButton setBackgroundImage:nil forState:UIControlStateHighlighted];
    [self.signUpController.signUpView.signUpButton setBackgroundImage:nil forState:UIControlStateNormal];
    [self.signUpController.signUpView.signUpButton setImage:[UIImage imageNamed:@"signUp"] forState:UIControlStateNormal];
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
    APProfileTableViewController *profile = [[APProfileTableViewController alloc] init];
    SPGooglePlacesAutocompleteViewController *departureDestination = [[SPGooglePlacesAutocompleteViewController alloc] init];
    [[travelers tabBarItem] setTitle:@"Travels"];
    [[travelers tabBarItem] setImage:[UIImage imageNamed:@"air6.png"]];
    [[profile tabBarItem] setTitle:@"Profile"];
    [[profile tabBarItem] setImage:[UIImage imageNamed:@"user16.png"]];
    UINavigationController *travelNav = [[UINavigationController alloc]initWithRootViewController:travelers];
    [[travelers navigationItem] setTitle:@"Travels"];
    [[profile navigationItem] setTitle:@"Profile"];
    UINavigationController *profileNav = [[UINavigationController alloc] initWithRootViewController:profile];
    [[trip tabBarItem] setTitle:@"trip"];
    NSArray *views = @[travelNav,departureDestination,profileNav];
    [menu setViewControllers:views];
    [self presentViewController:menu animated:true completion:nil];
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




