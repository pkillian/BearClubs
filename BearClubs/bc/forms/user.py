from django import forms
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from BearClubs.bc.models import User

class UserSignUpForm(UserCreationForm):
    username     = forms.CharField(required=True);
    email        = forms.EmailField(required=True);
    #password     = forms.CharField(required=True, widget=forms.PasswordInput);

    def clean_username(self):
        # TODO: check that username doesn't exist

        return self.cleaned_data.get('username');

    def clean_password(self):
        password     = self.cleaned_data.get('password1');
        confirm_pass = self.cleaned_data.get('password2');

        if not confirm_pass:
            raise forms.ValidationError("You must confirm your password");
        if password != confirm_pass:
            raise forms.ValidationError("Password and Confirm Password must match");

        # Passwords match; return the password
        return password;

    def save(self, commit=True):   
        user            = super(UserSignUpForm, self).save(commit=False);

        user.username   = self.cleaned_data['username'];
        user.email      = self.cleaned_data['email'];
        user.password   = self.cleaned_data['password1'];

        if commit:
            user.save();

        return user;

    class Meta:
        model = User;
        fields = ('username', 'email', 'password1', 'password2');

class UserSignInForm(AuthenticationForm):

    def loginUser(self, request):
        user = {}

        username = self.cleaned_data['username']
        password = self.cleaned_data['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user);
            else:
                return False
                # Return a 'disabled account' error message
        else:
            return False
            # Return an 'invalid login' error message
