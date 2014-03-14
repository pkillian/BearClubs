from django.test import TestCase
from BearClubs.bc.forms import AddClubForm
from BearClubs.bc.models import User, Organization, OrganizationType

from django.utils import unittest
from django.utils.unittest import TestLoader, TextTestRunner
from cStringIO import StringIO

from django.test import Client

class AddClubUnitTests(TestCase):

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
        User(username='test', password='1234', email='test@test.com').save();
        self.user = User.objects.get(username='test');

    def testValidClub1(self):
        form_data = {
            'name': 'Test Club',
            'description': 'Club Description',
            'contact_email': 'test@test.com',
            'organization_type': 1
        };

        form = AddClubForm(self.user, form_data);

        self.assertTrue(form.is_valid());

        form.save();

        test_club = Organization.objects.get(name='Test Club');

        self.assertTrue(test_club.name == 'Test Club');
        self.assertTrue(test_club.description == 'Club Description');
        self.assertTrue(test_club.contact_email == 'test@test.com');
    
    def testValidClub2(self):
        form_data = {
            'name': 'Test Club',
            'contact_email': 'test@test.com',
            'organization_type': 1
        };

        form = AddClubForm(self.user, form_data);

        self.assertTrue(form.is_valid());

        form.save();

        test_club = Organization.objects.get(name='Test Club');

        self.assertTrue(test_club.name == 'Test Club');
        self.assertTrue(test_club.description == '');
        self.assertTrue(test_club.contact_email == 'test@test.com');

    def testValidClub3(self):
        form_data = {
            'name': "a"*128,
            'description': 'Club Description',
            'contact_email': 'test@test.com',
            'organization_type': 2
        };

        form = AddClubForm(self.user, form_data);

        self.assertTrue(form.is_valid());

        form.save();

        test_club = Organization.objects.get(name="a"*128);

        self.assertTrue(test_club.name == "a"*128);
        self.assertTrue(test_club.description == 'Club Description');
        self.assertTrue(test_club.contact_email == 'test@test.com');

    def testValidClub4(self):
        email_128 = ("a"*119) + "@test.com";

        self.assertTrue(len(email_128) == 128);

        form_data = {
            'name': "Test",
            'description': 'Club Description',
            'contact_email': email_128,
            'organization_type': 2
        };

        form = AddClubForm(self.user, form_data);

        self.assertTrue(form.is_valid());

        form.save();

        test_club = Organization.objects.get(name="Test");

        self.assertTrue(test_club.name == "Test");
        self.assertTrue(test_club.description == 'Club Description');
        self.assertTrue(test_club.contact_email == email_128);

    def testNoNameClub(self):
        form_data = {
            'name': '',
            'description': 'Club Description',
            'contact_email': 'test@test.com',
            'organization_type': 1
        };

        form = AddClubForm(self.user, form_data);

        self.assertTrue(not form.is_valid());

    def testNameTooLongClub(self):
        form_data = {
            'name': "a"*129,
            'description': 'Club Description',
            'contact_email': 'test@test.com',
            'organization_type': 1
        };

        form = AddClubForm(self.user, form_data);

        self.assertTrue(not form.is_valid());

    def testNameNotUnique(self):
        form_data1 = {
            'name': "Test",
            'description': 'Club Description 1',
            'contact_email': 'test1@test.com',
            'organization_type': 1
        };

        form_data2 = {
            'name': "Test",
            'description': 'Club Description 2',
            'contact_email': 'test2@test.com',
            'organization_type': 2
        };

        form = AddClubForm(self.user, form_data1);

        self.assertTrue(form.is_valid());

        form.save();

        form = AddClubForm(self.user, form_data2);

        self.assertTrue(not form.is_valid());

    def testNoEmailClub(self):
        form_data = {
            'name': 'Test',
            'description': 'Club Description',
            'contact_email': '',
            'organization_type': 1
        };

        form = AddClubForm(self.user, form_data);

        self.assertTrue(not form.is_valid());

    def testEmailTooLongClub(self):
        email_gt_128 = ("a"*120) + "@test.com";

        self.assertTrue(len(email_gt_128) > 128);

        form_data = {
            'name': "Test",
            'description': 'Club Description',
            'contact_email': email_gt_128,
            'organization_type': 1
        };

        form = AddClubForm(self.user, form_data);

        self.assertTrue(not form.is_valid());

    def testEmailNotUnique(self):
        form_data1 = {
            'name': "Test 1",
            'description': 'Club Description 1',
            'contact_email': 'test@test.com',
            'organization_type': 1
        };

        form_data2 = {
            'name': "Test 2",
            'description': 'Club Description 2',
            'contact_email': 'test@test.com',
            'organization_type': 2
        };

        form = AddClubForm(self.user, form_data1);

        self.assertTrue(form.is_valid());

        form.save();

        form = AddClubForm(self.user, form_data2);

        self.assertTrue(not form.is_valid());

    def testNoOrgTypeClub(self):
        form_data = {
            'name': "Test",
            'description': 'Club Description',
            'contact_email': 'test@test.com'
        };

        form = AddClubForm(self.user, form_data);

        self.assertTrue(not form.is_valid());

    def testInvalidOrgTypeClub(self):
        form_data = {
            'name': "Test",
            'description': 'Club Description',
            'contact_email': 'test@test.com',
            'organization_type': -1
        };

        form = AddClubForm(self.user, form_data);

        self.assertTrue(not form.is_valid());


# If this file is invoked as a Python script, run the tests in this module
if __name__ == "__main__":
    # Add a verbose argument
    sys.argv = [sys.argv[0]] + ["-v"] + sys.argv[1:]
    unittest.main()
