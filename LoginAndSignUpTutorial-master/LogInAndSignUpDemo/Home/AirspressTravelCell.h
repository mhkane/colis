//
//  FoxtrotRouteTableViewCell.h
//  FoxtrotiOS
//
//  Created by Mohamed Kane on 1/15/15.
//  Copyright (c) 2015 Mohamed Kane. All rights reserved.
//

#import <UIKit/UIKit.h>

@interface AirspressTravelCell : UITableViewCell
@property (weak, nonatomic) IBOutlet UILabel *dateLabel;
@property (nonatomic, weak) IBOutlet UILabel *nameLabel;
@property (nonatomic, weak) IBOutlet UILabel *toLabel;
@property (nonatomic, weak) IBOutlet UIImageView *thumbnailImageView;
@property (weak, nonatomic) IBOutlet UILabel *fromLabel;
@end
