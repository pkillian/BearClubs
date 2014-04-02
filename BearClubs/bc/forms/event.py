from django import forms
from django.utils import timezone
from BearClubs.bc.models import Event, Organization
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
        self.fields['organization']=forms.ModelChoiceField(queryset=Organization.objects.all())

    def is_valid(self):
 
        # run the parent validation first
        valid = super(AddEventForm, self).is_valid();
 
        # we're done now if not valid
        if not valid:
            return valid;

        if self.cleaned_data['start_time'] > self.cleaned_data['end_time']:
            self._errors['time_error'] = "start time must be before end time";
            return False;

        if self.cleaned_data['start_time'] < timezone.now():
            self._errors['time_error'] = "start time must be after current time";
            return False;

        if self.cleaned_data['end_time'] < timezone.now():
            self._errors['time_error'] = "end time must be after current time";
            return False;

        return True;
   

    class Meta:
        model   = Event;
        fields  = ('name', 'description', 'organization', 'start_time', 'end_time', 'location', 'contact_email');