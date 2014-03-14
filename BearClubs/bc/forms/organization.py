from django import forms
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from BearClubs.bc.models import User

class AddClubForm(forms.Form):

    club_name            = forms.CharField(required=True);
    description          = forms.CharField(widget=forms.Textarea, required=True);
    contact_email        = forms.EmailField(required=True);

    def __init__(self, request, *args, **kwargs):
        forms.Form.__init__(self, *args, **kwargs);

        self.request = request;
        self.fields['contact_email'].initial = request.user.email;


    def setUser(self, request):
        self.user = request.user;

    def save(self, commit=True):   
        user            = super(UserSignUpForm, self).save(commit=False);

        user.username   = self.cleaned_data['username'];
        user.email      = self.cleaned_data['email'];
        
        user.set_password(self.cleaned_data['password1']);

        if commit:
            user.save();

        return authenticate(username=self.cleaned_data['username'], password=self.cleaned_data['password1']);

    class Meta:
        model = User;
        fields = ('club_name', 'description' 'contact_email');
