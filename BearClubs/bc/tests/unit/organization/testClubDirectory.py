from django.test import TestCase
from BearClubs.bc.forms import AddClubForm
from BearClubs.bc.models import User, Organization, OrganizationType

from django.utils import unittest
from django.utils.unittest import TestLoader, TextTestRunner
from cStringIO import StringIO

from django.test import Client

class GetClubsByPageUnitTests(TestCase):

    # Test cases:
    # -- Valid Page 1 and no increment: list all 3 clubs
    # -- Valid Page 1 and Increment 50: list all 3 clubs
    # -- Valid Page 2 and Increment 1: list only 'Test 2'
    # -- Invalid Page 50 and Increment 50: list all 3 clubs

    def setUp(self):
        bus_org_type = OrganizationType.objects.get(name='Business');
        cs_org_type = OrganizationType.objects.get(name='Computer Science');

        User(username='test', password='1234', email='test@test.com').save();
        
        Organization(name='Test 1', description='Test 1 Desc', contact_email='test1@test.com', organization_type=bus_org_type).save();
        Organization(name='Test 2', description='Test 2 Desc', contact_email='test2@test.com', organization_type=cs_org_type).save();
        Organization(name='Test 3', description='Test 3 Desc', contact_email='test3@test.com', organization_type=bus_org_type).save();
        self.user = User.objects.get(username='test');

    def testPageOneNoIncrement(self):
        orgs = Organization.getClubsByPage(1);

        self.assertTrue(len(orgs) == 3);
        self.assertTrue(orgs[0].name == 'Test 1');
        self.assertTrue(orgs[2].name == 'Test 3');

    def testPageOneIncrement50(self):
        orgs = Organization.getClubsByPage(1, 50);

        self.assertTrue(len(orgs) == 3);
        self.assertTrue(orgs[0].name == 'Test 1');
        self.assertTrue(orgs[2].name == 'Test 3');

    def testPageTwoIncrementOne(self):
        orgs = Organization.getClubsByPage(2, 1);

        self.assertTrue(len(orgs) == 1);
        self.assertTrue(orgs[0].name == 'Test 2');

    def testPage50Increment50(self):
        orgs = Organization.getClubsByPage(1);

        self.assertTrue(len(orgs) == 3);
        self.assertTrue(orgs[0].name == 'Test 1');
        self.assertTrue(orgs[2].name == 'Test 3');

class GetMaxPageUnitTests(TestCase):

    # Test cases (6 clubs total):
    # -- Increment 1:  max page == 6
    # -- Increment 2:  max page == 3
    # -- Increment 4:  max page == 2
    # -- Increment 5:  max page == 2
    # -- Increment 6:  max page == 1
    # -- Increment 10: max page == 1

    def setUp(self):
        bus_org_type = OrganizationType.objects.get(name='Business');
        cs_org_type = OrganizationType.objects.get(name='Computer Science');

        User(username='test', password='1234', email='test@test.com').save();
        
        Organization(name='Test 1', description='Test 1 Desc', contact_email='test1@test.com', organization_type=bus_org_type).save();
        Organization(name='Test 2', description='Test 2 Desc', contact_email='test2@test.com', organization_type=cs_org_type).save();
        Organization(name='Test 3', description='Test 3 Desc', contact_email='test3@test.com', organization_type=bus_org_type).save();
        Organization(name='Test 4', description='Test 4 Desc', contact_email='test4@test.com', organization_type=bus_org_type).save();
        Organization(name='Test 5', description='Test 5 Desc', contact_email='test5@test.com', organization_type=cs_org_type).save();
        Organization(name='Test 6', description='Test 6 Desc', contact_email='test6@test.com', organization_type=bus_org_type).save();
        
        self.user = User.objects.get(username='test');

    def testIncrementOne(self):
        self.assertTrue(Organization.getMaxPage(1) == 6);

    def testIncrementTwo(self):
        self.assertTrue(Organization.getMaxPage(2) == 3);

    def testIncrementFour(self):
        self.assertTrue(Organization.getMaxPage(4) == 2);

    def testIncrementFive(self):
        self.assertTrue(Organization.getMaxPage(5) == 2);

    def testIncrementSix(self):
        self.assertTrue(Organization.getMaxPage(6) == 1);

    def testIncrementTen(self):
        self.assertTrue(Organization.getMaxPage(10) == 1);



# If this file is invoked as a Python script, run the tests in this module
if __name__ == "__main__":
    # Add a verbose argument
    sys.argv = [sys.argv[0]] + ["-v"] + sys.argv[1:]
    unittest.main()
