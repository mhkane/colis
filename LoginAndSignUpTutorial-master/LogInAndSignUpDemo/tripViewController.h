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
@property (weak, nonatomic) IBOutlet UIDatePicker *tripDate;
@property (weak, nonatomic) IBOutlet UILabel *nextLabel;
@property BOOL isDepartureDate;
@property APTrip *tripToRegister;
@property (weak, nonatomic) IBOutlet UILabel *titleLabel;
@end
