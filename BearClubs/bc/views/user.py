from django.shortcuts import render, redirect
from django.contrib import auth
from django.core.context_processors import csrf
from BearClubs.bc.forms.user import UserSignUpForm, UserSignInForm

def userSignUp(request):
	if request.method == 'POST':
		form = UserSignUpForm(request.POST)
		if form.is_valid():
			# return successful registration, should login user and redirect to club directory
			user = form.save()
			auth.login(request, user)
			return render(request, 'index.html')
		else:
			# find out which fields were invalid and return error
			return userFormsRender(request, signUpForm=form)
			
	else:
		if (request.user.is_authenticated()):
			# if user is already authenticated then redirect to club directory
			return render(request, 'index.html')
		else:
			return userFormsRender(request)

def userSignIn(request):
	if request.method == 'POST':
		form = UserSignInForm(data=request.POST);

		if form.is_valid():
			form.loginUser(request);

			# On successful authentication, redirect to club directory
			return render(request, 'index.html');
		else:
			# On unsuccessful authentication, return error
			return userFormsRender(request, signInForm=form);
	else:
		if (request.user.is_authenticated()):
			# if user is already authenticated then redirect to club directory
			return render(request, 'index.html')
		else:
			return userFormsRender(request);

def userLogOut(request):
	auth.logout(request)
	return render(request, 'index.html')

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
