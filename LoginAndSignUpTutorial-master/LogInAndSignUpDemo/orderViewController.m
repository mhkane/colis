//
//  orderViewController.m
//  Airspress
//
//  Created by Mohamed Kane on 11/30/14.
//
//

#import "orderViewController.h"
#import <Parse/Parse.h>

@interface orderViewController ()

@end

@implementation orderViewController

- (void)viewDidLoad {
    [super viewDidLoad];
    // Do any additional setup after loading the view from its nib.
    [self.paymentMethod setDelegate:self];
  
}

-(int)pickerView:(UIPickerView *)pickerView numberOfRowsInComponent:(NSInteger)component{
    return 3;}

- (void)didReceiveMemoryWarning {
    [super didReceiveMemoryWarning];
    // Dispose of any resources that can be recreated.
}
- (NSString *)pickerView:(UIPickerView *)pickerView
             titleForRow:(NSInteger)row
            forComponent:(NSInteger)component
{
    NSArray *options = @[@"Cash",@"Credit Card",@"Mobile Payment"];
    return [options objectAtIndex:row];
}
- (IBAction)logout:(id)sender {
    [PFUser logOut];
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
