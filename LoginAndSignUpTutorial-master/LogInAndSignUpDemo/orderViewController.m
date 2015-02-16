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
    [self addObserver:self forKeyPath:@"weight" options:NSKeyValueObservingOptionNew context:nil];
    PFUser *user = [self.tripObject valueForKey:@"traveler"];
    NSString *idd = [user objectId];
    PFUser *trueUser = [PFQuery getUserObjectWithId:idd];
    self.traveler=trueUser;
}
-(void)observeValueForKeyPath:(NSString *)keyPath ofObject:(id)object change:(NSDictionary *)change context:(void *)context{
    self.weightLabel.text = [NSString stringWithFormat:@"%d",self.weight];
}
- (IBAction)plusButton:(id)sender {
    self.weight+=1;
}
- (IBAction)minusButton:(id)sender {
    if(self.weight>0){
        self.weight-=1;
    }
}
- (IBAction)order:(id)sender {
    PFObject *request = [PFObject objectWithClassName:@"request"];
    [request setObject:self.traveler forKey:@"traveler"];
    [request setObject:[PFUser currentUser] forKey:@"Requester"];
    [request setObject:self.productDescription.text forKey:@"moreInfo"];
    [request setValue:[NSNumber numberWithInt:self.weight]forKey:@"weightRequested"];
    [request setValue:self.tripObject forKey:@"tripId"];
    [request setValue:[NSNumber numberWithBool:false] forKey:@"accepted"];
    [request setValue:[NSNumber numberWithBool:false] forKey:@"deliveryStatus"];
    [request setValue:[NSNumber numberWithBool:false] forKey:@"paymentStatus"];
    [request saveInBackgroundWithBlock:^(BOOL succeeded, NSError *error) {
        if(succeeded){
            UIAlertView *success = [[UIAlertView alloc] initWithTitle:@"Success" message:@"Your order has been confirmed. An email will be sent shortly to the traveler" delegate:self cancelButtonTitle:@"Cool" otherButtonTitles: nil];
            [success show];
            [self sendEmail];
        }
        else{
            UIAlertView *failure = [[UIAlertView alloc] initWithTitle:@"Error" message:[error description] delegate:self cancelButtonTitle:@"Cool" otherButtonTitles: nil];
            [failure show];
        }
    }];
}
-(void)sendEmail{
    if(self.traveler){
    [PFCloud callFunctionInBackground:@"email" withParameters:@{@"email": [self.traveler email], @"text": self.productDescription.text,@"subject":@"You have a new Airspress Order",@"from_email":[[PFUser currentUser] email],@"from_name":[[PFUser currentUser] username],@"to_name":[self.traveler username]} block:^(NSString *result, NSError *error) {
        if (error) {
            //error
            NSLog(@"Error");
            UIAlertView *failure = [[UIAlertView alloc] initWithTitle:@"Error" message:[error description] delegate:self cancelButtonTitle:@"Cool" otherButtonTitles: nil];
            [failure show];
        } else {
            NSLog(@"result :%@", result);
        }
    }];}

}
-(BOOL)textFieldShouldReturn:(UITextField *)textField{
    [textField resignFirstResponder];
    return YES;
}
- (IBAction)tapSomewhere:(id)sender {
    [self.paymentMethod resignFirstResponder];
}
-(void)viewWillDisappear:(BOOL)animated{
    [self removeObserver:self forKeyPath:@"weight"];
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
/*
#pragma mark - Navigation

// In a storyboard-based application, you will often want to do a little preparation before navigation
- (void)prepareForSegue:(UIStoryboardSegue *)segue sender:(id)sender {
    // Get the new view controller using [segue destinationViewController].
    // Pass the selected object to the new view controller.
}
*/

@end
