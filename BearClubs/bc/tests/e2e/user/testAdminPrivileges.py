from cStringIO import StringIO
import re

from django.db import IntegrityError
from django.test import TestCase, Client
from django.utils import unittest, timezone

from BearClubs.bc.models import Event, Organization, OrganizationType, User, UserToEvent, UserToOrganization

class AdminTests(TestCase):

    client = Client();

    def setUp(self):
    	self.baseURL = 'http://localhost:8000';

        self.user = User(username='test', password='1234', email='test@test.com');
        self.user.set_password('1234');
        self.user.save();

        self.user2 = User(username='test2', password='12345', email='test2@test.com');
        self.user2.set_password('12345');
        self.user2.save();

        self.org1 = Organization(name='test org 1', contact_email='test1@test.com', organization_type=OrganizationType.objects.get(id=1));
        self.org1.save();

    def testClubCreatorAddedasAdmin(self):
    	"""
    	Tests that the club creator is automatically added as a member to the club and is an admin.
    	"""

    	self.client.login(username='test', password='1234');

        form_data = {
            'name': 'Test Club',
            'description': 'Club Description',
            'contact_email': 'test@test.com',
            'organization_type': 1
        };

        response = self.client.post(self.baseURL+'/clubs/new', form_data);
        
        test_club = Organization.objects.get(name="Test Club");
        test_user = User.objects.get(username="test");

        self.assertEquals(test_user, UserToOrganization.objects.get(user=test_user, organization=test_club).user);
        self.assertEquals(test_club, UserToOrganization.objects.get(user=test_user, organization=test_club).organization);
        self.assertTrue(UserToOrganization.objects.get(user=test_user, organization=test_club).admin);
    
    def testPromoteMembersAsAdmin(self):
    	"""
    	Tests that an admin of a club can promote members to admin and members are promoted to admins.
    	"""

    	# make user an admin
    	self.uto1 = UserToOrganization(user=self.user, organization=self.org1, admin=True);
    	self.uto1.save();

    	# add user2 to club (not as admin)
    	self.uto2 = UserToOrganization(user=self.user2, organization=self.org1);
    	self.uto2.save();

    	# login as user (admin)
    	self.client.login(username='test', password='1234');

    	# uto_id is connected to user2, the user we want to promote
    	data = {
    		'org_id': self.org1.id,
    		'uto_id': self.uto2.id,
    	};

    	# send data to promote
    	response = self.client.post(self.baseURL+'/user/promote', data);

    	# get the club and user we want to verify directly from db
        test_club = Organization.objects.get(name="test org 1");
        test_user = User.objects.get(username="test2");

        # check that the uto is of user2 and org1
    	self.assertEquals(test_user, UserToOrganization.objects.get(user=test_user, organization=test_club).user);
        self.assertEquals(test_club, UserToOrganization.objects.get(user=test_user, organization=test_club).organization);

        # check that user2 is now an admin
        self.assertTrue(UserToOrganization.objects.get(user=test_user, organization=test_club).admin);
    
    def testPromoteMembersNotAsAdmin(self):
    	"""
    	Tests that a regular member cannot promote other members as admins
    	"""

    	# add user to club (not as admin)
    	self.uto1 = UserToOrganization(user=self.user, organization=self.org1);
    	self.uto1.save();

    	# add user2 to club (not as admin)
    	self.uto2 = UserToOrganization(user=self.user2, organization=self.org1);
    	self.uto2.save();

    	# login as user
    	self.client.login(username='test', password='1234');

    	# uto_id is connected to user2, the user we want to promote
    	data = {
    		'org_id': self.org1.id,
    		'uto_id': self.uto2.id,
    	};

    	# user tries to promote
    	response = self.client.post(self.baseURL+'/user/promote', data);

    	# get the club and user we want to verify directly from db
        test_club = Organization.objects.get(name="test org 1");
        test_user = User.objects.get(username="test2");

        # check that the uto is of user2 and org1
    	self.assertEquals(test_user, UserToOrganization.objects.get(user=test_user, organization=test_club).user);
        self.assertEquals(test_club, UserToOrganization.objects.get(user=test_user, organization=test_club).organization);

        # check that user2 is NOT an admin
        self.assertFalse(UserToOrganization.objects.get(user=test_user, organization=test_club).admin);

	def testDemoteMembersAsAdmin(self):
		"""
    	Tests that an admin of a club can demote other admins and the selected admins are demoted to members.
    	"""
    	# make user an admin
        self.uto1 = UserToOrganization(user=self.user, organization=self.org1, admin=True);
        self.uto1.save();

        # add user2 to club (not as admin)
        self.uto2 = UserToOrganization(user=self.user2, organization=self.org1);
        self.uto2.save();

        # login as user (admin)
        self.client.login(username='test', password='1234');

        # uto_id is connected to user2, the user we want to promote
        data = {
            'org_id': self.org1.id,
            'uto_id': self.uto2.id,
        };

        # send data to demote
        response = self.client.post(self.baseURL+'/user/demote', data);

        # get the club and user we want to verify directly from db
        test_club = Organization.objects.get(name="test org 1");
        test_user = User.objects.get(username="test2");

        # check that the uto is of user2 and org1
        self.assertEquals(test_user, UserToOrganization.objects.get(user=test_user, organization=test_club).user);
        self.assertEquals(test_club, UserToOrganization.objects.get(user=test_user, organization=test_club).organization);

        # check that user2 is now not an admin
        self.assertFalse(UserToOrganization.objects.get(user=test_user, organization=test_club).admin);

    def testDemoteMembersNotAsAdmin(self):
    	"""
    	Tests that a regular member cannot deomote admins to regular members.
    	"""
    	# add user to club (not as admin)
        self.uto1 = UserToOrganization(user=self.user, organization=self.org1);
        self.uto1.save();

        # add user2 to club (not as admin)
        self.uto2 = UserToOrganization(user=self.user2, organization=self.org1);
        self.uto2.save();

        # login as user
        self.client.login(username='test', password='1234');

        # uto_id is connected to user2, the user we want to demote
        data = {
            'org_id': self.org1.id,
            'uto_id': self.uto2.id,
        };

        # user tries to demote
        response = self.client.post(self.baseURL+'/user/demote', data);

        # get the club and user we want to verify directly from db
        test_club = Organization.objects.get(name="test org 1");
        test_user = User.objects.get(username="test2");

        # check that the uto is of user2 and org1
        self.assertEquals(test_user, UserToOrganization.objects.get(user=test_user, organization=test_club).user);
        self.assertEquals(test_club, UserToOrganization.objects.get(user=test_user, organization=test_club).organization);

        # check that user2 is NOT an admin
        self.assertFalse(UserToOrganization.objects.get(user=test_user, organization=test_club).admin);
    
    def tearDown(self):
        self.client.logout();


# If this file is invoked as a Python script, run the tests in this module
if __name__ == "__main__":
    # Add a verbose argument
    sys.argv = [sys.argv[0]] + ["-v"] + sys.argv[1:]
    unittest.main()

