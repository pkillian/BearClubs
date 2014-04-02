from django.test import TestCase
from BearClubs.bc.forms import AddEventForm
from BearClubs.bc.models import User, Organization, OrganizationType, Event
from django.utils import timezone
import datetime

from django.utils import unittest
from django.utils.unittest import TestLoader, TextTestRunner
from cStringIO import StringIO

from django.test import Client

class AddEventUnitTests(TestCase):

    # Test cases:
    # -- Valid Club: succeed
    # -- Valid Club, no description: succeed
    # -- Valid Club, name = 128 chars: succeed
    # -- Valid Club, email = 128 chars: succeed
    # -- No name: failure
    # -- Name > 128 chars: failure
    # -- Name not unique: failure
    # -- No email: failure
    # -- Email > 128 chars: failure
    # -- Email not unique: failure
    # -- No OrgType id: failure
    # -- Invalid OrgType id: failure

    def setUp(self):
        bus_org_type = OrganizationType.objects.get(name='Business');
        cs_org_type = OrganizationType.objects.get(name='Computer Science');

        User(username='test', password='1234', email='test@test.com').save();
        Organization(name="Test Club", description="Club Description", contact_email="test@test.com", organization_type=bus_org_type).save();
        self.user = User.objects.get(username='test');
        self.club = Organization.objects.get(name="Test Club");

    def testValidEvent1(self):
        startDate = "2030-10-01 15:26"
        startTime = datetime.datetime.strptime(startDate, "%Y-%m-%d %H:%M")
        endTime = startTime + datetime.timedelta(1);

        form_data = {
            'name': 'Test Event',
            'description': 'Event Description',
            'organization': self.club.id,
            'contact_email': 'test@test.com',
            'start_time': startTime,
            'end_time': endTime,
            'location': 'Berkeley',
        };

        form = AddEventForm(self.user, form_data);
        self.assertTrue(form.is_valid(), form.errors.as_text);
        form.save();

        test_event = Event.objects.get(name="Test Event");

        self.assertTrue(test_event.name == 'Test Event');
        self.assertTrue(test_event.description == 'Event Description');
        self.assertTrue(test_event.contact_email == 'test@test.com');

    def testValidEvent2(self):
        form_data = {
            'name': 'Test Event',
            'contact_email': 'test@test.com',
            'organization': 1
        };

        form = AddEventForm(self.user, form_data);
        self.assertTrue(form.is_valid(), form.errors);
        form.save();

        test_event = Event.objects.get(name="Test Event");

        self.assertTrue(test_event.name == 'Test Event');
        #self.assertTrue(test_event.description == 'Event Description');
        self.assertTrue(test_event.contact_email == 'test@test.com');


# If this file is invoked as a Python script, run the tests in this module
if __name__ == "__main__":
    # Add a verbose argument
    sys.argv = [sys.argv[0]] + ["-v"] + sys.argv[1:]
    unittest.main()
