from cStringIO import StringIO
import re

from django.db import IntegrityError
from django.test import TestCase, Client
from django.utils import unittest, timezone

from BearClubs.bc.models import Event, Organization, OrganizationType, User, UserToEvent, UserToOrganization

class UserDashboardTests(TestCase):

    client = Client();

    def setUp(self):
        self.baseURL = 'http://localhost:8000';

        self.user = User(username='test', password='1234', email='test@test.com');
        self.user.set_password('1234');
        self.user.save();

        self.org1 = Organization(name='test org 1', contact_email='test1@test.com', organization_type=OrganizationType.objects.get(id=1));
        self.org2 = Organization(name='test org 2', contact_email='test2@test.com', organization_type=OrganizationType.objects.get(id=2));
        self.org3 = Organization(name='test org 3', contact_email='test3@test.com', organization_type=OrganizationType.objects.get(id=1));
        
        self.org1.save();
        self.org2.save();
        self.org3.save();

        self.event1 = Event(name='test 1', contact_email='test1@test.com', organization=self.org1, start_time=timezone.now(), end_time=timezone.now());
        self.event2 = Event(name='test 2', contact_email='test2@test.com', organization=self.org2, start_time=timezone.now(), end_time=timezone.now());
        self.event3 = Event(name='test 3', contact_email='test3@test.com', organization=self.org3, start_time=timezone.now(), end_time=timezone.now());

        self.event1.save();
        self.event2.save();
        self.event3.save();

        self.uto1 = UserToOrganization(user=self.user, organization=self.org1);
        self.uto2 = UserToOrganization(user=self.user, organization=self.org2);
        self.uto3 = UserToOrganization(user=self.user, organization=self.org3);

        self.ute1 = UserToEvent(user=self.user, event=self.event1);
        self.ute2 = UserToEvent(user=self.user, event=self.event2);
        self.ute3 = UserToEvent(user=self.user, event=self.event3);

        self.client.login(username='test', password='1234');

    def tearDown(self):
        self.client.logout();

    def testValidDashboard_ShowClubEvents(self):
        self.uto1.save();
        self.uto2.save();
        self.uto3.save();

        response = self.client.get(self.baseURL + '/user');

        self.assertTrue(self.event1.name in response.content);
        self.assertTrue('test 1' in response.content);
        self.assertTrue('test 2' in response.content);
        self.assertTrue('test 3' in response.content);

    def testValidDashboard_ShowSubscribedEvents(self):
        self.ute1.save();
        self.ute2.save();
        self.ute3.save();

        response = self.client.get(self.baseURL + '/user');

        self.assertTrue('test 1' in response.content);
        self.assertTrue('test 2' in response.content);
        self.assertTrue('test 3' in response.content);

    def testValidDashboard_ShowTwoSubscribedEvents(self):
        self.ute1.save();
        self.ute2.save();

        response = self.client.get(self.baseURL + '/user');

        self.assertTrue('test 1' in response.content);
        self.assertTrue('test 2' in response.content);

    def testValidDashboard_ShowOneSubscribedEvents(self):
        self.ute1.save();

        response = self.client.get(self.baseURL + '/user');

        self.assertTrue('test 1' in response.content);


# If this file is invoked as a Python script, run the tests in this module
if __name__ == "__main__":
    # Add a verbose argument
    sys.argv = [sys.argv[0]] + ["-v"] + sys.argv[1:]
    unittest.main()
