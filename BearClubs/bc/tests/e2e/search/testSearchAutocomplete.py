from cStringIO import StringIO

import haystack

from django.conf import settings
from django.core import management
from django.test import TestCase, Client
from django.test.utils import override_settings
from django.utils import unittest, timezone
from django.utils.unittest import TestLoader, TextTestRunner

from BearClubs.bc.models import User, Event, Organization, OrganizationType

class SearchAutocompleteEndToEndTests(TestCase):

    def setUp(self):
        haystack.connections.reload('test')
        super(SearchAutocompleteEndToEndTests, self).setUp()
        self.client = Client()

        bus_org_type = OrganizationType.objects.get(name='Business');
        business_club = Organization(name='Business Club', description='Test 1 Desc', contact_email='test1@test.com', organization_type=bus_org_type).save();

        User(username='test', password='1234', email='test@test.com').save();

        Event(name='event', description='event description', organization=Organization.objects.get(name='Business Club'),  start_time=timezone.now(), end_time=timezone.now()).save();


    def testUser(self):
        response = self.client.get('/search/autocomplete/?q=test')
        result = 'test'

        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)

        # Check that response contains result html
        self.assertContains(response, result, 1)

    def testOrganization(self):
        response = self.client.get('/search/autocomplete/?q=business')
        result = 'Business Club'

        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)

        # Check that response contains result html
        self.assertContains(response, result, 1)

    def testEvent(self):
        response = self.client.get('/search/autocomplete/?q=event')
        result = 'event'

        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)

        # Check that response contains result html
        self.assertContains(response, result, 1)

    def tearDown(self):
        management.call_command('clear_index', interactive=False, verbosity=0)

# If this file is invoked as a Python script, run the tests in this module
if __name__ == "__main__":
    # Add a verbose argument
    sys.argv = [sys.argv[0]] + ["-v"] + sys.argv[1:]
    unittest.main()