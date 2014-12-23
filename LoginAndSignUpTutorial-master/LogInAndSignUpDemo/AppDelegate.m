//
//  AppDelegate.m
//  LogInAndSignUpDemo
//
//  Created by Mattieu Gamache-Asselin on 6/14/12.
//  Copyright (c) 2013 Parse. All rights reserved.
//

#import "AppDelegate.h"
#import "DemoTableViewController.h"
#import "SubclassConfigViewController.h"
#import "tripViewController.h"
#import "deliveryRequestViewController.h"
#import "deliverersViewController.h"
#import "orderViewController.h"
#import "tripDetailViewController.h"
#import "searchViewController.h"

#import <FacebookSDK/FacebookSDK.h>

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
    UITabBarController *menu = [[UITabBarController alloc] init];
    deliveryRequestViewController *delivery = [[deliveryRequestViewController alloc]init];
    tripViewController *trip = [[tripViewController alloc] init];
    orderViewController *order = [[orderViewController alloc] init];
    deliverersViewController *travelers = [[deliverersViewController alloc]init];
    [[travelers tabBarItem] setTitle:@"travelers"];
    [[order tabBarItem] setTitle:@"order"];
    [[trip tabBarItem] setTitle:@"trip"];
    [[delivery tabBarItem] setTitle:@"delivery"];
    NSArray *views = @[delivery,trip,order];
    [menu setViewControllers:views];
    self.window = [[UIWindow alloc] initWithFrame:[[UIScreen mainScreen] bounds]];
    SubclassConfigViewController *login =[[SubclassConfigViewController alloc]init];
    self.window.rootViewController = login;
    PFInstallation *currentInstallation = [PFInstallation currentInstallation];
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
}

@end
