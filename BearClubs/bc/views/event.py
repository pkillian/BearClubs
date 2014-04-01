from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.core.context_processors import csrf

from BearClubs.bc.forms.event import AddEventForm

@login_required(login_url='/login')
def addEvent(request):
    args = {};

    # if it's a POST, add the event
    if request.POST:
        # get post data
        form = AddEventForm(request.user, request.POST);

        # check if form is valid
        if form.is_valid():
            # add the event
            form.save();

            # go to home
            return redirect('/');
        
        # if form is invalid, return it to the user
        else:
            return render(request, 'addEvent.html', {'form': form});

    # else, show a new addEvent form
    else:
        args.update(csrf(request));
        args['form'] = AddEventForm(request.user);
        return render(request, 'addEvent.html', args);
