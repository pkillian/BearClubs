from django import forms
from django.contrib.auth.forms import UserCreationForm

from BearClubs.bc.models import User

class UserSignUpForm(UserCreationForm):
    username     = forms.CharField(required=True);
    email        = forms.EmailField(required=True);
    password     = forms.CharField(required=True, widget=forms.PasswordInput);
    confirm_pass = forms.CharField(required=True, widget=forms.PasswordInput);

    def clean_username(self):
        # TODO: check that username doesn't exist

        return self.cleaned_data.get('username');

    def clean_password(self):
        password     = self.cleaned_data.get('password');
        confirm_pass = self.cleaned_data.get('confirm_pass');

        if not confirm_pass:
            raise forms.ValidationError("You must confirm your password");
        if password != confirm_pass:
            raise forms.ValidationError("Password and Confirm Password must match");

        # Passwords match; return the password
        return password;

    def save(self, commit=True):   
        user            = super(UserSignUpForm, self).save(commit=False)
        user.username   = self.cleaned_data['username'];
        user.email      = self.cleaned_data['email'];
        user.password   = self.cleaned_data['password'];

        if commit:
            user.save();

        return user;

    class Meta:
        model = User;
        fields = ('username', 'email', 'password', 'confirm_pass');
