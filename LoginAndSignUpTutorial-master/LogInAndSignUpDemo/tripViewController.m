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
    if(self){
        searchQuery = [[SPGooglePlacesAutocompleteQuery alloc] init];
        searchQuery.radius=100.0;
        shouldBeginEditing=YES;
    }
    return self;
}
- (IBAction)tapSomewhere:(id)sender {
    [self.toTextField resignFirstResponder];
    [self.fromTextField resignFirstResponder];
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
                                                            action:@selector(didTapAnywhere:)];
    self.toTextField.delegate =self;
    self.fromTextField.delegate=self;
    if(self){
        searchQuery = [[SPGooglePlacesAutocompleteQuery alloc] init];
        searchQuery.radius=100.0;
        shouldBeginEditing=YES;
    }
    
}
- (IBAction)registerTrip:(id)sender {
    PFObject *trip = [PFObject objectWithClassName:@"trip"];
    [trip setObject:self.fromTextField.text forKey:@"fromLocation"];
    [trip setObject:self.toTextField.text forKey:@"toLocation"];
    [trip setObject:self.tripDate.date forKey:@"departureDate"];
    [trip setObject:[PFUser currentUser] forKey:@"traveler"];
    NSDateFormatter *df2 = [[NSDateFormatter alloc] init];
    [df2 setDateFormat:@"EEE,d MMM yyyy"];
    NSString *dateString = [df2 stringFromDate:self.tripDate.date];
    NSString *flightString = [NSString stringWithFormat:@"Traveling from %@ to %@ on %@",self.fromTextField.text,self.toTextField.text,dateString];
    [trip setObject:flightString forKey:@"text"];
    [trip saveInBackground];
    UIAlertView *alert = [[UIAlertView alloc] initWithTitle:@"Flight registered"
                                                    message:@"Your flight have been registered" delegate:self cancelButtonTitle:@"Dismiss" otherButtonTitles: nil];
    [alert show];
                          
}
- (IBAction)addNewTrip:(id)sender {
    self.toTextField.text=@"";
    self.fromTextField.text=@"";
}
- (NSArray *)locationsFromJSONFile:(NSURL *)url {
    // Create a NSURLRequest with the given URL
    NSURLRequest *request = [NSURLRequest requestWithURL:url
                                             cachePolicy:NSURLRequestReloadIgnoringLocalAndRemoteCacheData
                                         timeoutInterval:30.0];
    
    // Get the data
    NSURLResponse *response;
    NSData *data = [NSURLConnection sendSynchronousRequest:request returningResponse:&response error:nil];
    
    // Now create a NSDictionary from the JSON data
    
    NSDictionary *jsonDictionary = [NSJSONSerialization JSONObjectWithData:data options:0 error:nil];
    NSArray *jsonList =[NSJSONSerialization JSONObjectWithData:data options:0 error:nil];
    NSMutableSet *city = [[NSMutableSet alloc] init];
    for(NSDictionary *cityDict in jsonList) {
        [city addObject:[cityDict objectForKey:@"city"]];
    }
    NSLog([city description]);
    NSDictionary *dict = [jsonList objectAtIndex:4];
    NSLog([dict description]);
    NSLog(@" Here is the count for list %d",[jsonList count]);
    
    // Create a new array to hold the locations
    NSMutableArray *locations = [[NSMutableArray alloc] init];
    
    // Get an array of dictionaries with the key "locations"
    //NSArray *array = [jsonDictionary objectForKey:@"city"];
    // Return the array of Location objects
    return locations;
}
-(void)didTapAnywhere: (UITapGestureRecognizer*) recognizer {
    [self.toTextField resignFirstResponder];
    [self.fromTextField resignFirstResponder];
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
