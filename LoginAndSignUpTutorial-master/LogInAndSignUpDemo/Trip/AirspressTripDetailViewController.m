//
//  RouteTableViewController.m
//  FoxtrotiOS
//
//  Created by Mohamed Kane on 1/13/15.
//  Copyright (c) 2015 Mohamed Kane. All rights reserved.
//

#import "FoxtrotRouteTableViewController.h"
#import "FoxtrotMapViewController.h"
#import "FoxtrotRouteTableViewCell.h"
#import "GoogleMapsViewController.h"


@interface FoxtrotRouteTableViewController ()

@end

@implementation FoxtrotRouteTableViewController

-(void)viewWillAppear:(BOOL)animated{
}
- (void)viewDidLoad {
    [super viewDidLoad];
    // Uncomment the following line to preserve selection between presentations.
    // self.clearsSelectionOnViewWillAppear = NO;
    
    // Uncomment the following line to display an Edit button in the navigation bar for this view controller.
    // self.navigationItem.rightBarButtonItem = self.editButtonItem;
    UIBarButtonItem *showMap = [[UIBarButtonItem alloc] initWithTitle:@"Show on a Map" style:UIBarButtonItemStylePlain target:self action:@selector(showMap)];
    self.navigationItem.rightBarButtonItem=showMap;
    self.navigationItem.title=@"Your itinerary";
    _manager = [[FoxtrotAPICallManager alloc] init];
    _manager.delegate=self;
    NSString *urlString = @"https://gist.githubusercontent.com/pcoughran/26f998592c4f9210751d/raw/7f660226b4e16e25422375f44813d8fa5b40df5b/gistfile1.json";
    [_manager fetchRouteWithString:urlString];
}

-(void)showMap{
    NSMutableArray *routePoint = _routePoints;
    GoogleMapsViewController *detailViewController = [[GoogleMapsViewController alloc] initWithAnnotations:routePoint];
    // Pass the selected object to the new view controller.
    [self.navigationController pushViewController:detailViewController animated:false];
}
- (void)didReceiveRoute:(FoxtrotRoute *)route{
    _routePoints = route.routePoints;
}
-(NSString *)giveRequestForRouteWithRoute:(NSMutableArray *) routePoints{
    NSString *directionBaseURL = @"https://maps.googleapis.com/maps/api/directions/json?origin=";
    FoxtrotRoutePoint *origin = [_routePoints firstObject];
    NSString *originString = [NSString stringWithFormat:@"%f,%f",origin.lat,origin.lng];
    NSMutableString *url = [[NSMutableString alloc]initWithString:[directionBaseURL stringByAppendingString:originString]];
    [url appendString:@"&destination="];
    if([routePoints count]>2){
        NSString *destinationString = [NSString stringWithFormat:@"%f,%f",origin.lat,origin.lng];
        int count = [routePoints count];
        FoxtrotRoutePoint *destination = [routePoints objectAtIndex:count-2];
    }
    else if([routePoints count]==2){
        NSString *destinationString = [NSString stringWithFormat:@"%f,%f",origin.lat,origin.lng];
        FoxtrotRoutePoint *destination = [routePoints objectAtIndex:1];
    }
    else if([routePoints count]==1){
        NSString *destinationString = [NSString stringWithFormat:@"%f,%f",origin.lat,origin.lng];
        int count = [routePoints objectAtIndex:1];
    }
    return @"";
}
-(void)askForDirectionsWithRoutePoints:(NSMutableArray *)routePoints{
   /* FoxtrotRoutePoint *origin = [_routePoints firstObject];
    NSString *originString = [NSString stringWithFormat:@"%f,%f",origin.lat,origin.lng];
    NSMutableString *url = [baseURLString stringByAppendingString:originString];
    [url appendString:@"&destination"];
    int count = [_routePoints count];*/
}
- (void)fetchingRouteFailedWithError:(NSError *)error{
    UIAlertView *errorAlert = [[UIAlertView alloc] initWithTitle:@"Error" message:[NSString stringWithFormat:@"%@",[error description]] delegate:self cancelButtonTitle:@"Okay" otherButtonTitles: nil];
    [errorAlert show];
}
- (void)didReceiveMemoryWarning {
    [super didReceiveMemoryWarning];
    // Dispose of any resources that can be recreated.
}
#pragma mark - Table view data source
- (NSInteger)numberOfSectionsInTableView:(UITableView *)tableView {
#warning Potentially incomplete method implementation.
    // Return the number of sections.
    return 1;
}
- (NSInteger)tableView:(UITableView *)tableView numberOfRowsInSection:(NSInteger)section {
#warning Incomplete method implementation.
    // Return the number of rows in the section.
    return [_routePoints count];
    [self.tableView reloadData];
}


- (UITableViewCell *)tableView:(UITableView *)tableView cellForRowAtIndexPath:(NSIndexPath *)indexPath {
    static NSString *simpleTableIdentifier = @"FoxtrotRouteTableViewCell";
    
    FoxtrotRouteTableViewCell *cell = (FoxtrotRouteTableViewCell *)[tableView dequeueReusableCellWithIdentifier:simpleTableIdentifier];
    if (cell == nil)
    {
        NSArray *nib = [[NSBundle mainBundle] loadNibNamed:simpleTableIdentifier owner:self options:nil];
        cell = [nib objectAtIndex:0];
    }
    FoxtrotRoutePoint *routePoint = [_routePoints objectAtIndex:indexPath.row];
    routePoint.index=indexPath.row;
    
    cell.nameLabel.text = routePoint.stop_name;
    /*cell.thumbnailImageView.image = [UIImage imageNamed:[thumbnails objectAtIndex:indexPath.row]];*/
    
    cell.prepTimeLabel.text =[NSString stringWithFormat:@"%ld",(long)indexPath.row];
    cell.thumbnailImageView.image = [UIImage imageNamed:@"mapIcon"];
    
    return cell;
}
- (CGFloat)tableView:(UITableView *)tableView heightForRowAtIndexPath:(NSIndexPath *)indexPath
{
    return 78;
}


/*
// Override to support conditional editing of the table view.
- (BOOL)tableView:(UITableView *)tableView canEditRowAtIndexPath:(NSIndexPath *)indexPath {
    // Return NO if you do not want the specified item to be editable.
    return YES;
}
*/

/*
// Override to support editing the table view.
- (void)tableView:(UITableView *)tableView commitEditingStyle:(UITableViewCellEditingStyle)editingStyle forRowAtIndexPath:(NSIndexPath *)indexPath {
    if (editingStyle == UITableViewCellEditingStyleDelete) {
        // Delete the row from the data source
        [tableView deleteRowsAtIndexPaths:@[indexPath] withRowAnimation:UITableViewRowAnimationFade];
    } else if (editingStyle == UITableViewCellEditingStyleInsert) {
        // Create a new instance of the appropriate class, insert it into the array, and add a new row to the table view
    }   
}
*/

/*
// Override to support rearranging the table view.
- (void)tableView:(UITableView *)tableView moveRowAtIndexPath:(NSIndexPath *)fromIndexPath toIndexPath:(NSIndexPath *)toIndexPath {
}
*/

/*
// Override to support conditional rearranging of the table view.
- (BOOL)tableView:(UITableView *)tableView canMoveRowAtIndexPath:(NSIndexPath *)indexPath {
    // Return NO if you do not want the item to be re-orderable.
    return YES;
}
*/


#pragma mark - Table view delegate

// In a xib-based application, navigation from a table can be handled in -tableView:didSelectRowAtIndexPath:
- (void)tableView:(UITableView *)tableView didSelectRowAtIndexPath:(NSIndexPath *)indexPath {
    // Navigation logic may go here, for example:
    // Create the next view controller.
    FoxtrotRoutePoint *routePoint = [_routePoints objectAtIndex:indexPath.row];
    GoogleMapsViewController *detailViewController = [[GoogleMapsViewController alloc] initWithAnnotations:@[routePoint]];
    
    // Pass the selected object to the new view controller.
    self.tabBarController.tabBar.hidden=YES;
    [self.navigationController pushViewController:detailViewController animated:false];
    

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
