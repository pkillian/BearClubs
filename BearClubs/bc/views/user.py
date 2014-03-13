from django.shortcuts import render, redirect
from django.contrib import auth
from django.core.context_processors import csrf
from BearClubs.bc.forms.user import UserSignUpForm

def userSignUp(request):
	args = {};

	if request.method == 'POST':
		form = UserSignUpForm(request.POST);
		if form.is_valid():
			# return successful registration, should login user and redirect to club directory
			form.save();
			return render(request, 'index.html');
		else:
			# find out which fields were invalid and return error
			args['signup_form'] = form;
			return render(request, 'signup.html', args);
	else:
		args.update(csrf(request));
		args['signup_form'] = UserSignUpForm();
		return render(request, 'signup.html', args);
