import datetime

from django.db import models

class Organization(models.Model):
    name           = models.CharField(max_length=128, unique=True);
    description    = models.TextField(blank=True);
    location       = models.CharField(max_length=256, blank=True);
    contact_email  = models.EmailField(max_length=128, unique=True);
    org_type       = models.ForeignKey('OrganizationType');
    created_at     = models.DateTimeField(editable=False);
    updated_at     = models.DateTimeField();

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

class OrganizationType(models.Model):
    name           = models.CharField(max_length=128, unique=True);
    description    = models.CharField(max_length=256, unique=True);
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
        db_table  = 'bc_organization_type';
