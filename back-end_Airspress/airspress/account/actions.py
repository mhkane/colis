'''
Relevant models (not Django db-backed models) to handle
user actions : put request on a travel, add a trip, make payments
and also edit profile information
'''
from signup.schemes import User
from parse_rest.datatypes import Object as ParseObject
class request(ParseObject):
    pass
class acceptedRequest(ParseObject):
    pass
def getdeal(travelUser, aRequest, aTrip):
    reqAccepted = {}
    try:
        reqWeight = aRequest.weightRequested
        reqUser = aRequest.Requester
        travelName = travelUser.username
        travelEmail = travelUser.email
        #priceDeal = aRequest.priceUsd
        pub_date = aRequest.createdAt
        departDate = aTrip.departureDate.date()
        destLocation = aTrip.toLocation
        oriLocation = aTrip.fromLocation
        reqAccepted = {'pubdate':pub_date, 
             'depDate':departDate, 'cityDep':destLocation, 
             'cityArr':oriLocation,'requestWeight':reqWeight, 
             'traveler':travelName, 'travelerEmail':travelEmail, 'reqUser':reqUser.username, 'reqEmail':reqUser.email}
    except AttributeError:
        pass
    reqAccepted['ispayed']= aRequest.paymentStatus or False
    reqAccepted['isdeliv']= aRequest.deliveryStatus or False
    '''
    
                            # send notification
                        travelName = travelUser.username
                        travelEmail = travelUser.email
                        #priceDeal = aRequest.priceUsd
                        pub_date = aRequest.createdAt
                        departDate = aTrip.departureDate.date()
                        destLocation = aTrip.toLocation
                        oriLocation = aTrip.fromLocation
                        reqAccepted = {'pubdate':pub_date, 
                             'depDate':departDate, 'cityDep':destLocation, 
                             'cityArr':oriLocation,'requestWeight':reqWeight, 
                             'traveler':travelName, 'travelerEmail':travelEmail, 'reqUser':reqUser.username, 'reqEmail':reqUser.email}
                    except AttributeError:
                        pass
    '''
    return reqAccepted