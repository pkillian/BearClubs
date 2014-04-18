from django import forms
from django.utils import timezone
from datetime import datetime
from BearClubs.bc.models import Event, Organization
from BearClubs.bc.models.mappings import UserToOrganization
from django.contrib.admin import widgets 

class AddEventForm(forms.ModelForm):

    def __init__(self, user, *args, **kwargs):
        forms.ModelForm.__init__(self, *args, **kwargs);
        
        ACCEPTABLE_FORMATS = ['%m/%d/%Y %I:%M:%S %p'];

        self.user = user;
        self.fields['contact_email'].initial = user.email;
        self.fields['start_time'] = forms.DateTimeField(label="Start Time - Format(MM/DD/YYYY HH:MM:SS AM/PM) ", input_formats=ACCEPTABLE_FORMATS);
        self.fields['end_time'] = forms.DateTimeField(label="End Time - Format(MM/DD/YYYY HH:MM:SS AM/PM) ", input_formats=ACCEPTABLE_FORMATS);
        utos = [uto.organization.id for uto in UserToOrganization.objects.filter(user=user, admin=True)];
        self.fields['organization']=forms.ModelChoiceField(queryset=Organization.objects.filter(pk__in=utos));

    def is_valid(self):
 
        # run the parent validation first
        valid = super(AddEventForm, self).is_valid();
 
        # we're done now if not valid
        if not valid:
            return valid;

        startTime = self.cleaned_data['start_time'];
        endTime = self.cleaned_data['end_time'];

        # try:
        #     startTime = self.cleaned_data['start_time'];
        #     startTime = datetime.strptime(startTime, '%m/%d/%Y %I:%M:%S %p');
        # except Exception as e:
        #     self._errors['time_error'] = str(e);
        #     return False;

        # try:
        #     endTime = self.cleaned_data['end_time'];
        #     endTime = datetime.strptime(endTime, '%m/%d/%Y %I:%M:%S %p');
        # except:
        #     self._errors['time_error'] = "end time is invalid format";
        #     return False;


        if startTime > endTime:
            self._errors['time_error'] = "start time must be before end time";
            return False;

        if startTime < timezone.now():
            self._errors['time_error'] = "start time must be after current time";
            return False;

        if endTime < timezone.now():
            self._errors['time_error'] = "end time must be after current time";
            return False;

        return True;
   

    class Meta:
        model   = Event;
        fields  = ('name', 'description', 'organization', 'start_time', 'end_time', 'location', 'contact_email');