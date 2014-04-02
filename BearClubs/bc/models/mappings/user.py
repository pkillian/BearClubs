from django.db import models
from django.utils import timezone

from BearClubs.bc.models.event import Event
from BearClubs.bc.models.organization import Organization
from BearClubs.bc.models.user import User

class UserToOrganization(models.Model):
    user         = models.ForeignKey(User);
    organization = models.ManyToManyField(Organization);
    admin        = models.BooleanField(default=False);
    created_at   = models.DateTimeField(default=timezone.now, editable=False);
    updated_at   = models.DateTimeField(default=timezone.now);

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        datetime_now = timezone.now();

        # If there's no ID, it's new
        if not self.id:
            self.created_at = datetime_now;

        # Always update the modified at value
        self.modified_at = datetime_now;

        return super(UserToOrganization, self).save(*args, **kwargs);

    class Meta:
        app_label = 'bc';
        db_table  = 'bc_user_to_organization';

class UserToEvent(models.Model):
    user       = models.ForeignKey(User);
    event      = models.ManyToManyField(Event);
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

    class Meta:
        app_label = 'bc';
        db_table  = 'bc_user_to_event';
