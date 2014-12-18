//
//  tripDetailViewController.m
//  Airspress
//
//  Created by Mohamed Kane on 12/18/14.
//
//

#import "tripDetailViewController.h"

@interface tripDetailViewController ()

@end

@implementation tripDetailViewController

-(void)viewWillAppear:(BOOL)animated{
    self.tripDetails.text = [NSString stringWithFormat:@"%@ has %@",[[self.trip valueForKey:@"traveler"] valueForKey:@"username"],[self.trip valueForKey:@"text"]];
}

- (void)viewDidLoad {
    [super viewDidLoad];
    // Do any additional setup after loading the view from its nib.
}

- (void)didReceiveMemoryWarning {
    [super didReceiveMemoryWarning];
    // Dispose of any resources that can be recreated.
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
