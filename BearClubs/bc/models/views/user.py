import datetime

from django.db import models

from BearClubs.bc.models.event import Event
from BearClubs.bc.models.organization import Organization
from BearClubs.bc.models.user import User

class UserSubscriptionView(models.Model):
    # See (http://zxq9.com/archives/616) for unmanaged pSQL view help

    class Meta:
        managed   = False;
        app_label = 'bc';
        db_table  = 'bc_user_subscription_view';
