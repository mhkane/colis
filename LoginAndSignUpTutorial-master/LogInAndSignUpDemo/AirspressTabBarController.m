//
//  AirspressTabBarController.m
//  Airspress
//
//  Created by Mohamed Kane on 12/24/14.
//
//

#import "AirspressTabBarController.h"
#import "orderViewController.h"
#import "tripViewController.h"
#import "SPGooglePlacesAutocompleteViewController.h"

@interface AirspressTabBarController ()
@property (nonatomic,strong) UINavigationController *navController;
@end

@implementation AirspressTabBarController
@synthesize navController;


- (void)viewDidLoad {
    [super viewDidLoad];
    //[[self tabBar] setBackgroundImage:[UIImage imageNamed:@"BackgroundTabBar.png"]];
    //    [[self tabBar] setSelectionIndicatorImage:[UIImage imageNamed:@"BackgroundTabBarItemSelected.png"]];
    // self.tabBar.tintColor = [UIColor colorWithRed:139.0f/255.0f green:111.0f/255.0f blue:95.0f/255.0f alpha:1.0f];
    // iOS 7 style
    self.tabBar.tintColor = [UIColor colorWithRed:254.0f/255.0f green:149.0f/255.0f blue:50.0f/255.0f alpha:1.0f];
    self.tabBar.barTintColor = [UIColor colorWithRed:0.0f/255.0f green:0.0f/255.0f blue:0.0f/255.0f alpha:1.0f];
     self.navController =[self.viewControllers objectAtIndex:1];
}

- (void)didReceiveMemoryWarning {
    [super didReceiveMemoryWarning];
    // Dispose of any resources that can be recreated.
}
- (void)setViewControllers:(NSArray *)viewControllers animated:(BOOL)animated {
    [super setViewControllers:viewControllers animated:animated];
    
    UIButton *plusButton = [UIButton buttonWithType:UIButtonTypeCustom];
    plusButton.frame = CGRectMake( 94.0f, 0.0f, 131.0f, self.tabBar.bounds.size.height);
    [plusButton setImage:[UIImage imageNamed:@"plus.png"] forState:UIControlStateNormal];
    [plusButton setImage:[UIImage imageNamed:@"plus.png"] forState:UIControlStateHighlighted];
    [plusButton addTarget:self action:@selector(plusButtonAction) forControlEvents:UIControlEventTouchUpInside];
    [self.tabBar addSubview:plusButton];
    
    UISwipeGestureRecognizer *swipeUpGestureRecognizer = [[UISwipeGestureRecognizer alloc] initWithTarget:self action:@selector(handleGesture:)];
    [swipeUpGestureRecognizer setDirection:UISwipeGestureRecognizerDirectionUp];
    [swipeUpGestureRecognizer setNumberOfTouchesRequired:1];
    [plusButton addGestureRecognizer:swipeUpGestureRecognizer];
}
-(void)plusButtonAction{
    UIActionSheet *actionSheet = [[UIActionSheet alloc] initWithTitle:nil delegate:self cancelButtonTitle:@"Cancel" destructiveButtonTitle:nil otherButtonTitles:@"Add new trip",@"Add new confirmation" ,nil];
    [actionSheet showFromTabBar:self.tabBar];
}
- (void)actionSheet:(UIActionSheet *)actionSheet clickedButtonAtIndex:(NSInteger)buttonIndex {
    if (buttonIndex == 0) {
        
        SPGooglePlacesAutocompleteViewController *newTrip = [[SPGooglePlacesAutocompleteViewController alloc] init];
        APTrip *trip = [[APTrip alloc] init];
        newTrip.tripToRegister=trip;
        //Very important note : Due to this choice, all the views will be embedded in a Navigation Controller.
        UINavigationController *nav = self.selectedViewController;
        newTrip.isDepartureLecation=true;
        newTrip.navigationItem.title=@"Departure";
        newTrip.navigationController.navigationBar.hidden=YES;
        self.navigationController.navigationBar.hidden=YES;
        nav.navigationBar.hidden=YES;
        [nav pushViewController:newTrip animated:YES];
        NSLog(@"%@",[newTrip description]);
        
       // [self.navigationController pushViewController:newTrip animated:YES];
    } else if (buttonIndex == 1) {
        UIViewController *rating = [[UIViewController alloc] init];
        UINavigationController *nav = self.selectedViewController;
        [nav pushViewController:rating animated:true];
    }
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
