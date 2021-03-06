from django.db import models
from django.utils import timezone

from BearClubs.bc.models.event import Event
from BearClubs.bc.models.organization import Organization
from BearClubs.bc.models.user import User

class UserToOrganization(models.Model):
    user          = models.ForeignKey('User');
    organization  = models.ForeignKey('Organization');
    admin         = models.BooleanField(default=False);
    created_at    = models.DateTimeField(default=timezone.now, editable=False);
    updated_at    = models.DateTimeField(default=timezone.now);

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        datetime_now = timezone.now();

        # If there's no ID, it's new
        if not self.id:
            self.created_at = datetime_now;

        # Always update the modified at value
        self.modified_at = datetime_now;

        return super(UserToOrganization, self).save(*args, **kwargs);

    @staticmethod
    def getOrganizationsForUser(user):
        uto_objects = UserToOrganization.objects.filter(user=user.id);
        return [uto.organization for uto in uto_objects];

    class Meta:
        app_label = 'bc';
        db_table  = 'bc_user_to_organization';
        unique_together = ('user', 'organization');

class UserToEvent(models.Model):
    user       = models.ForeignKey('User');
    event      = models.ForeignKey('Event');
    admin      = models.BooleanField(default=False);
    created_at = models.DateTimeField(default=timezone.now, editable=False);
    updated_at = models.DateTimeField(default=timezone.now);

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        datetime_now = timezone.now();

        # If there's no ID, it's new
        if not self.id:
            self.created_at = datetime_now;

        # Always update the modified at value
        self.modified_at = datetime_now;

        return super(UserToEvent, self).save(*args, **kwargs);

    @staticmethod
    def getUsersForEvent(event):
        ute_objects = UserToEvent.objects.filter(event=event.id);
        return [ute.user for ute in ute_objects];

    @staticmethod
    def getEventsForUser(user):
        ute_objects = UserToEvent.objects.filter(user=user.id);
        return [ute.event for ute in ute_objects];

    @staticmethod
    def userSubscribedToEvent(user=None, event=None):
        if (not user) or (not event):
            return False;

        if event in UserToEvent.getEventsForUser(user):
            return True;

        return False;

    class Meta:
        app_label = 'bc';
        db_table  = 'bc_user_to_event';
        unique_together = ('user', 'event');
