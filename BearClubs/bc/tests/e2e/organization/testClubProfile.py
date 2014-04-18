from cStringIO import StringIO
import re

from django.db import IntegrityError
from django.test import TestCase, Client
from django.utils import unittest, timezone

from BearClubs.bc.models import Event, Organization, OrganizationType, User, UserToEvent, UserToOrganization

class clubProfileTests(TestCase):

    client = Client();

    def setUp(self):
        self.baseURL = 'http://localhost:8000';

        self.user = User(username='test', password='1234', email='test@test.com');
        self.user.set_password('1234');
        self.user.save();

        self.user2 = User(username='test2', password='1234', email='test@test.com');
        self.user2.set_password('1234');
        self.user2.save();

        self.user3 = User(username='test3', password='1234', email='test@test.com');
        self.user3.set_password('1234');
        self.user3.save();

        self.org1 = Organization(name='test org 1', contact_email='test1@test.com', organization_type=OrganizationType.objects.get(id=1));
        self.org2 = Organization(name='test org 2', contact_email='test2@test.com', organization_type=OrganizationType.objects.get(id=2));
        self.org3 = Organization(name='test org 3', contact_email='test3@test.com', organization_type=OrganizationType.objects.get(id=1));
        
        self.org1.save();
        self.org2.save();
        self.org3.save();


        self.uto1 = UserToOrganization(user=self.user, organization=self.org1).save();
        self.uto2 = UserToOrganization(user=self.user2, organization=self.org1, admin=True).save();

    def testViewClubNotLoggedIn(self):
    	response = self.client.get(self.baseURL + '/clubs/1');

    	self.assertTrue(self.org1.name in response.content);
        self.assertTrue(self.org1.contact_email in response.content);
        self.assertTrue(self.org1.organization_type.name in response.content);
        self.assertFalse("Join Club" in response.content);
        self.assertFalse("Manage" in response.content);

    def testViewClubLoggedInNotMember(self):
        self.client.login(username='test3', password='1234');

        response = self.client.get(self.baseURL + '/clubs/1');

        self.assertTrue(self.org1.name in response.content);
        self.assertTrue(self.org1.contact_email in response.content);
        self.assertTrue(self.org1.organization_type.name in response.content);
        self.assertTrue("Join Club" in response.content);
        self.assertFalse("Manage" in response.content);

    def testViewClubLoggedInMember(self):
        self.client.login(username='test', password='1234');

        response = self.client.get(self.baseURL + '/clubs/1');

        self.assertTrue(self.org1.name in response.content);
        self.assertTrue(self.org1.contact_email in response.content);
        self.assertTrue(self.org1.organization_type.name in response.content);
        self.assertTrue("You are a member of this club." in response.content);
        self.assertFalse("Manage" in response.content);

    def testViewClubLoggedInAdmin(self):
        self.client.login(username='test2', password='1234');

        response = self.client.get(self.baseURL + '/clubs/1');

        self.assertTrue(self.org1.name in response.content);
        self.assertTrue(self.org1.contact_email in response.content);
        self.assertTrue(self.org1.organization_type.name in response.content);
        self.assertTrue("You are a member and admin of this club." in response.content);
        self.assertTrue("Manage" in response.content);

    def tearDown(self):
        self.client.logout();

if __name__ == "__main__":
    # Add a verbose argument
    sys.argv = [sys.argv[0]] + ["-v"] + sys.argv[1:]
    unittest.main()