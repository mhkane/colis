//
//  spaceManagementViewController.m
//  Airspress
//
//  Created by Mohamed Kane on 1/24/15.
//
//

#import "spaceManagementViewController.h"

@interface spaceManagementViewController ()

@end

@implementation spaceManagementViewController

- (void)viewDidLoad {
    [super viewDidLoad];
    // Do any additional setup after loading the view from its nib.
    
}

- (void)didReceiveMemoryWarning {
    [super didReceiveMemoryWarning];
    // Dispose of any resources that can be recreated.
}

- (UITableViewCell *)tableView:(UITableView *)tableView cellForRowAtIndexPath:(NSIndexPath *)indexPath{
    static NSString *CellIdentifier = @"FormTableViewCell";
    
    FormTableViewCell *cell = (FormTableViewCell *)[tableView dequeueReusableCellWithIdentifier:CellIdentifier];
    if (cell == nil)
    {
        NSArray *nib = [[NSBundle mainBundle] loadNibNamed:CellIdentifier owner:self options:nil];
        cell = [nib objectAtIndex:0];
    }
    switch (indexPath.row) {
        case 0:
            cell.titleLabel.text=@"Total Capacity (in Kg)";
            break;
        case 1:
            cell.titleLabel.text=@"Available Capacity (in Kg)";
        case 2:
            cell.titleLabel.text= @"Price per Kg";
            break;
        default:
            break;
    }
    return cell;
}

-(NSInteger)numberOfSectionsInTableView:(UITableView *)tableView{
    return 1;
}
-(NSInteger)tableView:(UITableView *)tableView numberOfRowsInSection:(NSInteger)section{
    return 3;
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
