//
//  deliveryRequestViewController.m
//  Airspress
//
//  Created by Mohamed Kane on 11/30/14.
//
//

#import "deliveryRequestViewController.h"

@interface deliveryRequestViewController ()

@end

@implementation deliveryRequestViewController

- (void)viewDidLoad {
    [super viewDidLoad];
    // Do any additional setup after loading the view from its nib.
}
- (IBAction)acceptDelivery:(id)sender {
    UIAlertView *confirmation = [[UIAlertView alloc] initWithTitle:@"Confirmation" message:@"You have accepted this delivery. Your confirmation code is 3456Ez" delegate:self cancelButtonTitle:@"Cancel" otherButtonTitles:@"Confirm", nil];
    [confirmation show];
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
