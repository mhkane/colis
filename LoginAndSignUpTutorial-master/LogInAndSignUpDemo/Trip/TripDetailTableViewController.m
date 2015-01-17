//
//  TripDetailTableViewController.m
//  
//
//  Created by Mohamed Kane on 1/16/15.
//
//

#import "TripDetailTableViewController.h"

@interface TripDetailTableViewController ()

@end

@implementation TripDetailTableViewController

- (void)viewDidLoad {
    [super viewDidLoad];
    
    // Uncomment the following line to preserve selection between presentations.
    // self.clearsSelectionOnViewWillAppear = NO;
    
    // Uncomment the following line to display an Edit button in the navigation bar for this view controller.
    // self.navigationItem.rightBarButtonItem = self.editButtonItem;
}

- (void)didReceiveMemoryWarning {
    [super didReceiveMemoryWarning];
    // Dispose of any resources that can be recreated.
}

#pragma mark - Table view data source

- (NSInteger)numberOfSectionsInTableView:(UITableView *)tableView {
#warning Potentially incomplete method implementation.
    // Return the number of sections.
    return 0;
}

- (NSInteger)tableView:(UITableView *)tableView numberOfRowsInSection:(NSInteger)section {
#warning Incomplete method implementation.
    // Return the number of rows in the section.
    return 8;
}


- (UITableViewCell *)tableView:(UITableView *)tableView cellForRowAtIndexPath:(NSIndexPath *)indexPath {
    static NSString *CellIdentifier = @"tripDetailCell";
    
    tripDetailCell *cell = (tripDetailCell *)[tableView dequeueReusableCellWithIdentifier:CellIdentifier];
    if (cell == nil)
    {
        NSArray *nib = [[NSBundle mainBundle] loadNibNamed:CellIdentifier owner:self options:nil];
        cell = [nib objectAtIndex:0];
    }
    // Configure the cell
    PFObject *tripForView= self.tripObject;
    PFUser *user = [tripForView valueForKey:@"traveler"];
    NSString *idd = [user objectId];
    PFUser *trueUser = [PFQuery getUserObjectWithId:idd];
    NSString *travelerName = [trueUser username];
    switch(indexPath.row){
        case 0:
            cell.titleLabel.text=@"Traveler";
            cell.detailTextLabel.text=travelerName;
            cell.icon.image = [UIImage imageNamed:@"traveler"];
            break;
        case 1:
            cell.titleLabel.text=@"Travelling from";
            cell.detailTextLabel.text=[tripForView objectForKey:@"fromLocation"];
            cell.icon.image=[UIImage imageNamed:@"fromIcon"];
            break;
        case 2:
            cell.titleLabel.text=@"Travelling to";
            cell.detailTextLabel.text=[tripForView objectForKey:@"toLocation"];
            cell.icon.image=[UIImage imageNamed:@"toIcon"];
            break;
        case 3:
            cell.titleLabel.text=@"Arrival Date";
            NSDate *travelDate = [self.tripObject objectForKey:@"arrivalDate"];
            NSDateFormatter *df2 =[[NSDateFormatter alloc] init];
            NSString *dateString = [df2 stringFromDate:travelDate];
            [df2 setDateFormat:@"EEE,d MMM yyyy"];
            cell.detailTextLabel.text=[tripForView objectForKey:@"toLocation"];
            cell.icon.image=[UIImage imageNamed:@"toIcon"];
            cell.detailTextLabel.text=dateString;
            break;
        /*case 4:
            cell.titleLabel.text=@"Space (in Kg)";
            cell.detailTextLabel.text= [tripForView objectForKey:@"availCapacity"];
            cell.icon.image=[UIImage imageNamed:@"suitcase"];
            break;
        case 5:
            cell.titleLabel.text=@"Email";
            cell.detailTextLabel.text= [trueUser objectForKey:@"email"];
            cell.icon.image=[UIImage imageNamed:@"email"];
            break;*/

    }
    return cell;
    
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

/*
#pragma mark - Navigation

// In a storyboard-based application, you will often want to do a little preparation before navigation
- (void)prepareForSegue:(UIStoryboardSegue *)segue sender:(id)sender {
    // Get the new view controller using [segue destinationViewController].
    // Pass the selected object to the new view controller.
}
*/

@end
