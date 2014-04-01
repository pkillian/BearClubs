from django import forms
from BearClubs.bc.models import Event

class AddEventForm(forms.ModelForm):

    def __init__(self, user, *args, **kwargs):
        forms.ModelForm.__init__(self, *args, **kwargs);

        self.user = user;
        self.fields['contact_email'].initial = user.email;

    class Meta:
        model   = Event;
        fields  = ('name', 'description', 'organization', 'start_time', 'end_time', 'location', 'contact_email');