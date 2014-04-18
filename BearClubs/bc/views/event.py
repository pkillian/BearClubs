from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.core.context_processors import csrf
from django.core.exceptions import ValidationError

from BearClubs.bc.forms.event import AddEventForm
from BearClubs.bc.models.mappings.user import UserToEvent
from BearClubs.bc.models.event import Event
from BearClubs.bc.models.user import User

def eventProfile(request, event_id):
    args = {}
    
    user = None;
    event = Event.objects.get(id=event_id);

    if request.user.is_authenticated():
        user = User.objects.get(id=request.user.id);
        
        if UserToEvent.userSubscribedToEvent(user=request.user, event=event):
            args['subscribed'] = True;

    args['event'] = event;

    return render(request, 'eventProfile.html', args);

def eventDirectory(request):
    total_events = Event.objects.count();
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
    max_page = Event.getMaxPage(increment);

    # order the clubs, then slice the list
    view_args['events']     = Event.getEventsByPage(page, increment);
    view_args['max_page']   = max_page;
    view_args['page']       = page;
    view_args['increment']  = increment;

    return render(request, 'eventDirectory.html', view_args);

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
            form.save()

            # go to home
            return redirect('/events');
        
        # if form is invalid, return it to the user
        else:
            return render(request, 'addEvent.html', {'form': form});

    # else, show a new addEvent form
    else:
        args.update(csrf(request));
        args['form'] = AddEventForm(request.user);
        return render(request, 'addEvent.html', args);

@login_required(login_url='/login')
def subscribe(request):
    args = {};
    event_id = None;

    if request.POST:
        user = User.objects.get(id=request.user.id);
        
        event_id = request.POST['event_id'];
        event = Event.objects.get(id=event_id);

        ute = UserToEvent(user=user, event=event);
        ute.save();

    else:
        return eventDirectory(request);

    return eventProfile(request, event_id);

@login_required(login_url='/login')
def unsubscribe(request):
    args = {};
    event_id = None;

    if request.POST:
        user = User.objects.get(id=request.user.id);

        event_id = request.POST['event_id'];
        event = Event.objects.get(id=event_id);

        ute = UserToEvent.objects.get(user=user, event=event);
        ute.delete();

    else:
        return eventDirectory(request);

    return eventProfile(request, event_id);
