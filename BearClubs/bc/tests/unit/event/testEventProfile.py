from django.test import TestCase
from BearClubs.bc.forms import AddEventForm
from BearClubs.bc.models import User, Organization, OrganizationType, Event, UserToOrganization
from django.utils import timezone
import datetime

from django.utils import unittest
from django.utils.unittest import TestLoader, TextTestRunner
from cStringIO import StringIO

from django.test import Client

class EventProfileUnitTests(TestCase):

    def setUp(self):
        bus_org_type = OrganizationType.objects.get(name='Business');
        cs_org_type = OrganizationType.objects.get(name='Computer Science');

        User(username='test', password='1234', email='test@test.com').save();
        Organization(name="Test Club", description="Club Description", contact_email="test@test.com", organization_type=bus_org_type).save();

        self.user = User.objects.get(username='test');
        self.club = Organization.objects.get(name="Test Club");

        UserToOrganization(user=self.user, organization=self.club, admin=True).save();

    def testEventAdmin(self):
        startTime = '9/24/2040 5:03:29 PM'
        endTime = '9/24/2050 5:03:29 PM'

        form_data = {
            'name': 'Test Event',
            'description': 'Event Description',
            'organization': self.club.id,
            'contact_email': 'test@test.com',
            'start_time': str(startTime),
            'end_time': str(endTime),
            'location': 'Berkeley',
        };

        form = AddEventForm(self.user, form_data);
        self.assertTrue(form.is_valid(), form.errors.as_text);
        form.save();

        test_event = Event.objects.get(name="Test Event");
        test_user_to_organization = UserToOrganization.objects.get(user=self.user);

        self.assertTrue(test_user_to_organization.organization == self.club);
        self.assertTrue(test_user_to_organization.admin == True);

    def testEventNotAdmin(self):
        test_user_to_organization = UserToOrganization.objects.get(user=self.user);
        test_user_to_organization.delete();

        startTime = '9/24/2040 5:03:29 PM'
        endTime = '9/24/2050 5:03:29 PM'

        form_data = {
            'name': 'Test Event',
            'description': 'Event Description',
            'organization': self.club.id,
            'contact_email': 'test@test.com',
            'start_time': str(startTime),
            'end_time': str(endTime),
            'location': 'Berkeley',
        };

        form = AddEventForm(self.user, form_data);
        self.assertFalse(form.is_valid(), form.errors.as_text);  

# If this file is invoked as a Python script, run the tests in this module
if __name__ == "__main__":
    # Add a verbose argument
    sys.argv = [sys.argv[0]] + ["-v"] + sys.argv[1:]
    unittest.main()