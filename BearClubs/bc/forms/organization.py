from django import forms

from BearClubs.bc.models import Organization, OrganizationType

class AddClubForm(forms.ModelForm):

    def __init__(self, user, *args, **kwargs):
        forms.ModelForm.__init__(self, *args, **kwargs);

        self.user = user;
        self.fields['contact_email'].initial = user.email;

    class Meta:
        model   = Organization;
        fields  = ('name', 'description', 'contact_email', 'organization_type');
