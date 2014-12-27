//
//  ProfileViewController.m
//  Airspress
//
//  Created by Mohamed Kane on 12/17/14.
//
//

#import "ProfileViewController.h"

@interface ProfileViewController ()

@end

@implementation ProfileViewController

- (void)viewDidLoad {
    [super viewDidLoad];
    // Do any additional setup after loading the view from its nib.
}

- (void)didReceiveMemoryWarning {
    [super didReceiveMemoryWarning];
    // Dispose of any resources that can be recreated.
}
- (void)drawCanvas1WithFrame: (CGRect)frame
{
    //// General Declarations
    CGColorSpaceRef colorSpace = CGColorSpaceCreateDeviceRGB();
    CGContextRef context = UIGraphicsGetCurrentContext();
    
    //// Color Declarations
    UIColor* gradient2Color = [UIColor colorWithRed: 1 green: 0 blue: 0 alpha: 1];
    UIColor* buttonGradientColor = [UIColor colorWithRed: 0.439 green: 0.004 blue: 0 alpha: 1];
    UIColor* color = [UIColor colorWithRed: 0.161 green: 0.039 blue: 0.349 alpha: 1];
    UIColor* color2 = [UIColor colorWithRed: 1 green: 0.486 blue: 0 alpha: 1];
    UIColor* alreadyHaveAnAccountTapToLoginColor = [UIColor colorWithRed: 1 green: 1 blue: 1 alpha: 1];
    UIColor* color3 = [UIColor colorWithRed: 0.233 green: 0.433 blue: 0.69 alpha: 1];
    UIColor* color4 = [UIColor colorWithRed: 0.271 green: 0.522 blue: 0.843 alpha: 1];
    UIColor* facebookLogoCopyColor = [UIColor colorWithRed: 1 green: 1 blue: 1 alpha: 1];
    UIColor* loginWithFACEBOOKColor = [UIColor colorWithRed: 1 green: 1 blue: 1 alpha: 1];
    UIColor* shape23Color = [UIColor colorWithRed: 0 green: 0 blue: 0 alpha: 0.129];
    UIColor* loginWithEMAILColor = [UIColor colorWithRed: 1 green: 1 blue: 1 alpha: 1];
    UIColor* aLocalMarketplaceToBuySellAllTheStuffYourKidsColor = [UIColor colorWithRed: 1 green: 1 blue: 1 alpha: 1];
    UIColor* kidshopColor = [UIColor colorWithRed: 1 green: 1 blue: 1 alpha: 1];
    UIColor* kidshopDropShadowColor = [UIColor colorWithRed: 0.011 green: 0.013 blue: 0.013 alpha: 1];
    UIColor* color22Color = [UIColor colorWithRed: 1 green: 1 blue: 1 alpha: 1];
    UIColor* chargeColor = [UIColor colorWithRed: 1 green: 1 blue: 1 alpha: 1];
    UIColor* color7 = [UIColor colorWithRed: 1 green: 1 blue: 1 alpha: 1];
    UIColor* bluetoothColor = [UIColor colorWithRed: 1 green: 1 blue: 1 alpha: 1];
    UIColor* color421PMColor = [UIColor colorWithRed: 1 green: 1 blue: 1 alpha: 1];
    UIColor* wifiColor = [UIColor colorWithRed: 1 green: 1 blue: 1 alpha: 1];
    UIColor* bELLColor = [UIColor colorWithRed: 1 green: 1 blue: 1 alpha: 1];
    UIColor* ellipse1Color = [UIColor colorWithRed: 1 green: 1 blue: 1 alpha: 1];
    
    //// Gradient Declarations
    CGFloat buttonGradientLocations[] = {0, 0.07, 1};
    CGGradientRef buttonGradient = CGGradientCreateWithColors(colorSpace, (__bridge CFArrayRef)@[(id)gradient2Color.CGColor, (id)[gradient2Color blendedColorWithFraction: 0.5 ofColor: buttonGradientColor].CGColor, (id)buttonGradientColor.CGColor], buttonGradientLocations);
    CGFloat defaultGradientVioletOrangeVioletOrangeLocations[] = {0, 1};
    CGGradientRef defaultGradientVioletOrangeVioletOrange = CGGradientCreateWithColors(colorSpace, (__bridge CFArrayRef)@[(id)color.CGColor, (id)color2.CGColor], defaultGradientVioletOrangeVioletOrangeLocations);
    CGFloat customLocations[] = {0, 1};
    CGGradientRef custom = CGGradientCreateWithColors(colorSpace, (__bridge CFArrayRef)@[(id)color3.CGColor, (id)color4.CGColor], customLocations);
    
    //// Shadow Declarations
    UIColor* innerGlowColor = UIColor.whiteColor;
    CGSize innerGlowColorOffset = CGSizeMake(0.1, -0.1);
    CGFloat innerGlowColorBlurRadius = 3;
    UIColor* kidshopDropShadow = [kidshopDropShadowColor colorWithAlphaComponent: 0.56];
    CGSize kidshopDropShadowOffset = CGSizeMake(-0.6, 0.6);
    CGFloat kidshopDropShadowBlurRadius = 1;
    
    //// Image Declarations
    UIImage* layer7Image = [UIImage imageNamed: @"layer7Image.png"];
    UIImage* layer10Image = [UIImage imageNamed: @"layer10Image.png"];
    UIImage* batteryImage = [UIImage imageNamed: @"batteryImage.png"];
    UIImage* ellipse1Image = [UIImage imageNamed: @"ellipse1Image.png"];
    UIImage* ellipse1Image2 = [UIImage imageNamed: @"ellipse1Image2.png"];
    
    //// Button
    {
        //// Rectangle Drawing
        CGRect rectangleRect = CGRectMake(CGRectGetMinX(frame) - 3, CGRectGetMinY(frame), CGRectGetWidth(frame) + 3, floor((CGRectGetHeight(frame)) * 1.00000 + 0.5));
        UIBezierPath* rectanglePath = [UIBezierPath bezierPathWithRect: rectangleRect];
        CGContextSaveGState(context);
        CGContextSetShadowWithColor(context, innerGlowColorOffset, innerGlowColorBlurRadius, [innerGlowColor CGColor]);
        CGContextBeginTransparencyLayer(context, NULL);
        [rectanglePath addClip];
        CGContextDrawLinearGradient(context, buttonGradient,
                                    CGPointMake(CGRectGetMidX(rectangleRect), CGRectGetMinY(rectangleRect)),
                                    CGPointMake(CGRectGetMidX(rectangleRect), CGRectGetMaxY(rectangleRect)),
                                    0);
        CGContextEndTransparencyLayer(context);
        CGContextRestoreGState(context);
        
        [UIColor.blackColor setStroke];
        rectanglePath.lineWidth = 2;
        [rectanglePath stroke];
    }
    
    
    //// bg GradientOverlay Drawing
    UIBezierPath* bgGradientOverlayPath = UIBezierPath.bezierPath;
    [bgGradientOverlayPath moveToPoint: CGPointMake(639.99, 1136)];
    [bgGradientOverlayPath addLineToPoint: CGPointMake(-0.01, 1136)];
    [bgGradientOverlayPath addLineToPoint: CGPointMake(-0.01, -0)];
    [bgGradientOverlayPath addLineToPoint: CGPointMake(639.99, -0)];
    [bgGradientOverlayPath addLineToPoint: CGPointMake(639.99, 1136)];
    [bgGradientOverlayPath closePath];
    CGContextSaveGState(context);
    [bgGradientOverlayPath addClip];
    CGContextDrawLinearGradient(context, defaultGradientVioletOrangeVioletOrange,
                                CGPointMake(319.99, 1136),
                                CGPointMake(319.99, -0),
                                kCGGradientDrawsBeforeStartLocation | kCGGradientDrawsAfterEndLocation);
    CGContextRestoreGState(context);
    
    
    //// Login
    {
        //// Group 3
        {
            CGContextSaveGState(context);
            CGContextSetAlpha(context, 0.76);
            CGContextBeginTransparencyLayer(context, NULL);
            
            
            //// Layer 7 Drawing
            CGContextSaveGState(context);
            CGContextTranslateCTM(context, 0, 1042);
            
            UIBezierPath* layer7Path = [UIBezierPath bezierPathWithRect: CGRectMake(-52, -1349, 767, 1455)];
            CGContextSaveGState(context);
            [layer7Path addClip];
            CGContextScaleCTM(context, 1.0, -1.0);
            CGContextDrawTiledImage(context, CGRectMake(-52, 1349, layer7Image.size.width, layer7Image.size.height), layer7Image.CGImage);
            CGContextRestoreGState(context);
            
            CGContextRestoreGState(context);
            
            
            CGContextEndTransparencyLayer(context);
            CGContextRestoreGState(context);
        }
        
        
        //// Already have an account?  Tap to Login Drawing
        CGRect alreadyHaveAnAccountTapToLoginRect = CGRectMake(63.21, 1065, 490.56, 31);
        UIFont* alreadyHaveAnAccountTapToLoginFont = [UIFont fontWithName: @"Helvetica" size: 23];
        [alreadyHaveAnAccountTapToLoginColor setFill];
        [@"Already have an account?  Tap to Login" drawInRect: alreadyHaveAnAccountTapToLoginRect withFont: alreadyHaveAnAccountTapToLoginFont lineBreakMode: NSLineBreakByWordWrapping alignment: NSTextAlignmentCenter];
        
        
        //// Facebook
        {
            //// Shape 23 GradientOverlay Drawing
            UIBezierPath* shape23GradientOverlayPath = UIBezierPath.bezierPath;
            [shape23GradientOverlayPath moveToPoint: CGPointMake(87.9, 849.24)];
            [shape23GradientOverlayPath addLineToPoint: CGPointMake(543.16, 849.24)];
            [shape23GradientOverlayPath addCurveToPoint: CGPointMake(557.56, 863.69) controlPoint1: CGPointMake(551.11, 849.24) controlPoint2: CGPointMake(557.56, 855.71)];
            [shape23GradientOverlayPath addLineToPoint: CGPointMake(557.56, 922.2)];
            [shape23GradientOverlayPath addCurveToPoint: CGPointMake(543.16, 936.65) controlPoint1: CGPointMake(557.56, 930.18) controlPoint2: CGPointMake(551.11, 936.65)];
            [shape23GradientOverlayPath addLineToPoint: CGPointMake(87.9, 936.65)];
            [shape23GradientOverlayPath addCurveToPoint: CGPointMake(73.5, 922.2) controlPoint1: CGPointMake(79.95, 936.65) controlPoint2: CGPointMake(73.5, 930.18)];
            [shape23GradientOverlayPath addLineToPoint: CGPointMake(73.5, 863.69)];
            [shape23GradientOverlayPath addCurveToPoint: CGPointMake(87.9, 849.24) controlPoint1: CGPointMake(73.5, 855.71) controlPoint2: CGPointMake(79.95, 849.24)];
            [shape23GradientOverlayPath closePath];
            CGContextSaveGState(context);
            [shape23GradientOverlayPath addClip];
            CGContextDrawLinearGradient(context, custom,
                                        CGPointMake(315.53, 936.65),
                                        CGPointMake(315.53, 849.24),
                                        kCGGradientDrawsBeforeStartLocation | kCGGradientDrawsAfterEndLocation);
            CGContextRestoreGState(context);
            
            
            //// Group 1
            {
                //// Facebook Logo copy Drawing
                UIBezierPath* facebookLogoCopyPath = UIBezierPath.bezierPath;
                [facebookLogoCopyPath moveToPoint: CGPointMake(144.6, 887.3)];
                [facebookLogoCopyPath addLineToPoint: CGPointMake(138.68, 887.3)];
                [facebookLogoCopyPath addLineToPoint: CGPointMake(138.68, 883.69)];
                [facebookLogoCopyPath addCurveToPoint: CGPointMake(140.33, 882.03) controlPoint1: CGPointMake(138.68, 882.34) controlPoint2: CGPointMake(139.65, 882.03)];
                [facebookLogoCopyPath addCurveToPoint: CGPointMake(144.5, 882.03) controlPoint1: CGPointMake(141.01, 882.03) controlPoint2: CGPointMake(144.5, 882.03)];
                [facebookLogoCopyPath addLineToPoint: CGPointMake(144.5, 876.08)];
                [facebookLogoCopyPath addLineToPoint: CGPointMake(138.75, 876.05)];
                [facebookLogoCopyPath addCurveToPoint: CGPointMake(130.92, 883.33) controlPoint1: CGPointMake(132.37, 876.05) controlPoint2: CGPointMake(130.92, 880.49)];
                [facebookLogoCopyPath addLineToPoint: CGPointMake(130.92, 887.3)];
                [facebookLogoCopyPath addLineToPoint: CGPointMake(127.23, 887.3)];
                [facebookLogoCopyPath addLineToPoint: CGPointMake(127.23, 893.42)];
                [facebookLogoCopyPath addLineToPoint: CGPointMake(130.92, 893.42)];
                [facebookLogoCopyPath addCurveToPoint: CGPointMake(130.92, 910.77) controlPoint1: CGPointMake(130.92, 901.29) controlPoint2: CGPointMake(130.92, 910.77)];
                [facebookLogoCopyPath addLineToPoint: CGPointMake(138.68, 910.77)];
                [facebookLogoCopyPath addCurveToPoint: CGPointMake(138.68, 893.42) controlPoint1: CGPointMake(138.68, 910.77) controlPoint2: CGPointMake(138.68, 901.2)];
                [facebookLogoCopyPath addLineToPoint: CGPointMake(143.92, 893.42)];
                [facebookLogoCopyPath addLineToPoint: CGPointMake(144.6, 887.3)];
                [facebookLogoCopyPath closePath];
                [facebookLogoCopyColor setFill];
                [facebookLogoCopyPath fill];
            }
            
            
            //// login with FACEBOOK Drawing
            CGRect loginWithFACEBOOKRect = CGRectMake(126.16, 879, 365, 24);
            UIFont* loginWithFACEBOOKFont = [UIFont fontWithName: @"Helvetica" size: 16.03];
            [loginWithFACEBOOKColor setFill];
            [@"login with FACEBOOK" drawInRect: loginWithFACEBOOKRect withFont: loginWithFACEBOOKFont lineBreakMode: NSLineBreakByWordWrapping alignment: NSTextAlignmentCenter];
        }
        
        
        //// Email
        {
            //// Group 8
            {
                //// Shape 23 Drawing
                UIBezierPath* shape23Path = UIBezierPath.bezierPath;
                [shape23Path moveToPoint: CGPointMake(87.9, 955.24)];
                [shape23Path addLineToPoint: CGPointMake(543.16, 955.24)];
                [shape23Path addCurveToPoint: CGPointMake(557.56, 969.69) controlPoint1: CGPointMake(551.11, 955.24) controlPoint2: CGPointMake(557.56, 961.71)];
                [shape23Path addLineToPoint: CGPointMake(557.56, 1028.2)];
                [shape23Path addCurveToPoint: CGPointMake(543.16, 1042.65) controlPoint1: CGPointMake(557.56, 1036.18) controlPoint2: CGPointMake(551.11, 1042.65)];
                [shape23Path addLineToPoint: CGPointMake(87.9, 1042.65)];
                [shape23Path addCurveToPoint: CGPointMake(73.5, 1028.2) controlPoint1: CGPointMake(79.95, 1042.65) controlPoint2: CGPointMake(73.5, 1036.18)];
                [shape23Path addLineToPoint: CGPointMake(73.5, 969.69)];
                [shape23Path addCurveToPoint: CGPointMake(87.9, 955.24) controlPoint1: CGPointMake(73.5, 961.71) controlPoint2: CGPointMake(79.95, 955.24)];
                [shape23Path closePath];
                [shape23Color setFill];
                [shape23Path fill];
            }
            
            
            //// Group 10
            {
            }
            
            
            //// login with EMAIL Drawing
            CGRect loginWithEMAILRect = CGRectMake(136.62, 985, 308, 24);
            UIFont* loginWithEMAILFont = [UIFont fontWithName: @"Helvetica" size: 16.03];
            [loginWithEMAILColor setFill];
            [@"login with EMAIL" drawInRect: loginWithEMAILRect withFont: loginWithEMAILFont lineBreakMode: NSLineBreakByWordWrapping alignment: NSTextAlignmentCenter];
            
            
            //// Layer 10 Drawing
            UIBezierPath* layer10Path = [UIBezierPath bezierPathWithRect: CGRectMake(121, 987, 32, 24)];
            CGContextSaveGState(context);
            [layer10Path addClip];
            CGContextScaleCTM(context, 1.0, -1.0);
            CGContextDrawTiledImage(context, CGRectMake(121, -987, layer10Image.size.width, layer10Image.size.height), layer10Image.CGImage);
            CGContextRestoreGState(context);
        }
        
        
        //// A local marketplace to buy & sell  all the stuff your kids  Drawing
        CGRect aLocalMarketplaceToBuySellAllTheStuffYourKidsRect = CGRectMake(101.04, 274, 441.53, 59);
        UIFont* aLocalMarketplaceToBuySellAllTheStuffYourKidsFont = [UIFont fontWithName: @"Helvetica" size: 23.22];
        [aLocalMarketplaceToBuySellAllTheStuffYourKidsColor setFill];
        [@"A local marketplace to buy & sell \nall the stuff your kids " drawInRect: aLocalMarketplaceToBuySellAllTheStuffYourKidsRect withFont: aLocalMarketplaceToBuySellAllTheStuffYourKidsFont lineBreakMode: NSLineBreakByWordWrapping alignment: NSTextAlignmentCenter];
        
        
        //// Kidshop Drawing
        CGRect kidshopRect = CGRectMake(110.22, 117, 474, 150);
        CGContextSaveGState(context);
        CGContextSetShadowWithColor(context, kidshopDropShadowOffset, kidshopDropShadowBlurRadius, [kidshopDropShadow CGColor]);
        UIFont* kidshopFont = [UIFont fontWithName: @"Helvetica" size: 118];
        [kidshopColor setFill];
        [@"Kidshop" drawInRect: kidshopRect withFont: kidshopFont lineBreakMode: NSLineBreakByWordWrapping alignment: NSTextAlignmentCenter];
        CGContextRestoreGState(context);
        
        
        
        //// Status bar white
        {
            //// Battery 2
            {
                //// Graphic 22% Drawing
                CGRect graphic22Rect = CGRectMake(425.11, 18, 148, 29);
                UIFont* graphic22Font = [UIFont fontWithName: @"HelveticaNeue" size: 24];
                [color22Color setFill];
                [@"22%" drawInRect: graphic22Rect withFont: graphic22Font lineBreakMode: NSLineBreakByWordWrapping alignment: NSTextAlignmentRight];
                
                
                //// battery Drawing
                UIBezierPath* batteryPath = [UIBezierPath bezierPathWithRect: CGRectMake(579, 22, 45, 19)];
                CGContextSaveGState(context);
                [batteryPath addClip];
                CGContextScaleCTM(context, 1.0, -1.0);
                CGContextDrawTiledImage(context, CGRectMake(579, -22, batteryImage.size.width, batteryImage.size.height), batteryImage.CGImage);
                CGContextRestoreGState(context);
                
                
                //// charge Drawing
                UIBezierPath* chargePath = UIBezierPath.bezierPath;
                [chargePath moveToPoint: CGPointMake(583, 24)];
                [chargePath addLineToPoint: CGPointMake(590, 24)];
                [chargePath addLineToPoint: CGPointMake(590, 39)];
                [chargePath addLineToPoint: CGPointMake(583, 39)];
                [chargePath addCurveToPoint: CGPointMake(581, 37) controlPoint1: CGPointMake(581.9, 39) controlPoint2: CGPointMake(581, 38.1)];
                [chargePath addLineToPoint: CGPointMake(581, 26)];
                [chargePath addCurveToPoint: CGPointMake(583, 24) controlPoint1: CGPointMake(581, 24.9) controlPoint2: CGPointMake(581.9, 24)];
                [chargePath closePath];
                [chargeColor setFill];
                [chargePath fill];
                
                
                //// Graphic + Drawing
                UIBezierPath* graphicPath = UIBezierPath.bezierPath;
                [graphicPath moveToPoint: CGPointMake(625, 28)];
                [graphicPath addCurveToPoint: CGPointMake(628, 31.5) controlPoint1: CGPointMake(626.93, 28) controlPoint2: CGPointMake(628, 29.57)];
                [graphicPath addCurveToPoint: CGPointMake(625, 35) controlPoint1: CGPointMake(628, 33.43) controlPoint2: CGPointMake(626.93, 35)];
                [graphicPath addLineToPoint: CGPointMake(625, 28)];
                [graphicPath closePath];
                [color7 setFill];
                [graphicPath fill];
            }
            
            
            //// Group 14
            {
                CGContextSaveGState(context);
                CGContextSetAlpha(context, 0.4);
                CGContextBeginTransparencyLayer(context, NULL);
                
                
                //// Bluetooth Drawing
                UIBezierPath* bluetoothPath = UIBezierPath.bezierPath;
                [bluetoothPath moveToPoint: CGPointMake(502.29, 31.49)];
                [bluetoothPath addLineToPoint: CGPointMake(507.81, 25.84)];
                [bluetoothPath addLineToPoint: CGPointMake(500.14, 17.99)];
                [bluetoothPath addLineToPoint: CGPointMake(499.94, 17.99)];
                [bluetoothPath addLineToPoint: CGPointMake(499.94, 29.08)];
                [bluetoothPath addLineToPoint: CGPointMake(494.22, 23.23)];
                [bluetoothPath addLineToPoint: CGPointMake(492.84, 24.64)];
                [bluetoothPath addLineToPoint: CGPointMake(499.53, 31.49)];
                [bluetoothPath addLineToPoint: CGPointMake(492.84, 38.34)];
                [bluetoothPath addLineToPoint: CGPointMake(494.22, 39.75)];
                [bluetoothPath addLineToPoint: CGPointMake(499.94, 33.9)];
                [bluetoothPath addLineToPoint: CGPointMake(499.94, 44.99)];
                [bluetoothPath addLineToPoint: CGPointMake(500.3, 44.99)];
                [bluetoothPath addLineToPoint: CGPointMake(507.89, 37.23)];
                [bluetoothPath addLineToPoint: CGPointMake(502.29, 31.49)];
                [bluetoothPath closePath];
                [bluetoothPath moveToPoint: CGPointMake(505.06, 25.84)];
                [bluetoothPath addLineToPoint: CGPointMake(502, 29)];
                [bluetoothPath addLineToPoint: CGPointMake(502, 23)];
                [bluetoothPath addLineToPoint: CGPointMake(505.06, 25.84)];
                [bluetoothPath closePath];
                [bluetoothPath moveToPoint: CGPointMake(502, 40)];
                [bluetoothPath addLineToPoint: CGPointMake(502, 34)];
                [bluetoothPath addLineToPoint: CGPointMake(505.14, 37.23)];
                [bluetoothPath addLineToPoint: CGPointMake(502, 40)];
                [bluetoothPath closePath];
                [bluetoothColor setFill];
                [bluetoothPath fill];
                
                
                CGContextEndTransparencyLayer(context);
                CGContextRestoreGState(context);
            }
            
            
            //// Graphic 4:21 PM Drawing
            CGRect graphic421PMRect = CGRectMake(220.15, 16, 195, 30);
            UIFont* graphic421PMFont = [UIFont fontWithName: @"HelveticaNeue-Medium" size: 25];
            [color421PMColor setFill];
            [@"4:21 PM" drawInRect: graphic421PMRect withFont: graphic421PMFont lineBreakMode: NSLineBreakByWordWrapping alignment: NSTextAlignmentCenter];
            
            
            //// Signal & Carrier
            {
                //// wifi Drawing
                UIBezierPath* wifiPath = UIBezierPath.bezierPath;
                [wifiPath moveToPoint: CGPointMake(165.47, 25)];
                [wifiPath addCurveToPoint: CGPointMake(175.6, 28.83) controlPoint1: CGPointMake(169.35, 25) controlPoint2: CGPointMake(172.89, 26.45)];
                [wifiPath addLineToPoint: CGPointMake(177.48, 26.72)];
                [wifiPath addCurveToPoint: CGPointMake(165.47, 21.92) controlPoint1: CGPointMake(174.27, 23.89) controlPoint2: CGPointMake(170.07, 21.92)];
                [wifiPath addCurveToPoint: CGPointMake(153.47, 26.7) controlPoint1: CGPointMake(160.87, 21.92) controlPoint2: CGPointMake(156.68, 23.89)];
                [wifiPath addLineToPoint: CGPointMake(155.35, 28.81)];
                [wifiPath addCurveToPoint: CGPointMake(165.47, 25) controlPoint1: CGPointMake(158.06, 26.44) controlPoint2: CGPointMake(161.59, 25)];
                [wifiPath closePath];
                [wifiPath moveToPoint: CGPointMake(165.47, 31.08)];
                [wifiPath addCurveToPoint: CGPointMake(171.56, 33.35) controlPoint1: CGPointMake(167.79, 31.08) controlPoint2: CGPointMake(169.92, 31.94)];
                [wifiPath addLineToPoint: CGPointMake(173.55, 31.12)];
                [wifiPath addCurveToPoint: CGPointMake(165.47, 28) controlPoint1: CGPointMake(171.38, 29.23) controlPoint2: CGPointMake(168.56, 28)];
                [wifiPath addCurveToPoint: CGPointMake(157.39, 31.11) controlPoint1: CGPointMake(162.38, 28) controlPoint2: CGPointMake(159.56, 29.23)];
                [wifiPath addLineToPoint: CGPointMake(159.38, 33.34)];
                [wifiPath addCurveToPoint: CGPointMake(165.47, 31.08) controlPoint1: CGPointMake(161.02, 31.94) controlPoint2: CGPointMake(163.14, 31.08)];
                [wifiPath closePath];
                [wifiPath moveToPoint: CGPointMake(169.56, 35.58)];
                [wifiPath addCurveToPoint: CGPointMake(165.47, 34) controlPoint1: CGPointMake(168.46, 34.65) controlPoint2: CGPointMake(167.03, 34)];
                [wifiPath addCurveToPoint: CGPointMake(161.37, 35.57) controlPoint1: CGPointMake(163.91, 34) controlPoint2: CGPointMake(162.48, 34.64)];
                [wifiPath addLineToPoint: CGPointMake(165.47, 40.17)];
                [wifiPath addLineToPoint: CGPointMake(169.56, 35.58)];
                [wifiPath closePath];
                [wifiColor setFill];
                [wifiPath fill];
                
                
                //// BELL Drawing
                CGRect bELLRect = CGRectMake(88.21, 18, 156, 28);
                UIFont* bELLFont = [UIFont fontWithName: @"HelveticaNeue" size: 23];
                [bELLColor setFill];
                [@"BELL" drawInRect: bELLRect withFont: bELLFont lineBreakMode: NSLineBreakByWordWrapping alignment: NSTextAlignmentLeft];
                
                
                //// Ellipse 1 Drawing
                UIBezierPath* ellipse1Path = UIBezierPath.bezierPath;
                [ellipse1Path moveToPoint: CGPointMake(17.5, 26)];
                [ellipse1Path addCurveToPoint: CGPointMake(23, 31.5) controlPoint1: CGPointMake(20.54, 26) controlPoint2: CGPointMake(23, 28.46)];
                [ellipse1Path addCurveToPoint: CGPointMake(17.5, 37) controlPoint1: CGPointMake(23, 34.54) controlPoint2: CGPointMake(20.54, 37)];
                [ellipse1Path addCurveToPoint: CGPointMake(12, 31.5) controlPoint1: CGPointMake(14.46, 37) controlPoint2: CGPointMake(12, 34.54)];
                [ellipse1Path addCurveToPoint: CGPointMake(17.5, 26) controlPoint1: CGPointMake(12, 28.46) controlPoint2: CGPointMake(14.46, 26)];
                [ellipse1Path closePath];
                [ellipse1Color setFill];
                [ellipse1Path fill];
                
                
                //// Ellipse Drawing
                UIBezierPath* ellipsePath = UIBezierPath.bezierPath;
                [ellipsePath moveToPoint: CGPointMake(31.5, 26)];
                [ellipsePath addCurveToPoint: CGPointMake(37, 31.5) controlPoint1: CGPointMake(34.54, 26) controlPoint2: CGPointMake(37, 28.46)];
                [ellipsePath addCurveToPoint: CGPointMake(31.5, 37) controlPoint1: CGPointMake(37, 34.54) controlPoint2: CGPointMake(34.54, 37)];
                [ellipsePath addCurveToPoint: CGPointMake(26, 31.5) controlPoint1: CGPointMake(28.46, 37) controlPoint2: CGPointMake(26, 34.54)];
                [ellipsePath addCurveToPoint: CGPointMake(31.5, 26) controlPoint1: CGPointMake(26, 28.46) controlPoint2: CGPointMake(28.46, 26)];
                [ellipsePath closePath];
                [ellipse1Color setFill];
                [ellipsePath fill];
                
                
                //// Ellipse 2 Drawing
                UIBezierPath* ellipse2Path = UIBezierPath.bezierPath;
                [ellipse2Path moveToPoint: CGPointMake(45.5, 26)];
                [ellipse2Path addCurveToPoint: CGPointMake(51, 31.5) controlPoint1: CGPointMake(48.54, 26) controlPoint2: CGPointMake(51, 28.46)];
                [ellipse2Path addCurveToPoint: CGPointMake(45.5, 37) controlPoint1: CGPointMake(51, 34.54) controlPoint2: CGPointMake(48.54, 37)];
                [ellipse2Path addCurveToPoint: CGPointMake(40, 31.5) controlPoint1: CGPointMake(42.46, 37) controlPoint2: CGPointMake(40, 34.54)];
                [ellipse2Path addCurveToPoint: CGPointMake(45.5, 26) controlPoint1: CGPointMake(40, 28.46) controlPoint2: CGPointMake(42.46, 26)];
                [ellipse2Path closePath];
                [ellipse1Color setFill];
                [ellipse2Path fill];
                
                
                //// Ellipse 3 Drawing
                UIBezierPath* ellipse3Path = [UIBezierPath bezierPathWithRect: CGRectMake(54, 26, 11, 11)];
                CGContextSaveGState(context);
                [ellipse3Path addClip];
                CGContextScaleCTM(context, 1.0, -1.0);
                CGContextDrawTiledImage(context, CGRectMake(54, -26, ellipse1Image.size.width, ellipse1Image.size.height), ellipse1Image.CGImage);
                CGContextRestoreGState(context);
                
                
                //// Ellipse 4 Drawing
                UIBezierPath* ellipse4Path = [UIBezierPath bezierPathWithRect: CGRectMake(68, 26, 11, 11)];
                CGContextSaveGState(context);
                [ellipse4Path addClip];
                CGContextScaleCTM(context, 1.0, -1.0);
                CGContextDrawTiledImage(context, CGRectMake(68, -26, ellipse1Image2.size.width, ellipse1Image2.size.height), ellipse1Image2.CGImage);
                CGContextRestoreGState(context);
            }
        }
    }
    
    
    //// Cleanup
    CGGradientRelease(buttonGradient);
    CGGradientRelease(defaultGradientVioletOrangeVioletOrange);
    CGGradientRelease(custom);
    CGColorSpaceRelease(colorSpace);
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
