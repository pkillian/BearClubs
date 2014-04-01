from django import forms
from BearClubs.bc.models import Event
from datetimewidget.widgets import DateTimeWidget

class AddEventForm(forms.ModelForm):

    def __init__(self, user, *args, **kwargs):
        forms.ModelForm.__init__(self, *args, **kwargs);
        
        dateTimeOptions = {
             'format': 'mm/dd/yyyy HH:ii P',
             'autoclose': 'true',
             'showMeridian' : 'true'
        }


        self.user = user;
        self.fields['contact_email'].initial = user.email;
        self.fields['start_time'].widget = DateTimeWidget(options = dateTimeOptions)
        self.fields['end_time'].widget = DateTimeWidget(options = dateTimeOptions)

    class Meta:
        model   = Event;
        fields  = ('name', 'description', 'organization', 'start_time', 'end_time', 'location', 'contact_email');