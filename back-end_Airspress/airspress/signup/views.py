from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from authomatic import Authomatic
from authomatic.adapters import DjangoAdapter
from schemes import User, currentUser
from airspress.settings import CONFIG

authomatic = Authomatic(CONFIG, 'a super secret random string about falconpress and his brethren')

def home(request):
    # Create links and OpenID form and forward to the Login handler.
    # Recover data from sessions
    cUser=None
    try:
        saken = request.session['lsten']
        cUser = currentUser(saken)
    except KeyError:
        return render(request, 'signup/index.html')
    
    if cUser is not None:
        objID = cUser['objectId']
        username = cUser['username']
        if objID:
            return render(request, 'signup/index.html', {'greetings':username})
    return render(request, 'signup/index.html')

def login(request, provider_name):
    # We need the response object for the adapter.
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
                        explodeName = result.user.name.split(' ', 2) #Build username from FB name
                        PUsername = '_'.join(explodeName[:2 if len(explodeName)>2 else 1]) #join 2 first component of exploded name
                        account.username = PUsername
                        account.save()
                        request.session['lsten'] = account.sessionToken
                        return HttpResponseRedirect(reverse('trips:index'))
                else:
                    pass
    
    return response           
            # If there are credentials (only by AuthorizationProvider),
            # we can _access user's protected res
def logout(request):
    try:
        request.session.flush()
    except:
        pass
    return HttpResponseRedirect(reverse('signup:index'))