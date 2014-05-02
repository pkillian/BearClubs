import urllib2
from xml.dom import minidom

from django.conf import settings
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect

def calnet(request):
    # check if logged in
    if request.user.is_authenticated():
        return redirect('/user');

    # if not, go through the CAS workflow
    else:
        # if we get a ticket back, verify that ticket
        if request.GET.get('ticket'):
            try:
                url = settings.CALNET_VALIDATE + '&ticket=' + request.GET.get('ticket');
                
                result = urllib2.urlopen(url);
                xmlData = minidom.parse(result);

                if xmlData:
                    print(xmlData);

                if xmlData.getElementsByTagName('cas:user'):
                    print(xmlData.getElementsByTagName('cas:user')[0].firstChild.nodeValue);

            except:
                return HttpResponse("error")

            return redirect('/user');

        # if not, send the user to CAS login
        else:
            return redirect(settings.CALNET_TICKET_AUTH);
