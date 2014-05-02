from cStringIO import StringIO

import haystack

from django.conf import settings
from django.core import management
from django.test import TestCase, Client
from django.test.utils import override_settings
from django.utils import unittest, timezone
from django.utils.unittest import TestLoader, TextTestRunner

from BearClubs.bc.models import User, Event, Organization, OrganizationType

class SearchEndToEndTests(TestCase):
    fixtures = ['test_data.json']

    def setUp(self):
        haystack.connections.reload('test')
        super(SearchEndToEndTests, self).setUp()
        self.client = Client()

    # Error with Haystack
    # def testUser(self):
    #     user = User(username='testsearch', password='1234', email='test@search.com')
    #     user.set_password('1234')
    #     user.save();

    #     response = self.client.get('/search/?q=test')
    #     result_html = 'User: testsearch</a>'

    #     # Check that the response is 200 OK.
    #     self.assertEqual(response.status_code, 200)

    #     # Check that response contains result html
    #     self.assertContains(response, result_html, 0)

    def testOrganization(self):
        response = self.client.get('/search/?q=test')
        result_html = '<a href="/clubs/1">Organization: Test Club</a>'

        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)

        # Check that response contains result html
        self.assertContains(response, result_html, 1)

    def testEvent(self):
        response = self.client.get('/search/?q=test')
        result_html = 'Event: Test Event 1</a>'

        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)

        # Check that response contains result html
        self.assertContains(response, result_html, 1)

    def tearDown(self):
        management.call_command('clear_index', interactive=False, verbosity=0)

# If this file is invoked as a Python script, run the tests in this module
if __name__ == "__main__":
    # Add a verbose argument
    sys.argv = [sys.argv[0]] + ["-v"] + sys.argv[1:]
    unittest.main()