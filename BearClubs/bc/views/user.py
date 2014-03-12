from django.shortcuts import render
from django.contrib import auth
from django.core.context_processors import csrf
from BearClubs.bc.forms.user import UserSignUpForm

def userSignUp(request):
	if request.method == 'POST':
		form = UserSignUpForm(request.POST)
		if form.is_valid():
			form.save()
			return render(request, 'index.html')
			# return successful registration, should login user and redirect to club directory
		else:
			# find out which fields were invalid and return error
			args = {}
			args['form'] = form
			return render(request, 'signup.html', args)
	else:
		args = {}
		args.update(csrf(request))
		args['form'] = UserSignUpForm()
		return render(request, 'signup.html', args)
