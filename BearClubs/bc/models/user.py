import hashlib
import re
import urllib2
from xml.dom import minidom

from django.conf import settings
from django.contrib import auth
from django.core.exceptions import ObjectDoesNotExist
from django.core.urlresolvers import reverse
from django.db import models 

class User(auth.models.User):
    # Following fields inherited from auth.models.User
    # ------------------------------------------------
    # username     = models.CharField(max_length=128, unique=True);
    # password     = models.CharField(max_length=128, unique=True);
    # email        = models.EmailField(max_length=128, unique=True);
    # first_name   = models.CharField(max_length=64);
    # last_name    = models.CharField(max_length=64);

    calNetID = models.IntegerField(null=True, blank=True);

    def __unicode__(self):
        return 'User: %s' % (self.username)

    @staticmethod
    def loginOrRegister(request, calNetID):
        user = {};

        try:
            user = User.objects.get(calNetID=calNetID);
        except ObjectDoesNotExist:
            user = User.registerCalNet(calNetID);

        if user:
            user.backend = 'django.contrib.auth.backends.ModelBackend';
            auth.login(request, user);

    @staticmethod
    def registerCalNet(calNetID, testData=None):

        bMailUsername   = "";
        firstName       = "";
        lastName        = "";
        bMail           = "";
        hashWord        = "";

        url = settings.BERKELEY_PERSON_API + str(calNetID);

        # Get and parse data from Berkeley API
        try:
            # Dependency injection
            if testData:
                result = testData;
            else:
                result = urllib2.urlopen(url);

            # Parse the result
            xmlData = minidom.parse(result);
            print(xmlData.toxml());

            # Check for multiple first names
            if xmlData.getElementsByTagName('givenname0'):
                if xmlData.getElementsByTagName('givenname0')[0].firstChild:
                    firstName = xmlData.getElementsByTagName('givenname0')[0].firstChild.nodeValue;
            elif xmlData.getElementsByTagName('givenname'):
                if xmlData.getElementsByTagName('givenname')[0].firstChild:
                    firstName = xmlData.getElementsByTagName('givenname')[0].firstChild.nodeValue;

            # Get rid of spaces
            if " " in firstName:
                firstName = re.match(r'(.*)\s.*', firstName).group(1);

            print("FIRST NAME: " + firstName);

            # Check for multiple last names
            if xmlData.getElementsByTagName('sn0'):
                if xmlData.getElementsByTagName('sn0')[0].firstChild:
                    lastName = xmlData.getElementsByTagName('sn0')[0].firstChild.nodeValue;
            elif xmlData.getElementsByTagName('sn'):
                if xmlData.getElementsByTagName('sn')[0].firstChild:
                    lastName = xmlData.getElementsByTagName('sn')[0].firstChild.nodeValue;

            print("LAST NAME: " + lastName);

            print("GETTING EMAIL");

            # Check for multiple email addresses
            if xmlData.getElementsByTagName('mail0'):
                if xmlData.getElementsByTagName('mail0')[0].firstChild:
                    bMail = xmlData.getElementsByTagName('mail0')[0].firstChild.nodeValue;
            elif xmlData.getElementsByTagName('mail'):
                if xmlData.getElementsByTagName('mail')[0].firstChild:
                    bMail = xmlData.getElementsByTagName('mail')[0].firstChild.nodeValue;
            
            # NO EMAIL; FERPA forbids us from releasing/guessing the email
            # Just make it unique for now
            if not bMail:
                bMail = "no_email_on_file" + calNetID + "@berkeley.edu";

            print("BMAIL: " + bMail);

            # Get username from bMail address
            bMailUsername = re.match(r'(.*)@.*\.?berkeley\.edu$', bMail).group(1);

            print("BMAIL USER: " + bMailUsername);

        # Exception? Return null and the view will handle the error
        except:
            print("XML PARSING ERROR IN USER MODEL");
            return;

        m = hashlib.sha256();
        m.update(firstName);
        m.update(lastName);
        m.update(bMail);

        hashWord = m.hexdigest();

        try:
            user = User.objects.create_user(
                username=bMailUsername,
                email=bMail,
                password=hashWord,
                calNetID=calNetID
            );
        except:
            print("USER OBJECTS CREATE ERROR");
            return;

        user.first_name = firstName;
        user.last_name = lastName;
        user.save();

        return user;

    def get_absolute_url(self):
        return reverse('profile', args=[self.id])

    class Meta:
        app_label = 'bc';
