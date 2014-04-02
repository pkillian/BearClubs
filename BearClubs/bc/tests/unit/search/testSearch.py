from cStringIO import StringIO

import haystack

from django.conf import settings
from django.core import management
from django.test import TestCase, Client
from django.test.utils import override_settings
from django.utils import unittest, timezone
from django.utils.unittest import TestLoader, TextTestRunner

from BearClubs.bc.models import User, Event, Organization, OrganizationType

TEST_INDEX = {
    'default': {
        'ENGINE': 'haystack.backends.elasticsearch_backend.ElasticsearchSearchEngine',
        'URL': 'http://127.0.0.1:9200/',
        'TIMEOUT': 60 * 10,
        'INDEX_NAME': 'test_index',
    },
}

@override_settings(HAYSTACK_CONNECTIONS=TEST_INDEX)
class SearchUnitTests(TestCase):

    # Test cases:
    # -- Haystack indexes User model
    # -- Haystack indexes Organization model
    # -- Haystack indexes Event model

    def setUp(self):
        haystack.connections.reload('default')
        super(SearchUnitTests, self).setUp()

        bus_org_type = OrganizationType.objects.get(name='Business');
        cs_org_type = OrganizationType.objects.get(name='Computer Science');

        User(username='test', password='1234', email='test@test.com').save();
        
        organization_1 = Organization(name='Test 1', description='Test 1 Desc', contact_email='test1@test.com', organization_type=bus_org_type).save();
        organization_2 = Organization(name='Test 2', description='Test 2 Desc', contact_email='test2@test.com', organization_type=cs_org_type).save();
        organization_3 = Organization(name='Test 3', description='Test 3 Desc', contact_email='test3@test.com', organization_type=bus_org_type).save();

        Event(name='testevent', description='event description', organization=Organization.objects.get(name='Test 1'),  start_time=timezone.now(), end_time=timezone.now()).save();

    def testUserIndex(self):
        results = haystack.query.SearchQuerySet().models(User).all()
        assert results.count() == User.objects.count(), "Got %d; expected %d" % (results.count(), User.objects.count());

    def testOrganizationIndex(self):
        results = haystack.query.SearchQuerySet().models(Organization).all()
        assert results.count() == Organization.objects.count(), "Got %d; expected %d" % (results.count(), Organization.objects.count());

    def testEventIndex(self):
        results = haystack.query.SearchQuerySet().models(Event).all()
        assert results.count() == Event.objects.count(), "Got %d; expected %d" % (results.count(), Event.objects.count());

    def tearDown(self):
        management.call_command('clear_index', interactive=False, verbosity=0)

@override_settings(HAYSTACK_CONNECTIONS=TEST_INDEX)
class SearchEndToEndTests(TestCase):

    # Test cases:

    def setUp(self):
        self.client = Client()

        bus_org_type = OrganizationType.objects.get(name='Business');
        business_club = Organization(name='Business Club', description='Test 1 Desc', contact_email='test1@test.com', organization_type=bus_org_type).save();

        User(username='test', password='1234', email='test@test.com').save();

        Event(name='event', description='event description', organization=Organization.objects.get(name='Business Club'),  start_time=timezone.now(), end_time=timezone.now()).save();


    def testUser(self):
        response = self.client.get('/search/?q=test')
        result_html = '<a href="/user/1">User: test</a>'

        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)

        # Check that response contains result html
        self.assertContains(response, result_html, 1)

    def testOrganization(self):
        response = self.client.get('/search/?q=business')
        result_html = '<a href="/clubs/1">Organization: Business Club</a>'

        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)

        # Check that response contains result html
        self.assertContains(response, result_html, 1)

    def testEvent(self):
        response = self.client.get('/search/?q=event')
        result_html = 'Event: event</a>'

        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)

        # Check that response contains result html
        self.assertContains(response, result_html, 1)

# If this file is invoked as a Python script, run the tests in this module
if __name__ == "__main__":
    # Add a verbose argument
    sys.argv = [sys.argv[0]] + ["-v"] + sys.argv[1:]
    unittest.main()