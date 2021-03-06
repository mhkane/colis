//
//  AppDelegate.m
//  LogInAndSignUpDemo
//
//  Created by Mattieu Gamache-Asselin on 6/14/12.
//  Copyright (c) 2013 Parse. All rights reserved.
//

#import "AppDelegate.h"
#import "DemoTableViewController.h"
#import "tripViewController.h"
#import "deliveryRequestViewController.h"
#import "deliverersViewController.h"
#import "orderViewController.h"
#import "searchViewController.h"
#import "AirspressLoginViewController.h"
#import "AirspressTabBarController.h"
#import "Confirmation2ViewController.h"
#import "SPGooglePlacesAutocompleteViewController.h"
#import "AirspressTripDetailViewController.h"
#import "APLoginViewController.h"
#import <FacebookSDK/FacebookSDK.h>
#import "spaceManagementViewController.h"

@implementation AppDelegate


#pragma mark - UIApplicationDelegate

- (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions {
   
    
    // ****************************************************************************
    // Fill in with your Parse and Twitter credentials. Don't forget to add your
    // Facebook id in Info.plist:
    // ****************************************************************************
    [Parse setApplicationId:@"9GC4ybpn3PxuHyfCm3JKQZXyC1WBNuiTzhRcTHo6"
                  clientKey:@"tWpMJpqLwQGENYGL9HQILn7s598qr7f1hU0G9C7t"];
    [PFFacebookUtils initializeFacebook];
    [PFTwitterUtils initializeWithConsumerKey:@"your_twitter_consumer_key" consumerSecret:@"your_twitter_consumer_secret"];
    
    // Set default ACLs
    PFACL *defaultACL = [PFACL ACL];
    [defaultACL setPublicReadAccess:YES];
    [PFACL setDefaultACL:defaultACL withAccessForCurrentUser:YES];
    
    // Register for Push Notitications
    
    UIUserNotificationType userNotificationTypes = (UIUserNotificationTypeAlert |
                                                    UIUserNotificationTypeBadge |
                                                    UIUserNotificationTypeSound);
    UIUserNotificationSettings *settings = [UIUserNotificationSettings settingsForTypes:userNotificationTypes
                                                                             categories:nil];
    [application registerUserNotificationSettings:settings];
    [application registerForRemoteNotifications];
    self.window = [[UIWindow alloc] initWithFrame:[[UIScreen mainScreen] bounds]];
    tripViewController *trip = [[tripViewController alloc] init];
    Confirmation2ViewController * c = [[Confirmation2ViewController alloc] init];
    SPGooglePlacesAutocompleteViewController *vc = [[SPGooglePlacesAutocompleteViewController alloc] init];
    AirspressTripDetailViewController *cont = [[AirspressTripDetailViewController alloc] init];
    APLoginViewController *l = [[APLoginViewController alloc] initWithNibName:@"APLoginViewController" bundle:[NSBundle mainBundle]];
    AirspressLoginViewController *login2 = [[AirspressLoginViewController alloc]init];
    spaceManagementViewController *r = [[spaceManagementViewController alloc] init];
    login2.fields = PFLogInFieldsUsernameAndPassword| PFLogInFieldsFacebook | PFLogInFieldsSignUpButton ;
    l.fields =PFLogInFieldsUsernameAndPassword| PFLogInFieldsFacebook | PFLogInFieldsSignUpButton | PFLogInFieldsLogInButton ;
    self.window.rootViewController = l;
    self.window.backgroundColor = [UIColor whiteColor];
    [self.window makeKeyAndVisible];
    return YES;
}
- (void)application:(UIApplication *)application didRegisterForRemoteNotificationsWithDeviceToken:(NSData *)deviceToken {
    // Store the deviceToken in the current installation and save it to Parse.
    PFInstallation *currentInstallation = [PFInstallation currentInstallation];
    NSLog(@"Registered for push");
    [currentInstallation setDeviceTokenFromData:deviceToken];
    [currentInstallation saveInBackground];
}

- (void)application:(UIApplication *)application didReceiveRemoteNotification:(NSDictionary *)userInfo {
    [PFPush handlePush:userInfo];
}
// Facebook oauth callback
- (BOOL)application:(UIApplication *)application handleOpenURL:(NSURL *)url {
    return [PFFacebookUtils handleOpenURL:url];
}

- (BOOL)application:(UIApplication *)application openURL:(NSURL *)url
  sourceApplication:(NSString *)sourceApplication annotation:(id)annotation {
    return [PFFacebookUtils handleOpenURL:url];
}

- (void)applicationDidBecomeActive:(UIApplication *)application {
    // Handle an interruption during the authorization flow, such as the user clicking the home button.
    [FBSession.activeSession handleDidBecomeActive];
    [FBAppEvents activateApp];
    [PFUser logOut];
}


@end
