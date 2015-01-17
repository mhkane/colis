//
//  RouteTableViewController.h
//  FoxtrotiOS
//
//  Created by Mohamed Kane on 1/13/15.
//  Copyright (c) 2015 Mohamed Kane. All rights reserved.
//

#import <UIKit/UIKit.h>
#import "FoxtrotAPICaller.h"
#import "FoxtrotAPICallManagerDelegate.h"
#import "FoxtrotAPICallManager.h"
#import "FoxtrotRoutePoint.h"
#import <AFNetworking.h>
#import <AFHTTPRequestOperation.h>
#import "GoogleMapsViewController.h"




@interface FoxtrotRouteTableViewController : UITableViewController <UITableViewDataSource,UITableViewDelegate,FoxtrotAPICallManagerDelegate>{
    NSMutableArray *_routePoints;
    FoxtrotAPICallManager *_manager;
}
@property NSString *customerID;
@property NSString *driverID;




@end
