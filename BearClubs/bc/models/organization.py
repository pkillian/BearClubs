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

    @staticmethod
    def getClubsByPage(page, increment=50):
        assert(page > 0);
        assert(increment > 0);

        max_page = Organization.getMaxPage(increment);

        if page > max_page:
            page = max_page;

        # get START_INDEX based on page and increment parameters
        start_index = (page - 1) * increment;

        # only get INCREMENT items at a time
        end_index = start_index + increment;

        return Organization.objects.order_by('name')[start_index:end_index];

    @staticmethod
    def getMaxPage(increment):
        total_clubs = Organization.objects.count();
        max_page = (total_clubs // increment);

        # if there's a remainder, add one
        if total_clubs % increment != 0:
            max_page += 1;

        if max_page <= 0:
            max_page = 1;

        return max_page;

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
