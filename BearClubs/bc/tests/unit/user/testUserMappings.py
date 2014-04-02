from cStringIO import StringIO

from django.db import IntegrityError
from django.test import TestCase
from django.utils import unittest, timezone

from BearClubs.bc.models import Event, Organization, OrganizationType, User, UserToEvent, UserToOrganization

class UserToEventMappingTests(TestCase):

    def setUp(self):
        self.user = User(username='test', password='1234', email='test@test.com');
        self.user.save();

        self.org = Organization(name='test org', contact_email='test@test.com', organization_type=OrganizationType.objects.get(id=1));
        self.org.save();

        self.event = Event(name='test 1', contact_email='test@test.com', organization=self.org, start_time=timezone.now(), end_time=timezone.now());
        self.event2 = Event(name='test 2', contact_email='test@test.com', organization=self.org, start_time=timezone.now(), end_time=timezone.now());
        self.event3 = Event(name='test 3', contact_email='test@test.com', organization=self.org, start_time=timezone.now(), end_time=timezone.now());

        self.event.save();
        self.event2.save();
        self.event3.save();

    def testAddValidUserToEventMapping_NoAdmin(self):
        UserToEvent(user=self.user, event=self.event).save();

        ute = UserToEvent.objects.filter(user=self.user);
        ute = ute[0];

        self.assertTrue(ute.user == self.user);
        self.assertTrue(ute.event == self.event);
        self.assertFalse(ute.admin);

    def testAddValidUserToEventMapping_Admin(self):
        UserToEvent(user=self.user, event=self.event, admin=True).save();

        ute = UserToEvent.objects.filter(user=self.user);
        ute = ute[0];

        self.assertTrue(ute.user == self.user);
        self.assertTrue(ute.event == self.event);
        self.assertTrue(ute.admin);

    def testAddValidUserToEventMapping_ManyEvents(self):
        UserToEvent(user=self.user, event=self.event, admin=True).save();
        UserToEvent(user=self.user, event=self.event2).save();
        UserToEvent(user=self.user, event=self.event3, admin=True).save();

        ute = UserToEvent.objects.filter(user=self.user);
        ute1 = ute[0];
        ute2 = ute[1];
        ute3 = ute[2];

        self.assertTrue(ute1.user == self.user);
        self.assertTrue(ute1.event == self.event);
        self.assertTrue(ute1.admin);

        self.assertTrue(ute2.user == self.user);
        self.assertTrue(ute2.event == self.event2);
        self.assertFalse(ute2.admin);

        self.assertTrue(ute3.user == self.user);
        self.assertTrue(ute3.event == self.event3);
        self.assertTrue(ute3.admin);

    def testAddValidUserToEventMapping_GetEventsForUser(self):
        UserToEvent(user=self.user, event=self.event, admin=True).save();
        UserToEvent(user=self.user, event=self.event2).save();
        UserToEvent(user=self.user, event=self.event3, admin=True).save();

        ute = UserToEvent.getEventsForUser(self.user);
        event_result1 = ute[0];
        event_result2 = ute[1];
        event_result3 = ute[2];

        self.assertTrue(event_result1 == self.event);
        self.assertTrue(event_result2 == self.event2);
        self.assertTrue(event_result3 == self.event3);

    def testInvalidUserToEvent_NoUser(self):
        try:
            UserToEvent(event=self.event).save();
        except IntegrityError:
            return True;

    def testInvalidUserToEvent_NoEvent(self):
        try:
            UserToEvent(user=self.user).save();
        except IntegrityError:
            return True;

    def testInvalidUserToEvent_Duplicate(self):
        try:
            UserToEvent(user=self.user, event=self.event).save();
            UserToEvent(user=self.user, event=self.event).save();
        except IntegrityError:
            return True;


class UserToOrganizationMappingTests(TestCase):

    def setUp(self):
        self.user = User(username='test', password='1234', email='test@test.com');
        self.user.save();

        self.org = Organization(name='test org', contact_email='test@test.com', organization_type=OrganizationType.objects.get(id=1));
        self.org2 = Organization(name='test org 2', contact_email='test2@test.com', organization_type=OrganizationType.objects.get(id=2));
        self.org3 = Organization(name='test org 3', contact_email='test3@test.com', organization_type=OrganizationType.objects.get(id=1));

        self.org.save();
        self.org2.save();
        self.org3.save();

        self.event = Event(name='test 1', contact_email='test@test.com', organization=self.org, start_time=timezone.now(), end_time=timezone.now());
        self.event.save();

    def testAddValidUserToOrganizationMapping_NoAdmin(self):
        UserToOrganization(user=self.user, organization=self.org).save();

        uto = UserToOrganization.objects.filter(user=self.user);
        uto = uto[0];

        self.assertTrue(uto.user == self.user);
        self.assertTrue(uto.organization == self.org);
        self.assertFalse(uto.admin);

    def testAddValidUserToOrganizationMapping_Admin(self):
        UserToOrganization(user=self.user, organization=self.org, admin=True).save();

        uto = UserToOrganization.objects.filter(user=self.user);
        uto = uto[0];

        self.assertTrue(uto.user == self.user);
        self.assertTrue(uto.organization == self.org);
        self.assertTrue(uto.admin);

    def testAddValidUserToEventMapping_ManyOrganizations(self):
        UserToOrganization(user=self.user, organization=self.org, admin=True).save();
        UserToOrganization(user=self.user, organization=self.org2).save();
        UserToOrganization(user=self.user, organization=self.org3, admin=True).save();

        uto = UserToOrganization.objects.filter(user=self.user);
        uto1 = uto[0];
        uto2 = uto[1];
        uto3 = uto[2];

        self.assertTrue(uto1.user == self.user);
        self.assertTrue(uto1.organization == self.org);
        self.assertTrue(uto1.admin);

        self.assertTrue(uto2.user == self.user);
        self.assertTrue(uto2.organization == self.org2);
        self.assertFalse(uto2.admin);

        self.assertTrue(uto3.user == self.user);
        self.assertTrue(uto3.organization == self.org3);
        self.assertTrue(uto3.admin);

    def testAddValidUserToEventMapping_GetOrganizationsForUser(self):
        UserToOrganization(user=self.user, organization=self.org, admin=True).save();
        UserToOrganization(user=self.user, organization=self.org2).save();
        UserToOrganization(user=self.user, organization=self.org3, admin=True).save();

        uto = UserToOrganization.getOrganizationsForUser(self.user);
        org_result1 = uto[0];
        org_result2 = uto[1];
        org_result3 = uto[2];

        self.assertTrue(org_result1 == self.org);
        self.assertTrue(org_result2 == self.org2);
        self.assertTrue(org_result3 == self.org3);

    def testInvalidUserToOrganization_NoUser(self):
        try:
            UserToOrganization(organization=self.org).save();
        except IntegrityError:
            return True;

    def testInvalidUserToOrganization_NoOrganization(self):
        try:
            UserToOrganization(user=self.user).save();
        except IntegrityError:
            return True;

    def testInvalidUserToOrganization_Duplicate(self):
        try:
            UserToOrganization(user=self.user, organization=self.org).save();
            UserToOrganization(user=self.user, organization=self.org).save();
        except IntegrityError:
            return True;

# If this file is invoked as a Python script, run the tests in this module
if __name__ == "__main__":
    # Add a verbose argument
    sys.argv = [sys.argv[0]] + ["-v"] + sys.argv[1:]
    unittest.main()
