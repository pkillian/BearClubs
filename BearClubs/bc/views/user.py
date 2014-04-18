from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.core.context_processors import csrf
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect

from BearClubs.bc.forms import UserSignUpForm, UserSignInForm
from BearClubs.bc.models import User, Organization
from BearClubs.bc.models.mappings import UserToEvent, UserToOrganization

@login_required(login_url='/login')
def dashboard(request):
    args = {};
    args['user'] = request.user;

    clubs = UserToOrganization.getOrganizationsForUser(request.user);
    club_events = list()
    for org in clubs:
        events_for_org = Organization.getEventsForOrganization(org)
        club_events.extend(events_for_org)

    for event in UserToEvent.getEventsForUser(request.user):
        # only add individual event if not suscribed to club that is hosting the event
        if event not in club_events:
            club_events.append(event)

    args['events'] = club_events

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

    club_events = list()
    for org in user.clubs:
        events_for_org = Organization.getEventsForOrganization(org)
        club_events.extend(events_for_org)

    for event in UserToEvent.getEventsForUser(user):
        # only add individual event if not suscribed to club that is hosting the event
        if event not in club_events:
            club_events.append(event)

    user.events = club_events

    print user.events

    args['user'] = user;

    return render(request, "userProfile.html", args);

@login_required(login_url='/login')
def promote(request):
    org_id = int(request.POST.get('org_id', ''));
    uto_id = int(request.POST.get('uto_id',''));
    uto = UserToOrganization.objects.get(id=uto_id);
    uto.admin = True;
    uto.save();

    return redirect("/clubs/"+str(org_id));

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

