from cStringIO import StringIO
import re

from django.db import IntegrityError
from django.test import TestCase, Client
from django.utils import unittest, timezone
import datetime

from BearClubs.bc.models import Event, Organization, OrganizationType, User, UserToEvent, UserToOrganization

class EventProfileTests(TestCase):

    client = Client();

    def setUp(self):
    	self.baseURL = 'http://localhost:8000';

        self.user = User(username='test', password='1234', email='test@test.com');
        self.user.set_password('1234');
        self.user.save();

        self.org1 = Organization(name='test org 1', contact_email='test1@test.com', organization_type=OrganizationType.objects.get(id=1));
        self.org1.save();

        self.event = Event(name="test event", description="event description", organization=self.org1, contact_email="test@test.com", start_time=timezone.now(), end_time=timezone.now(), location="Berkeley");
        self.event.save();

    def testViewEventNotLoggedIn(self):
        """
        Tests that we can view the details of a valid event when not logged in
        """
        response = self.client.get(self.baseURL + '/events/' + str(self.event.id));

        self.assertTrue(self.event.name in response.content);
        self.assertTrue(self.event.description in response.content);
        self.assertTrue(self.event.organization.name in response.content);
        self.assertTrue(self.event.contact_email in response.content);
        self.assertTrue(self.event.location in response.content);

    def testViewEventLoggedIn(self):
        """
        Tests that we can view the details of a valid event when logged in
        """
        self.client.login(username='test', password='1234');

        response = self.client.get(self.baseURL + '/events/' + str(self.event.id));

        self.assertTrue(self.event.name in response.content);
        self.assertTrue(self.event.description in response.content);
        self.assertTrue(self.event.organization.name in response.content);
        self.assertTrue(self.event.contact_email in response.content);
        self.assertTrue(self.event.location in response.content);

    def tearDown(self):
        self.client.logout();


# If this file is invoked as a Python script, run the tests in this module
if __name__ == "__main__":
    # Add a verbose argument
    sys.argv = [sys.argv[0]] + ["-v"] + sys.argv[1:]
    unittest.main()