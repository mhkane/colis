//
//  searchViewController.m
//  Airspress
//
//  Created by Mohamed Kane on 12/19/14.
//
//

#import "searchViewController.h"
#import "deliverersViewController.h"

@interface searchViewController ()

@end

@implementation searchViewController

- (void)viewDidLoad {
    [super viewDidLoad];
    // Do any additional setup after loading the view from its nib.
}

- (void)didReceiveMemoryWarning {
    [super didReceiveMemoryWarning];
    // Dispose of any resources that can be recreated.
}
- (IBAction)searchBar:(id)sender {
    bool condition1 = [self.fromTextField.text isEqualToString:@""];
    bool condition2 =[self.toTextField.text isEqualToString:@""];
    PFQuery *searchQuery = [PFQuery queryWithClassName:@"trip"];
    if(!condition1 && condition2){
        [searchQuery whereKey:@"fromLocation" equalTo:self.fromTextField.text];
    }
    else if(condition1&&condition2){
    }
    else if(condition2 && ! condition1){
        [searchQuery whereKey:@"toLocation" equalTo:self.toTextField.text];
    }
    else{
          [searchQuery whereKey:@"fromLocation" equalTo:self.fromTextField.text];
          [searchQuery whereKey:@"toLocation" equalTo:self.toTextField.text];
    }
    deliverersViewController *searchController =[[deliverersViewController alloc] init];
    searchController.query=searchQuery;
    [self presentViewController:searchController animated:false completion:nil];
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
