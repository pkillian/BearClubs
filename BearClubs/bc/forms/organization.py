from django import forms

from BearClubs.bc.models import Organization, OrganizationType

class AddClubForm(forms.ModelForm):

    def __init__(self, request, *args, **kwargs):
        forms.ModelForm.__init__(self, *args, **kwargs);

        self.request = request;
        self.fields['contact_email'].initial = request.user.email;

    class Meta:
        model   = Organization;
        fields  = ('name', 'description', 'contact_email', 'organization_type');
