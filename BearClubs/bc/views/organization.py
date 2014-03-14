from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.core.context_processors import csrf

from BearClubs.bc.forms.organization import AddClubForm
from BearClubs.bc.models.organization import Organization

def directory(request):
    first_50_clubs = [];

    first_50_clubs = Organization.objects.all()[:50];
    # get 50 clubs here

    return render(request, 'directory.html', {'clubs': first_50_clubs});

@login_required(login_url='/login')
def addClub(request):
    args = {};

    if request.POST:
        # get post data
        form = AddClubForm(request, request.POST);

        # check if form is valid
        if form.is_valid():
            # add the club
            form.save();

            # go to directory
            return redirect('/clubs');
        
        # if form is invalid, return it to the user
        else:
            return render(request, 'addClub.html', {'form': form});

    else:
        args.update(csrf(request));
        args['form'] = AddClubForm(request);
        return render(request, 'addClub.html', args);
