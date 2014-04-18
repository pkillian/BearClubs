from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.core.context_processors import csrf
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect

from BearClubs.bc.forms import UserSignUpForm, UserSignInForm
from BearClubs.bc.models import User
from BearClubs.bc.models.mappings import UserToEvent, UserToOrganization

@login_required(login_url='/login')
def dashboard(request):
    args = {};
    args['user'] = request.user;
    args['events'] = UserToEvent.getEventsForUser(request.user);

    return render(request, "dashboard.html", args);

@login_required(login_url='/login')
def profile(request, user_id):
    args = {};

    try:
        user = User.objects.get(id=user_id);
    except ObjectDoesNotExist:
        user = request.user;

    if user.first_name:
        user.name = user.first_name;
        if user.last_name: 
            user.name += " " + user.last_name;
    else:
        user.name = user.username;

    user.clubs = UserToOrganization.getOrganizationsForUser(user);
    user.events = UserToEvent.getEventsForUser(user);

    args['user'] = user;

    return render(request, "userProfile.html", args);

@login_required(login_url='/login')
def promote(request):
    org_id = request.POST.get('org_id', '-1');
    uto_id = request.POST.get('uto_id','-1');
    if UserToOrganization.objects.get(user=request.user, organization=org_id).admin == True:
        uto = UserToOrganization.objects.get(id=uto_id);
        uto.admin = True;
        uto.save();

    return redirect('/clubs/'+str(org_id)+'/manage_members');

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

            # On successful authentication, redirect to dashboard
            return redirect("/user");
        else:
            # On unsuccessful authentication, return error
            return userFormsRender(request, signInForm=form);
    else:
        if (request.user.is_authenticated()):
            # if user is already authenticated then redirect to dashboard
            return redirect("/user")
        else:
            return userFormsRender(request);

def userLogOut(request):
    auth.logout(request)
    return redirect('/login')

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
