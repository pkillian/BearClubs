from django.utils import timezone

from django.db import models

class Organization(models.Model):
    name                = models.CharField(max_length=128, unique=True);
    description         = models.TextField(blank=True);
    location            = models.CharField(max_length=256, blank=True);
    contact_email       = models.EmailField(max_length=128, unique=True);
    organization_type   = models.ForeignKey('OrganizationType');
    created_at          = models.DateTimeField(default=timezone.now, editable=False);
    updated_at          = models.DateTimeField(default=timezone.now);

    class Meta:
        app_label = 'bc';

class OrganizationType(models.Model):
    name           = models.CharField(max_length=128, unique=True);
    description    = models.CharField(max_length=256, unique=True);
    created_at     = models.DateTimeField(default=timezone.now, editable=False);
    updated_at     = models.DateTimeField(default=timezone.now);

    def __unicode__(self):
        return self.name;

    class Meta:
        app_label = 'bc';
        db_table  = 'bc_organization_type';
