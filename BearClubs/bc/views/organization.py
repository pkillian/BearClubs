from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.core.context_processors import csrf

from BearClubs.bc.forms.organization import AddClubForm
from BearClubs.bc.models.organization import Organization
from BearClubs.bc.models.user import User
from BearClubs.bc.models.mappings import UserToOrganization

def __unicode__(self):
    return self.name;

def directory(request):
    total_clubs = Organization.objects.count();
    view_args = {};

    # get paging information from URL params
    page      = int(request.GET.get('page', '1'));
    increment = int(request.GET.get('inc', '50'));

    # prevent negatives
    if page <= 0:
        page = 1;

    # Bound increment values
    if increment <= 0:
        increment = 50;
    elif increment > 250:
        increment = 250;

    # set the max number of pages; (5 // 50) = 0;
    max_page = Organization.getMaxPage(increment);

    # order the clubs, then slice the list
    view_args['clubs']      = Organization.getClubsByPage(page, increment);
    view_args['max_page']   = max_page;
    view_args['page']       = page;
    view_args['increment']  = increment;

    return render(request, 'directory.html', view_args);

def clubProfile(request, organization_id):

    args = {}
    args['club'] = Organization.objects.get(id=organization_id);

    org = Organization.objects.get(id=organization_id);

    #filter out UserToOrganization entries that have members in this organization
    members = UserToOrganization.objects.filter(organization=org);
    args['members'] = members;

    if request.user.is_authenticated():
        user = User.objects.get(id=int(request.user.id));
        user.save();

        args['member'] = False;

        #check if logged-in user is a member of this organization already
        for member in members:
            if member.user.username == user.username:
                args['member'] = True;
                break;      #to account for the users that joined the club multiple times, but this should not happen anymore
            else:
                args['member'] = False;

        #check if current logged-in user is an admin for this organization
        for member in members:
            if member.user.username == user.username and member.admin == True:
                args['admin'] = True;
                break;      #to account for the users that joined the club multiple times, but this should not happen anymore
            else:
                args['admin'] = False;


    return render(request, 'clubProfile.html', args);

@login_required(login_url='/login')
def joinClub(request):
    if request.user.is_authenticated() and request.POST:
        organization_id = int(request.POST.get('organization_id','-1'));

        org = Organization.objects.get(id=organization_id);
        user = User.objects.get(id=request.user.id);

        uto = UserToOrganization(user=user, organization=org);

        uto.save();

    return redirect("/clubs/"+str(organization_id));

@login_required(login_url='/login')
def manage(request, organization_id):
    args = {};

    if request.user.is_authenticated():

        org = Organization.objects.get(id=organization_id);
        args['club'] = org;

        user = User.objects.get(id=request.user.id);
        
        members = UserToOrganization.objects.filter(organization=org);
        args['members'] = members;

        args['member'] = False;

        #check if logged-in user is a member of this organization already
        for member in members:
            if member.user.username == user.username:
                args['member'] = True;
                break;      #to account for the users that joined the club multiple times, but this should not happen anymore
            else:
                args['member'] = False;

        #check if current logged-in user is an admin for this organization
        for member in members:
            if member.user.username == user.username and member.admin == True:
                args['admin'] = True;
                break;      #to account for the users that joined the club multiple times, but this should not happen anymore
            else:
                args['admin'] = False;
    return render(request, 'manage.html', args);

@login_required(login_url='/login')
def addClub(request):
    args = {};

    # if it's a POST, add the club
    if request.POST:
        # get post data
        form = AddClubForm(request.user, request.POST);

        # check if form is valid
        if form.is_valid():
            # add the club
            org = form.save();

            # get club creator
            user = User.objects.get(id=request.user.id);

            # add club creator to club as admin
            uto = UserToOrganization(user=user, organization=org, admin=True);
            uto.save();

            # go to directory
            return redirect('/clubs');
        
        # if form is invalid, return it to the user
        else:
            return render(request, 'addClub.html', {'form': form});

    # else, show a new addClub form
    else:
        args.update(csrf(request));
        args['form'] = AddClubForm(request.user);
        return render(request, 'addClub.html', args);
