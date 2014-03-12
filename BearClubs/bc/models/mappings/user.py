import datetime

from django.db import models

from BearClubs.bc.models.user import User
from BearClubs.bc.models.organization import Organization

class UserToOrganization(models.Model):
    user         = models.ManyToManyField(User);
    organization = models.ManyToManyField(Organization);
    created_at   = models.DateTimeField(editable=False);
    updated_at   = models.DateTimeField();

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        datetime_now = datetime.datetime.now();

        # If there's no ID, it's new
        if not self.id:
            self.created_at = datetime_now;

        # Always update the modified at value
        self.modified_at = datetime_now;

        return super(User, self).save(*args, **kwargs);

    class Meta:
        app_label = 'bc';
        db_table  = 'bc_user_to_organization';
