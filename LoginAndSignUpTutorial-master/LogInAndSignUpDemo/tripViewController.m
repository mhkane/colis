//
//  tripViewController.m
//  LogInAndSignUpDemo
//
//  Created by Mohamed Kane on 11/27/14.
//
//

#import "tripViewController.h"

@interface tripViewController ()

@end

@implementation tripViewController
-(id)initWithNibName:(NSString *)nibNameOrNil bundle:(NSBundle *)nibBundleOrNil{
    self = [super initWithNibName:nibNameOrNil bundle:nibBundleOrNil];
    
    return self;
}
-(void)viewWillAppear:(BOOL)animated{
    if(self.isDepartureDate){
        self.titleLabel.text = @"Pick your departure date";
        self.nextLabel.text = @"Next";
    }
    else{
        self.titleLabel.text = @"Pick your arrival date";
        self.nextLabel.text= @"Pick departure city";
    }
}
- (IBAction)minusTotalSpace:(id)sender {
}
- (IBAction)plusTotalSpace:(id)sender {
}
- (IBAction)minusFreeSpace:(id)sender {
}
- (IBAction)plusFreeSpace:(id)sender {
}
- (IBAction)minusPrice:(id)sender {
}
- (IBAction)plusPrice:(id)sender {
}
- (IBAction)nextButton:(id)sender {
    if(self.isDepartureDate){
    tripViewController *newTrip = [[tripViewController alloc] init];
        self.tripToRegister.departureDate=self.tripDate.date;
        newTrip.tripToRegister = self.tripToRegister;
        newTrip.isDepartureDate=false;
        [self.navigationController pushViewController:newTrip animated:false];
    }
    else{
    SPGooglePlacesAutocompleteViewController * search = [[SPGooglePlacesAutocompleteViewController alloc] init];
        self.navigationController.navigationBar.hidden=YES;
        search.isDepartureLecation=true;
        self.tripToRegister.arrivalDate=self.tripDate.date;
        search.tripToRegister=self.tripToRegister;
        [self.navigationController pushViewController:search animated:false];
    }



   
    
}
- (void)viewDidLoad {
    [super viewDidLoad];
    // Do any additional setup after loading the view from its nib.
   /* NSURL *city = [NSURL URLWithString:@"https://gist.githubusercontent.com/tdreyno/4278655/raw/airports.json"];
    tripViewController *trip = [[tripViewController alloc] init];
    NSArray *cityList = [trip locationsFromJSONFile:city];
    NSLog(@" Here is the count %d",[cityList count]);
    
    NSLog([cityList description]);*/
   }

-(BOOL)textFieldShouldReturn:(UITextField *)textField{
    [textField resignFirstResponder];
    return YES;
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
