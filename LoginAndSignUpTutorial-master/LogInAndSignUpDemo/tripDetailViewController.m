//
//  tripDetailViewController.m
//  Airspress
//
//  Created by Mohamed Kane on 12/18/14.
//
//

#import "tripDetailViewController.h"
#import "deliveryRequestViewController.h"
#import "orderViewController.h"

@interface tripDetailViewController ()

@end

@implementation tripDetailViewController

-(id)initWithMessage:(NSString *) message{
    self=[super init];
    self.message=message;
    self.tripDetails.text=message;
    self.tripDetails.attributedText=[[NSAttributedString alloc] initWithString:message];
    return self;
    
}

-(void)viewWillAppear:(BOOL)animated{
    [super viewWillAppear:animated];
    NSLog(@"Here is my message %@",self.message);
}

- (void)viewDidLoad {
    [super viewDidLoad];
    NSLog(@"Here is my text %@",self.tripDetails.text);
    self.tripDetails.text=self.message;

    // Do any additional setup after loading the view from its nib.
}

- (IBAction)order:(id)sender {
    [self.navigationController pushViewController:[[orderViewController alloc] init] animated:false];
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
