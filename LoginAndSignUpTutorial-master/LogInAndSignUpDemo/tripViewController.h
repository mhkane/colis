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

@interface tripViewController : UIViewController <UITextFieldDelegate,UIGestureRecognizerDelegate>{
    NSArray *searchResultPlaces;
    SPGooglePlacesAutocompleteQuery *searchQuery;
    BOOL shouldBeginEditing;
}
@property NSArray *options;
//- (NSArray *)locationsFromJSONFile:(NSURL *)url;
@property (weak, nonatomic) IBOutlet UIDatePicker *tripDate;
@property (strong, nonatomic) IBOutlet UITapGestureRecognizer *tapGesture;
@property BOOL isDepartureDate;

@end
