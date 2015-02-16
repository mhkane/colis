//
//  EditProfileViewController.m
//  Airspress
//
//  Created by Mohamed Kane on 12/29/14.
//
//

#import "EditProfileViewController.h"
#import "AirspressProfileViewController.h"

@interface EditProfileViewController ()

@end

@implementation EditProfileViewController
-(void)viewWillAppear:(BOOL)animated{
    PFUser *currentUser = [PFUser currentUser];
    self.biography.text = [currentUser objectForKey:@"userBio"];
    PFFile *imageFile =[currentUser objectForKey:@"profilePicture"];
    [imageFile getDataInBackgroundWithBlock:^(NSData *data, NSError *error) {
        UIImage *image = [[UIImage alloc] init];
        if(data!=nil){
            image = [UIImage imageWithData:data];
        }
        else{
           image = [UIImage imageNamed:@"userProfile.png"];
        }
        self.profilePic.image = image;
    }];
}
- (void)viewDidLoad {
    [super viewDidLoad];
    // Do any additional setup after loading the view from its nib.
    
    
}

- (void)didReceiveMemoryWarning {
    [super didReceiveMemoryWarning];
    // Dispose of any resources that can be recreated.
}
- (IBAction)doneButton:(id)sender {
    PFUser *currentUser = [PFUser currentUser];
    [currentUser setObject:self.biography.text forKey:@"userBio"];
    [currentUser save];
[[self navigationController] popViewControllerAnimated:YES];
}
-(void)imagePickerController:(UIImagePickerController *)picker didFinishPickingMediaWithInfo:(NSDictionary *)info{
    UIImage *originalImage = (UIImage *)[info objectForKey:UIImagePickerControllerOriginalImage];
    PFUser *currentUser = [PFUser currentUser];
    NSData *image = UIImagePNGRepresentation(originalImage);
    PFFile *profilePic = [PFFile fileWithData:image];
    [currentUser setObject:profilePic forKey:@"profilePicture"];
    [currentUser saveInBackgroundWithBlock:^(BOOL succeeded, NSError *error) {
        NSLog(@"Image saved");
        [picker dismissViewControllerAnimated:YES completion:nil];
    }];
}
- (IBAction)showPhotoLibrary:(id)sender {
    if (([UIImagePickerController isSourceTypeAvailable:
          UIImagePickerControllerSourceTypeSavedPhotosAlbum] == NO)) {
        return;
    }
    
    UIImagePickerController *mediaUI = [[UIImagePickerController alloc] init];
    mediaUI.sourceType = UIImagePickerControllerSourceTypePhotoLibrary;
    
    // Displays saved pictures from the Camera Roll album.
    mediaUI.mediaTypes = @[(NSString*)kUTTypeImage];
    
    // Hides the controls for moving & scaling pictures
    mediaUI.allowsEditing = NO;
    
    mediaUI.delegate = self;
    [self.navigationController presentViewController:mediaUI animated:true completion:nil];
}




@end
