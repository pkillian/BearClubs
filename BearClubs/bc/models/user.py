import datetime

from django.db import models

class User(models.Model):
    username     = models.CharField(max_length=128, unique=True);
    email        = models.EmailField(max_length=128, unique=True);
    first_name   = models.CharField(max_length=64);
    last_name    = models.CharField(max_length=64);
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
