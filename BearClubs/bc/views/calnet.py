import urllib2
from xml.dom import minidom

from django.conf import settings
from django.contrib import auth
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect

from BearClubs.bc.models import User

def calnet_login(request, testData=None):
    # check if logged in
    if request.user.is_authenticated():
        return redirect('/user');

    # if not, go through the CAS workflow
    else:

        # if we get a ticket back, verify that ticket
        if request.GET.get('ticket'):
            try:
                # Compile a URL for CAS login
                url = settings.CALNET_VALIDATE + '&ticket=' + request.GET.get('ticket');

                result = '';

                # Dependency injection
                if testData:
                    result = testData;
                else:
                    result = urllib2.urlopen(url);

                # Parse the result
                xmlData = minidom.parse(result);

                # If the XML response has the <cas:user /> element...
                if xmlData.getElementsByTagName('cas:user'):

                    # Get the user ID and login or register it
                    userID = xmlData.getElementsByTagName('cas:user')[0].firstChild.nodeValue;

                    try:
                        User.loginOrRegister(request, userID);
                    except:
                        print("USER MODEL LOGIN/REGISTER ERROR");
                        return redirect('/error');

                    # There was a failure...
                    if not request.user.is_authenticated():
                        print("USER ISN'T AUTHENTICATED AFTER USER MODEL WORKFLOW");
                        return redirect('/error');

            # Catch XML parsing errors
            except:
                print("XML PARSE ERROR");
                return redirect('/error');

            return redirect('/user');

        # if not, send the user to CAS login
        else:
            return redirect(settings.CALNET_TICKET_AUTH);

def calnet_logout(request):
    auth.logout(request);
    return redirect(settings.CALNET_LOGOUT);

