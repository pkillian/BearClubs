from cStringIO import StringIO
import re

from django.db import IntegrityError
from django.test import TestCase, Client
from django.utils import unittest, timezone

from BearClubs.bc.models import Event, Organization, OrganizationType, User, UserToEvent, UserToOrganization

class UserToEventMappingTests(TestCase):

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


        self.uto1 = UserToOrganization(user=self.user, organization=self.org1);
        self.uto2 = UserToOrganization(user=self.user, organization=self.org2);
        self.uto3 = UserToOrganization(user=self.user, organization=self.org3);

        self.org1 = Organization(name='test org 1', contact_email='test1@test.com', organization_type=OrganizationType.objects.get(id=1));
        self.org2 = Organization(name='test org 2', contact_email='test2@test.com', organization_type=OrganizationType.objects.get(id=2));
        self.org3 = Organization(name='test org 3', contact_email='test3@test.com', organization_type=OrganizationType.objects.get(id=1));
        
        self.org1.save();
        self.org2.save();
        self.org3.save();

    def testViewClubNotLoggedIn(self):
    	response = self.client.get(self.baseURL + '/clubs/1');

    	self.assertTrue(self.org1.name in response.content);
    	self.assertTrue(self.user.username in response.content);
    	self.assertTrue('href="/clubs/1')

    def tearDown(self):
        self.client.logout();