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
    # -- Valid Event: succeed
    # -- Valid Event, no description: succeed
    # -- Valid Event, no location: succeed
    # -- Valid Event, name = 128 chars: succeed
    # -- Valid Event, email = 128 chars: succeed
    # -- No name: failure
    # -- Name > 128 chars: failure
    # -- No email: failure
    # -- Email > 128 chars: failure
    # -- No Org id: failure
    # -- start_time > end_time : failure
    # -- start_time & end_time in past: failure
    # -- start_time in past: failure
    # -- start_time invalid format: failure

    def setUp(self):
        bus_org_type = OrganizationType.objects.get(name='Business');
        cs_org_type = OrganizationType.objects.get(name='Computer Science');

        User(username='test', password='1234', email='test@test.com').save();
        Organization(name="Test Club", description="Club Description", contact_email="test@test.com", organization_type=bus_org_type).save();
        self.user = User.objects.get(username='test');
        self.club = Organization.objects.get(name="Test Club");

    def testValidEvent1(self):
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

        self.assertTrue(test_event.name == 'Test Event');
        self.assertTrue(test_event.description == 'Event Description');
        self.assertTrue(test_event.contact_email == 'test@test.com');
        self.assertTrue(test_event.location == 'Berkeley');

    def testValidEvent2(self):
        startTime = '9/24/2040 5:03:29 PM'
        endTime = '9/24/2050 5:03:29 PM'

        form_data = {
            'name': 'Test Event',
            'contact_email': 'test@test.com',
            'start_time': str(startTime),
            'end_time': str(endTime),
            'organization': self.club.id,
            'location': 'Berkeley'
        };

        form = AddEventForm(self.user, form_data);
        self.assertTrue(form.is_valid(), form.errors);
        form.save();

        test_event = Event.objects.get(name="Test Event");

        self.assertTrue(test_event.name == 'Test Event');
        self.assertTrue(test_event.location == 'Berkeley');
        self.assertTrue(test_event.contact_email == 'test@test.com');

    def testValidEvent3(self):
        startTime = '9/24/2040 5:03:29 PM'
        endTime = '9/24/2050 5:03:29 PM'

        form_data = {
            'name': 'Test Event',
            'description': 'Event Description',
            'contact_email': 'test@test.com',
            'start_time': str(startTime),
            'end_time': str(endTime),
            'organization': self.club.id,
        };

        form = AddEventForm(self.user, form_data);
        self.assertTrue(form.is_valid(), form.errors);
        form.save();

        test_event = Event.objects.get(name="Test Event");

        self.assertTrue(test_event.name == 'Test Event');
        self.assertTrue(test_event.description == 'Event Description');
        self.assertTrue(test_event.contact_email == 'test@test.com');

    def testValidEvent4(self):
        startTime = '9/24/2040 5:03:29 PM'
        endTime = '9/24/2050 5:03:29 PM'

        form_data = {
            'name': 'a'*128,
            'description': 'Event Description',
            'contact_email': 'test@test.com',
            'start_time': str(startTime),
            'end_time': str(endTime),
            'organization': self.club.id,
        };

        form = AddEventForm(self.user, form_data);
        self.assertTrue(form.is_valid(), form.errors);
        form.save();

        test_event = Event.objects.get(name="a"*128);

        self.assertTrue(test_event.name == 'a'*128);
        self.assertTrue(test_event.description == 'Event Description');
        self.assertTrue(test_event.contact_email == 'test@test.com');

    def testValidEvent5(self):
        startTime = '9/24/2040 5:03:29 PM'
        endTime = '9/24/2050 5:03:29 PM'

        email_128 = ("a"*119) + "@test.com";

        self.assertTrue(len(email_128) == 128);

        form_data = {
            'name': 'Test Event',
            'description': 'Event Description',
            'contact_email': email_128,
            'start_time': str(startTime),
            'end_time': str(endTime),
            'organization': self.club.id,
        };

        form = AddEventForm(self.user, form_data);
        self.assertTrue(form.is_valid(), form.errors);
        form.save();

        test_event = Event.objects.get(name="Test Event");

        self.assertTrue(test_event.name == 'Test Event');
        self.assertTrue(test_event.description == 'Event Description');
        self.assertTrue(test_event.contact_email == email_128);

    def testNoNameEvent(self):
        startTime = '9/24/2040 5:03:29 PM'
        endTime = '9/24/2050 5:03:29 PM'

        form_data = {
            'name': '',
            'description': 'Event Description',
            'organization': self.club.id,
            'contact_email': 'test@test.com',
            'start_time': str(startTime),
            'end_time': str(endTime),
            'location': 'Berkeley',
        };

        form = AddEventForm(self.user, form_data);
        self.assertFalse(form.is_valid());

    def testNameTooLongEvent(self):
        startTime = '9/24/2040 5:03:29 PM'
        endTime = '9/24/2050 5:03:29 PM'

        form_data = {
            'name': 'a'*129,
            'description': 'Event Description',
            'contact_email': 'test@test.com',
            'start_time': str(startTime),
            'end_time': str(endTime),
            'organization': self.club.id,
        };

        form = AddEventForm(self.user, form_data);
        self.assertFalse(form.is_valid());

    def testNoEmailEvent(self):
        startTime = '9/24/2040 5:03:29 PM'
        endTime = '9/24/2050 5:03:29 PM'

        form_data = {
            'name': 'Test Event',
            'description': 'Event Description',
            'organization': self.club.id,
            'start_time': str(startTime),
            'end_time': str(endTime),
            'location': 'Berkeley',
        };

        form = AddEventForm(self.user, form_data);
        self.assertFalse(form.is_valid());

    def testEmailTooLongEvent(self):
        startTime = '9/24/2040 5:03:29 PM'
        endTime = '9/24/2050 5:03:29 PM'

        email = ("a"*120) + "@test.com";

        form_data = {
            'name': '',
            'description': 'Event Description',
            'organization': self.club.id,
            'contact_email': email,
            'start_time': str(startTime),
            'end_time': str(endTime),
            'location': 'Berkeley',
        };

        form = AddEventForm(self.user, form_data);
        self.assertFalse(form.is_valid());

    def testNoOrganizationEvent(self):
        startTime = '9/24/2040 5:03:29 PM'
        endTime = '9/24/2050 5:03:29 PM'

        form_data = {
            'name': 'Test Event',
            'description': 'Event Description',
            'contact_email': 'test@test.com',
            'start_time': str(startTime),
            'end_time': str(endTime),
            'location': 'Berkeley',
        };

        form = AddEventForm(self.user, form_data);
        self.assertFalse(form.is_valid());

    def testStartTimeGreaterThanEndTimeEvent(self):
        startTime = '9/24/2060 5:03:29 PM'
        endTime = '9/24/2050 5:03:29 PM'

        form_data = {
            'name': 'Test Event',
            'description': 'Event Description',
            'contact_email': 'test@test.com',
            'start_time': str(startTime),
            'end_time': str(endTime),
            'location': 'Berkeley',
        };

        form = AddEventForm(self.user, form_data);
        self.assertFalse(form.is_valid());
     
    def testStartTimeAndEndTimeInPastEvent(self):
        startTime = '9/24/2010 5:03:29 PM'
        endTime = '9/24/2011 5:03:29 PM'

        form_data = {
            'name': 'Test Event',
            'description': 'Event Description',
            'contact_email': 'test@test.com',
            'start_time': str(startTime),
            'end_time': str(endTime),
            'location': 'Berkeley',
        };

        form = AddEventForm(self.user, form_data);
        self.assertFalse(form.is_valid());

    def testStartTimeInPastEvent(self):
        startTime = '9/24/2010 5:03:29 PM'
        endTime = '9/24/2044 5:03:29 PM'

        form_data = {
            'name': 'Test Event',
            'description': 'Event Description',
            'contact_email': 'test@test.com',
            'start_time': str(startTime),
            'end_time': str(endTime),
            'location': 'Berkeley',
        };

        form = AddEventForm(self.user, form_data);
        self.assertFalse(form.is_valid());

    def testInvalidDateFormatEvent(self):
        startTime = '9/24/2010 5:03'
        endTime = '9/24/2044 5:03:29 PM'

        form_data = {
            'name': 'Test Event',
            'description': 'Event Description',
            'contact_email': 'test@test.com',
            'start_time': str(startTime),
            'end_time': str(endTime),
            'location': 'Berkeley',
        };

        form = AddEventForm(self.user, form_data);
        self.assertFalse(form.is_valid());


# If this file is invoked as a Python script, run the tests in this module
if __name__ == "__main__":
    # Add a verbose argument
    sys.argv = [sys.argv[0]] + ["-v"] + sys.argv[1:]
    unittest.main()
