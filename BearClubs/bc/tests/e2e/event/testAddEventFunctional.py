from django.test import TestCase, Client
from BearClubs.bc.forms import AddEventForm
from BearClubs.bc.models import User, Organization, OrganizationType, Event, UserToOrganization
from django.utils import timezone
import datetime

from django.utils import unittest
from django.utils.unittest import TestLoader, TextTestRunner
from cStringIO import StringIO

from django.test import Client

class AddEventFunctionalTests(TestCase):

	# Test cases:
    # -- Valid Event: succeed
    # -- Valid Event, no description: succeed
    # -- Valid Event, no location: succeed
    # -- Valid Event, name = 128 chars: succeed
    # -- Valid Event, email = 128 chars: succeed

    def setUp(self):
        bus_org_type = OrganizationType.objects.get(name='Business');
        cs_org_type = OrganizationType.objects.get(name='Computer Science');

        self.baseURL = 'http://localhost:8000';

        self.user = User(username='test', password='1234', email='test@test.com');
        self.user.set_password('1234');
        self.user.save();


    	self.c = Client();


        Organization(name="Test Club", description="Club Description", contact_email="test@test.com", organization_type=bus_org_type).save();
        self.club = Organization.objects.get(name="Test Club");

        self.uto = UserToOrganization(user=self.user, organization=self.club, admin=True).save();
        self.c.login(username='test', password='1234');

    def tearDown(self):
        self.c.logout();

    def testValidEvent1(self):
        startTime = '9/24/2040 5:03:29 PM'
        endTime = '9/24/2050 5:03:29 PM'

        form_data = {
            'name': 'Test Event',
            'description': 'Event Description',
            'organization': 1,
            'contact_email': 'test@test.com',
            'start_time': str(startTime),
            'end_time': str(endTime),
            'location': 'Berkeley',
        };

        response = self.c.post(self.baseURL+'/events/new', form_data);
        
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

        response = self.c.post(self.baseURL+'/events/new', form_data);

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

        response = self.c.post(self.baseURL+'/events/new', form_data);

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

        response = self.c.post(self.baseURL+'/events/new', form_data);

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

        response = self.c.post(self.baseURL+'/events/new', form_data);

        test_event = Event.objects.get(name="Test Event");

        self.assertTrue(test_event.name == 'Test Event');
        self.assertTrue(test_event.description == 'Event Description');
        self.assertTrue(test_event.contact_email == email_128);

        









