from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.core.context_processors import csrf

from BearClubs.bc.forms.organization import AddClubForm
from BearClubs.bc.models.organization import Organization

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
            form.save();

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
