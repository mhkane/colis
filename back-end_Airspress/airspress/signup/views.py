from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from authomatic import Authomatic
from authomatic.adapters import DjangoAdapter
from schemes import User
from airspress.settings import CONFIG
from django.http.request import HttpRequest

authomatic = Authomatic(CONFIG, 'a super secret random string about falconpress and his brethren')

def home(request):
    # Create links and OpenID form to the Login handler.
    return render(request, 'signup/index.html')

def login(request, provider_name):
    # We we need the response object for the adapter.
    response = HttpResponse()
    
    # Start the login procedure.
    result = authomatic.login(DjangoAdapter(request, response), provider_name)
     
    # If there is no result, the login procedure is still pending.
    # Don't write anything to the response if there is no result!
    if result:
        # If there is result, the login procedure is over and we can write to response.
        #response.write('<a href="..">Home</a>')
        
        if result.error:
            # Login procedure finished with an error.
            response.write('<h2>Damn that error: {0}</h2>'.format(result.error.message))
        elif result.user:
            
            # OAuth 2.0 and OAuth 1.0a provide only limited user data on login,
            # We need to update the user to get more info.
            if not (result.user.name and result.user.id):
                result.user.update()
            
            # Recover information for Parse authData
            #response.write(u'{0}'.format(result.user.name))
            fbID = result.user.id
            # response.write(u'<h2>Your email is: {0}</h2>'.format(result.user.email))
            
            # Seems like we're done, but there's more we can do...
            if result.user.credentials:
                if result.provider.name == 'fb':
                    #serialized_credentials = result.user.credentials.serialize()
                    credentials = authomatic.credentials(result.user.credentials)
                    valid = credentials.valid
                    expiration_date = credentials.expiration_date
                    access_token = credentials.token
                    if valid:
                        authData = {"facebook": {"id": fbID, "access_token": access_token,
                         "expiration_date": expiration_date}}
                        account = User.login_auth(authData)
                        return render(request,'signup/index.html',{'greetings':u'{0}'.format(result.user.name)})
                else:
                    pass
    
    return response           
            # If there are credentials (only by AuthorizationProvider),
            # we can _access user's protected res