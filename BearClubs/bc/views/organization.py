from django.shortcuts import render, redirect
from django.contrib import auth
from django.core.context_processors import csrf

from BearClubs.bc.forms.user import UserSignUpForm
from BearClubs.bc.models.organization import Organization

def directory(request):
    first_50_clubs = [];

    first_50_clubs = Organization.objects.all()[:50];
    # get 50 clubs here

    return render(request, 'directory.html' {'clubs': first_50_clubs});
