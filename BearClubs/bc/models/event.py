from django.utils import timezone

from django.db import models

class Event(models.Model):
    name           = models.CharField(max_length=128);
    description    = models.TextField(blank=True);
    organization   = models.ForeignKey('Organization');
    start_time     = models.DateTimeField();
    end_time       = models.DateTimeField();
    location       = models.CharField(max_length=256, blank=True);
    location_lat   = models.CharField(max_length=256, blank=True);
    location_lng   = models.CharField(max_length=256, blank=True);
    contact_email  = models.EmailField(max_length=128);
    created_at     = models.DateTimeField(default=timezone.now, editable=False);
    updated_at     = models.DateTimeField(default=timezone.now);

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        datetime_now = timezone.now();

        # If there's no ID, it's new
        if not self.id:
            self.created_at = datetime_now;

        # Always update the modified at value
        self.updated_at = datetime_now;

        return super(Event, self).save(*args, **kwargs);

    def get_absolute_url(self):
        return ''

    def __unicode__(self):
        return 'Event: %s' % (self.name)

    class Meta:
        app_label = 'bc';
