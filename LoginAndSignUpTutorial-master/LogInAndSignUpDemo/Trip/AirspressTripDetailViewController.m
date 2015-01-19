//
//  RouteTableViewController.m
//  FoxtrotiOS
//
//  Created by Mohamed Kane on 1/13/15.
//  Copyright (c) 2015 Mohamed Kane. All rights reserved.
//

#import "AirspressTripDetailViewController.h"

@interface AirspressTripDetailViewController ()
@property NSMutableArray *trueDetails;
@property NSMutableArray *titles;
@end

@implementation AirspressTripDetailViewController

-(void)initializeWithData{
    if(self){
    self.trueDetails = [[NSMutableArray alloc] init];
    self.titles = [[NSMutableArray alloc] init];
    NSString *tripDetails = @"Trip details";
    NSDateFormatter *df2 =[[NSDateFormatter alloc] init];
    [df2 setDateFormat:@"EEE,d MMM yyyy"];
    NSString *toLocation = [self.tripObject objectForKey:@"toLocation"];
    NSString *fromLocation = [self.tripObject objectForKey:@"fromLocation"];
    NSDate *departureDate = [self.tripObject objectForKey:@"departureDate"];
    NSString *departureDateString = [df2 stringFromDate:departureDate];
    NSDate *arrivalDate = [self.tripObject objectForKey:@"arrivalDate"];
    NSString *arrivalDateString = [df2 stringFromDate:arrivalDate];
    NSNumber *availCapacity = [self.tripObject objectForKey:@"availCapacity"];
    PFUser *user = [self.tripObject valueForKey:@"traveler"];
    NSString *idd = [user objectId];
    PFUser *trueUser = [PFQuery getUserObjectWithId:idd];
    NSString *travelerName = [trueUser username];
    NSString *email = [trueUser email];
    NSString *telephone = [trueUser objectForKey:@"additional"];
    if(tripDetails){
        [self.trueDetails addObject:tripDetails];
        [self.titles addObject:@""];
    }
    if(departureDateString){
        [self.trueDetails addObject:departureDateString];
        [self.titles addObject:@"Departure Date"];
    }
    if(arrivalDateString){
        [self.trueDetails addObject:arrivalDateString];
        [self.titles addObject:@"Arrival Date"];
    }
    if(fromLocation){
        [self.trueDetails addObject:fromLocation];
        [self.titles addObject:@"Travelling from"];
    }
    if(toLocation){
        [self.trueDetails addObject:toLocation];
        [self.titles addObject:@"Travelling to"];
    }
    if(availCapacity){
        
        if(availCapacity<[NSNumber numberWithInt:2]){
            [self.trueDetails addObject:[NSString stringWithFormat:@"%@ Kg",availCapacity]];
        }
        [self.trueDetails addObject:[NSString stringWithFormat:@"%@ Kgs",availCapacity]];
        [self.titles addObject:@"Available Capacity (in Kg)"];
    }
    if(travelerName){
        [self.trueDetails addObject:travelerName];
        [self.titles addObject:@"Traveler's name"];
    }
    if(email){
        [self.trueDetails addObject:email];
        [self.titles addObject:@"Email"];
    }
    if(telephone){
        [self.trueDetails addObject:telephone];
        [self.titles addObject:@"Telephone"];
    }}
    

}
-(void)viewWillAppear:(BOOL)animated{
    // NSArray *labelTitle = @[@"",@"Departure Date",@"Arrival Date",@"Travelling from",@"Travelling to",@"Available Space (in Kg)",@"Traveler Name", @"Email",@"Telephone"];
    [self initializeWithData];
   
   }
- (void)viewDidLoad {
    [self initializeWithData];
    [super viewDidLoad];
   
    // Uncomment the following line to preserve selection between presentations.
    // self.clearsSelectionOnViewWillAppear = NO;
    
    // Uncomment the following line to display an Edit button in the navigation bar for this view controller.
    // self.navigationItem.rightBarButtonItem = self.editButtonItem;
    UIBarButtonItem *showMap = [[UIBarButtonItem alloc] initWithTitle:@"Order" style:UIBarButtonItemStylePlain target:self action:@selector(showMap)];
    self.navigationItem.rightBarButtonItem=showMap;
    self.navigationItem.title=@"Trip information";
}

-(void)showMap{
    NSLog(@"Touched");
  
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
    NSLog(@"Count : %d",[self.titles count]);
    return [self.titles count];
    [self.tableView reloadData];
}



- (UITableViewCell *)tableView:(UITableView *)tableView cellForRowAtIndexPath:(NSIndexPath *)indexPath {
    static NSString *simpleTableIdentifier = @"AirspressTripDetailCell";
    AirspressTripDetailCell *cell = (AirspressTripDetailCell *)[tableView dequeueReusableCellWithIdentifier:simpleTableIdentifier];
    if(indexPath.row<[self.titles count]){
        if (cell == nil)
        {
            NSArray *nib = [[NSBundle mainBundle] loadNibNamed:simpleTableIdentifier owner:self options:nil];
            cell = [nib objectAtIndex:0];
        }
        if(indexPath.row==0){
            cell.backgroundView = [[UIImageView alloc] initWithImage:[ [UIImage imageNamed:@"takeoff3.jpg"] stretchableImageWithLeftCapWidth:0.0 topCapHeight:5.0] ];}
        cell.detailLabel.text = [self.trueDetails objectAtIndex:indexPath.row];
        cell.nameLabel.text=[self.titles objectAtIndex:indexPath.row];
    }
    return cell;
}
- (CGFloat)tableView:(UITableView *)tableView heightForRowAtIndexPath:(NSIndexPath *)indexPath
{
    if(indexPath.row==0){
        return 240;
    }
    return 54;
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
