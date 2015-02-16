//
//  tripViewController.h
//  LogInAndSignUpDemo
//
//  Created by Mohamed Kane on 11/27/14.
//
//

#import <UIKit/UIKit.h>
#import "SPGooglePlacesAutocompleteViewController.h"
#import "SPGooglePlacesAutocompleteQuery.h"
#import "SPGooglePlacesAutocompleteUtilities.h"
#import "APTrip.h"
@interface tripViewController : UIViewController <UITextFieldDelegate>{
    NSArray *searchResultPlaces;
    SPGooglePlacesAutocompleteQuery *searchQuery;
    BOOL shouldBeginEditing;
}

@property NSArray *options;
//- (NSArray *)locationsFromJSONFile:(NSURL *)url;
@property (weak, nonatomic) IBOutlet UILabel *toHideArrival2;
@property (weak, nonatomic) IBOutlet UIButton *toHidenWhenArrival;
@property (strong, nonatomic) IBOutletCollection(UITextField) NSArray *textFieldToHide;
@property (strong, nonatomic) IBOutletCollection(UIButton) NSArray *buttonHidden;
@property (strong, nonatomic) IBOutletCollection(UILabel) NSArray *toBehidden;
@property (weak, nonatomic) IBOutlet UITextField *totalSpaceField;
@property (weak, nonatomic) IBOutlet UITextField *freeSpaceField;
@property (weak, nonatomic) IBOutlet UILabel *regTripLabel;
@property (weak, nonatomic) IBOutlet UIDatePicker *tripDate;
@property (weak, nonatomic) IBOutlet UILabel *nextLabel;
@property BOOL isDepartureDate;
@property APTrip *tripToRegister;
@property (weak, nonatomic) IBOutlet UILabel *titleLabel;
@property (weak, nonatomic) IBOutlet UIButton *registerTrip;
@end
