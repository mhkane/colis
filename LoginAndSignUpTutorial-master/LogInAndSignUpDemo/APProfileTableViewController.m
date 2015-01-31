//
//  APProfileTableViewController.m
//  Airspress
//
//  Created by Mohamed Kane on 1/31/15.
//
//

#import "APProfileTableViewController.h"
#import "APProfilePicTableViewCell.h"
#import "AirspressTripDetailCell.h"
NSString *const usernameKey = @"username";
NSString *const additionalKey = @"additional";
NSString *const emailKey = @"email";
NSString *const profilePicKey = @"profilePicture";
NSString *const points = @"userPoints";
NSString *const profilePicCellIdentifier = @"APProfilePicTableViewCell";
NSString *const AirspressTripDetailIdentifier= @"AirspressTripDetailCell";
@interface APProfileTableViewController ()
@property NSArray *userKeys;
@property NSMutableDictionary *userInfo;
@end
@implementation APProfileTableViewController

- (void)viewDidLoad {
    [super viewDidLoad];
    self.userKeys= @[additionalKey,emailKey,points];
    if(!self.user){
        self.user = [PFUser currentUser];
    }
    self.userInfo = [[NSMutableDictionary alloc] init];
    for(NSString *userKey in self.userKeys){
        if([self.user valueForKey:userKey]){
            [self.userInfo setValue:[self.user valueForKey:userKey] forKey:userKey];
        }
    }
    [self.tableView reloadData];
    
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
    // Return the number of sections.
    return 1;
}

- (NSInteger)tableView:(UITableView *)tableView numberOfRowsInSection:(NSInteger)section {
    // Return the number of rows in the section.
    return [self.userInfo count];
}


- (UITableViewCell *)tableView:(UITableView *)tableView cellForRowAtIndexPath:(NSIndexPath *)indexPath {
        if(indexPath.row>0&&indexPath.row<=[self.userInfo count]){
            AirspressTripDetailCell *cell = (AirspressTripDetailCell *)[tableView dequeueReusableCellWithIdentifier:AirspressTripDetailIdentifier];
            cell.thumbnailImageView.image = [UIImage imageNamed:@"mapIcon"];
            if (cell == nil)
            {
                NSArray *nib = [[NSBundle mainBundle] loadNibNamed:AirspressTripDetailIdentifier owner:self options:nil];
                cell = [nib objectAtIndex:0];
                cell.thumbnailImageView.image = [UIImage imageNamed:@"mapIcon"];
            }
            NSString *keyForRow = [self.userKeys objectAtIndex:indexPath.row];

            cell.nameLabel.text= keyForRow;
            cell.detailLabel.text = [self.userInfo valueForKey:keyForRow];
            return cell;
        }
        else if(indexPath.row==0){
        APProfilePicTableViewCell *cell = (APProfilePicTableViewCell *)[tableView dequeueReusableCellWithIdentifier:profilePicCellIdentifier];
            if (cell == nil)
            {
                NSArray *nib = [[NSBundle mainBundle] loadNibNamed:profilePicCellIdentifier owner:self options:nil];
                cell = [nib objectAtIndex:0];
            }
            cell.userLabel.text = self.user.username;
            PFUser *userForCell = self.user;
            PFFile *profilePic = [userForCell objectForKey:profilePicKey];
            [profilePic getDataInBackgroundWithBlock:^(NSData *data, NSError *error) {
                UIImage *image = [[UIImage alloc]init];
                if(error){
                    UIAlertView *error = [[UIAlertView alloc] initWithTitle:@"Error" message:[error description] delegate:self cancelButtonTitle:@"Okay" otherButtonTitles: nil];
                    [error show];
                }
                else{
                    if(data!=nil){
                    image = [UIImage imageWithData:data];
                    }
                    cell.profilePicture.image=image;
                    cell.profilePicture.layer.cornerRadius = cell.profilePicture.frame.size.width / 2;
                    cell.profilePicture.clipsToBounds = YES;
                    cell.profilePicture.layer.borderWidth = 3.0f;
                    cell.profilePicture.layer.borderColor = [UIColor whiteColor].CGColor;

                }
            }];
        
            return cell;
        }
        else{
            return [[UITableViewCell alloc] init];
        }
}
- (CGFloat)tableView:(UITableView *)tableView heightForRowAtIndexPath:(NSIndexPath *)indexPath
{
    if(indexPath.row==0){
        return 172;}
    return 60;
    
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
#pragma mark - Table view delegate

// In a xib-based application, navigation from a table can be handled in -tableView:didSelectRowAtIndexPath:
- (void)tableView:(UITableView *)tableView didSelectRowAtIndexPath:(NSIndexPath *)indexPath {
    // Navigation logic may go here, for example:
    // Create the next view controller.
    <#DetailViewController#> *detailViewController = [[<#DetailViewController#> alloc] initWithNibName:<#@"Nib name"#> bundle:nil];
    
    // Pass the selected object to the new view controller.
    
    // Push the view controller.
    [self.navigationController pushViewController:detailViewController animated:YES];
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
