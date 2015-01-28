//
//  spaceManagementViewController.m
//  Airspress
//
//  Created by Mohamed Kane on 1/24/15.
//
//

#import "spaceManagementViewController.h"
static NSString *const tripKey = @"trip";
static NSString *const fromLocationKey = @"fromLocation";
static NSString *const toLocationKey =@"toLocation";
static NSString *const departureDateKey=@"departureDate";
static NSString *const travelerKey = @"traveler";
static NSString *const arrivalDateKey = @"arrivalDate";
static NSString *const totalCapacityKey= @"totalCapacity";
static NSString *const availCapacityKey = @"availCapacity";
static NSString *const unitPriceKey = @"unitPriceUsd";
static NSString *const successTitle = @"Trip Registered";
static NSString *const succcessMessage =@"Congratulations, your flight information have been registered";
static NSString *const errorMessageTitle = @"Wrong input format";
static NSString *const errorMessageContent = @"Please, make sure that the values your enter are positive" ;
@interface spaceManagementViewController ()

@end

@implementation spaceManagementViewController

- (void)viewDidLoad {
    [super viewDidLoad];
    [self.availableSpaceField setDelegate:self];
    [self.totalSpaceField setDelegate:self];
    [self.priceField setDelegate:self];
    // Do any additional setup after loading the view from its nib.
    
    [self.totalSpaceField setText:[NSString stringWithFormat:@"%d",self.totalSpace]];
    [self.availableSpaceField setText:[NSString stringWithFormat:@"%d",self.availableSpace]];
    [self.priceField setText:[NSString stringWithFormat:@"%d",self.pricePerUnit]];
    [self addObserver:self forKeyPath:@"totalSpace" options:NSKeyValueObservingOptionNew context:nil];
    [self addObserver:self forKeyPath:@"availableSpace" options:NSKeyValueObservingOptionNew context:nil];
    [self addObserver:self forKeyPath:@"pricePerUnit" options:NSKeyValueObservingOptionNew context:nil];

   
}
-(void)observeValueForKeyPath:(NSString *)keyPath ofObject:(id)object change:(NSDictionary *)change context:(void *)context{
    [self.totalSpaceField setText:[NSString stringWithFormat:@"%d",self.totalSpace]];
    [self.availableSpaceField setText:[NSString stringWithFormat:@"%d",self.availableSpace]];
    [self.priceField setText:[NSString stringWithFormat:@"%d",self.pricePerUnit]];
}
- (IBAction)tapSomewhere:(id)sender {
    [self.totalSpaceField resignFirstResponder];
    [self.availableSpaceField resignFirstResponder];
    [self.priceField resignFirstResponder];
    
}
-(BOOL)textFieldShouldReturn:(UITextField *)textField{
    [textField resignFirstResponder];
    return YES;
}
     
- (IBAction)minusTotalSpace:(id)sender {
    if(self.totalSpace>0){
        self.totalSpace-=1;
    }
}
- (IBAction)plusTotalSpace:(id)sender {
    self.totalSpace+=1;
}
- (IBAction)minusAvailableSpace:(id)sender {
    if(self.availableSpace>0){
        self.availableSpace-=1;
    }
}
- (IBAction)plusAvailableSpace:(id)sender {
    self.availableSpace+=1;
}
- (IBAction)minusPrice:(id)sender {
    if(self.pricePerUnit>0){
        self.pricePerUnit-=1;
    }
}
- (IBAction)plusPrice:(id)sender {
    self.pricePerUnit+=1;
}
-(void)textFieldDidEndEditing:(UITextField *)textField{
    NSNumberFormatter *formatter = [[NSNumberFormatter alloc] init];
    NSNumber *textNumber = [formatter numberFromString:textField.text];
    if(textNumber.doubleValue>=0.0){
        NSLog(@"Good");
    }
    else{
        UIAlertView *alert = [[UIAlertView alloc] initWithTitle:errorMessageTitle message:errorMessageContent delegate:self cancelButtonTitle:@"Okay" otherButtonTitles: nil];
        [alert show];
    }
    
}
- (IBAction)registerTrip:(id)sender {
    NSNumberFormatter *formatter = [[NSNumberFormatter alloc] init];
    double totalSpace = [formatter numberFromString:self.totalSpaceField.text].doubleValue;
    NSLog([NSString stringWithFormat:@" total Space : %f",totalSpace]);
    double availableSpace = [formatter numberFromString:self.availableSpaceField.text].doubleValue;
    NSLog([NSString stringWithFormat:@" available Space : %f",availableSpace]);
    double pricePerUnit = [formatter numberFromString:self.priceField.text].doubleValue;
    NSLog([NSString stringWithFormat:@" Price : %f",pricePerUnit]);
    
    bool cond1 = totalSpace>=0.0;
    bool cond2 = availableSpace>=0.0;
    bool cond3 = pricePerUnit>=0.0;
    if(cond1&cond2&cond3){
        PFObject *tripObject = [PFObject objectWithClassName:tripKey];
        NSLog([NSString stringWithFormat:@"from :%@",self.tripToRegister.fromLocation]);
        [tripObject setValue:self.tripToRegister.fromLocation forKey:fromLocationKey];
        [tripObject setValue:self.tripToRegister.toLocation forKey:toLocationKey];
          NSLog([NSString stringWithFormat:@"to :%@",self.tripToRegister.toLocation]);
       [tripObject setValue:self.tripToRegister.departureDate forKey:departureDateKey];
        NSLog([NSString stringWithFormat:@"Departure :%@",self.tripToRegister.departureDate]);
       [tripObject setValue:[PFUser currentUser] forKey:travelerKey];
        NSLog([NSString stringWithFormat:@"user :%@",[PFUser currentUser]]);
        [tripObject setValue:self.tripToRegister.arrivalDate forKey:arrivalDateKey];
              NSLog([NSString stringWithFormat:@"arrival :%@",self.tripToRegister.arrivalDate]);
        [tripObject setValue:[NSNumber numberWithDouble:availableSpace] forKey:availCapacityKey];
        [tripObject setValue:[NSNumber numberWithDouble:totalSpace] forKey:totalCapacityKey];
        [tripObject setValue:[NSNumber numberWithDouble:pricePerUnit] forKey:unitPriceKey];
        [tripObject saveInBackgroundWithBlock:^(BOOL succeeded, NSError *error) {
            UIAlertView *alert = [[UIAlertView alloc] initWithTitle:successTitle message:succcessMessage delegate:self cancelButtonTitle:@"Home" otherButtonTitles: nil];
            [alert show];
        }];
    }
    else{
        UIAlertView *alert = [[UIAlertView alloc] initWithTitle:errorMessageTitle message:errorMessageContent delegate:self cancelButtonTitle:@"Okay" otherButtonTitles: nil];
        [alert show];
    }}


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
