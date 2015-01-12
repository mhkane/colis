//
//  Confirmation2ViewController.m
//  Airspress
//
//  Created by Mohamed Kane on 1/11/15.
//
//

#import "Confirmation2ViewController.h"


@interface Confirmation2ViewController ()

@end

@implementation Confirmation2ViewController

- (void)viewDidLoad {
    [super viewDidLoad];
    // Do any additional setup after loading the view from its nib.
    
    self.button2 = [JSQFlatButton buttonWithType:UIButtonTypeRoundedRect];
    self.button2.normalBackgroundColor = [UIColor colorWithRed:1.0f green:0.58f blue:0.21f alpha:1.0f];
    self.button2.normalForegroundColor = [UIColor blackColor];
    [self.button2 setFlatTitle:@"Confirm Delivery"];
    [self.button2 setFlatImage:[UIImage imageNamed:@"airplane68.png"]];
    self.button2.cornerRadius = 12.0f;
    self.button2.borderWidth = 1.0f;
    self.button2.normalBorderColor = [UIColor blackColor];
    self.button2.highlightedBorderColor = [UIColor blackColor];
    /*[button addTarget:self
               action:@selector(aMethod:)
     forControlEvents:UIControlEventTouchUpInside];*/
    //[button setTitle:@"Show View" forState:UIControlStateNormal];
    self.button2.frame = CGRectMake(80.0, 210.0, 160.0, 40.0);
    [self.view addSubview:self.button2];
    
    self.button1 = [JSQFlatButton buttonWithType:UIButtonTypeRoundedRect];
    self.button1.normalBackgroundColor = [UIColor colorWithRed:1.0f green:0.58f blue:0.21f alpha:1.0f];
    self.button1.normalForegroundColor = [UIColor blackColor];
    [self.button1 setFlatTitle:@"Confirm Receiving"];
    [self.button1 setFlatImage:[UIImage imageNamed:@"shopping2.png"]];
    self.button1.cornerRadius = 12.0f;
    self.button1.borderWidth = 1.0f;
    self.button1.normalBorderColor = [UIColor blackColor ];
    self.button1.highlightedBorderColor = [UIColor blackColor];
    /*[button addTarget:self
     action:@selector(aMethod:)
     forControlEvents:UIControlEventTouchUpInside];*/
    //[button setTitle:@"Show View" forState:UIControlStateNormal];
    self.button1.frame = CGRectMake(80.0, 270.0, 160.0, 40.0);
    [self.view addSubview:self.button1];
    

    

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
