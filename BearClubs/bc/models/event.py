from django.utils import timezone
from django.core.exceptions import ValidationError
from django.db import models
from django.core.urlresolvers import reverse

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

    @staticmethod
    def getEventsByPage(page, increment=50):
        assert(page > 0);
        assert(increment > 0);

        max_page = Event.getMaxPage(increment);

        if page > max_page:
            page = max_page;

        # get START_INDEX based on page and increment parameters
        start_index = (page - 1) * increment;

        # only get INCREMENT items at a time
        end_index = start_index + increment;

        return Event.objects.order_by('name')[start_index:end_index];

    @staticmethod
    def getMaxPage(increment):
        total_events = Event.objects.count();
        max_page = (total_events // increment);

        # if there's a remainder, add one
        if total_events % increment != 0:
            max_page += 1;

        if max_page <= 0:
            max_page = 1;

        return max_page;

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
        return reverse('event', args=[self.id]);

    def __unicode__(self):
        return 'Event: %s' % (self.name)

    class Meta:
        app_label = 'bc';
