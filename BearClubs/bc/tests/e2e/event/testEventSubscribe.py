from django.test import TestCase
from BearClubs.bc.forms import AddEventForm
from BearClubs.bc.models import User, Organization, OrganizationType, Event, UserToEvent
from django.utils import timezone
import datetime

from django.utils import unittest
from django.utils.unittest import TestLoader, TextTestRunner
from cStringIO import StringIO

from django.db import IntegrityError, transaction
from django.core.exceptions import ObjectDoesNotExist
from django.test import Client

class EventSubscribeTests(TestCase):
    baseURL = 'http://localhost:8000';

    fixtures = ['test_data.json'];
    client = Client();

    def setUp(self):
        self.user = User.objects.get(id=1);
        self.event_1 = Event.objects.get(id=1);
        self.event_2 = Event.objects.get(id=2);

        self.client.login(username='test', password='1234');

    def testEventSubscribe(self):
        self.client.post(self.baseURL + '/events/subscribe', {'event_id': 2});

        self.assertTrue(UserToEvent.userSubscribedToEvent(user=self.user, event=self.event_2));

    def testEventUnsubscribe(self):
        self.client.post(self.baseURL + '/events/unsubscribe', {'event_id': 1});

        self.assertFalse(UserToEvent.userSubscribedToEvent(user=self.user, event=self.event_1));

    def testEventSubscribeMoreThanOnce(self):
        self.client.post(self.baseURL + '/events/subscribe', {'event_id': 2});

        try:
            with transaction.atomic():
                self.client.post(self.baseURL + '/events/subscribe', {'event_id': 2});
        except IntegrityError:
            pass;

        self.assertTrue(UserToEvent.userSubscribedToEvent(user=self.user, event=self.event_2));


    def testEventUnubscribeWhenNotSubscribed(self):
        try:
            with transaction.atomic():
                self.client.post(self.baseURL + '/events/unsubscribe', {'event_id': 2});
        except ObjectDoesNotExist:
            pass;
        
        self.assertFalse(UserToEvent.userSubscribedToEvent(user=self.user, event=self.event_2));
