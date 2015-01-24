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
- (IBAction)nextButton:(id)sender {
    if(self.isDepartureDate){
    tripViewController *newTrip = [[tripViewController alloc] init];
        newTrip.isDepartureDate=false;
        [self.navigationController pushViewController:newTrip animated:false];}
    SPGooglePlacesAutocompleteViewController * search = [[SPGooglePlacesAutocompleteViewController alloc] init];
    self.navigationController.navigationBar.hidden=YES;
    [self.navigationController pushViewController:search animated:false];



   
    
}
- (void)viewDidLoad {
    [super viewDidLoad];
    // Do any additional setup after loading the view from its nib.
   /* NSURL *city = [NSURL URLWithString:@"https://gist.githubusercontent.com/tdreyno/4278655/raw/airports.json"];
    tripViewController *trip = [[tripViewController alloc] init];
    NSArray *cityList = [trip locationsFromJSONFile:city];
    NSLog(@" Here is the count %d",[cityList count]);
    
    NSLog([cityList description]);*/
   self.tapGesture = [[UITapGestureRecognizer alloc] initWithTarget:self
                                                            action:@selector(didTapAnywhere:)]
    ;}

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
