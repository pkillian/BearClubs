from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.core.context_processors import csrf
from django.shortcuts import render, redirect

from BearClubs.bc.forms import UserSignUpForm, UserSignInForm
from BearClubs.bc.models import User;

@login_required(login_url='/login')
def dashboard(request):
    args = {};
    args['user'] = request.user;

    return render(request, "dashboard.html", args);

@login_required(login_url='/login')
def profile(request, user_id):
    args = {};
    args['user'] = User.objects.get(id=user_id);

    return render(request, "userProfile.html", args);

def userSignUp(request):
    if request.method == 'POST':
        form = UserSignUpForm(request.POST)
        if form.is_valid():
            # return successful registration, should login user and redirect to club directory
            user = form.save()
            auth.login(request, user)
            return redirect("/clubs")
        else:
            # find out which fields were invalid and return error
            return userFormsRender(request, signUpForm=form)

    else:
        if (request.user.is_authenticated()):
            # if user is already authenticated then redirect to club directory
            return redirect("/clubs")
        else:
            return userFormsRender(request)

def userSignIn(request):
    if request.method == 'POST':
        form = UserSignInForm(data=request.POST);

        if form.is_valid():
            form.loginUser(request);

            # On successful authentication, redirect to club directory
            return redirect("/clubs");
        else:
            # On unsuccessful authentication, return error
            return userFormsRender(request, signInForm=form);
    else:
        if (request.user.is_authenticated()):
            # if user is already authenticated then redirect to club directory
            return redirect("/clubs")
        else:
            return userFormsRender(request);

def userLogOut(request):
    auth.logout(request)
    return render(request, 'index.html')

def userFormsRender(request, signUpForm=None, signInForm=None):
    args = {};
    args.update(csrf(request));

    if signUpForm == None:
        signUpForm = UserSignUpForm();

    if signInForm == None:
        signInForm = UserSignInForm();

    args['signup_form'] = signUpForm;
    args['signin_form'] = signInForm;

    return render(request, 'signup.html', args);
