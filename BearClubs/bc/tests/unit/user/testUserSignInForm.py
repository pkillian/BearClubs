from django.test import TestCase
from django.test.client import Client
from BearClubs.bc.forms.user import UserSignUpForm, UserSignInForm
from BearClubs.bc.models import User
from BearClubs.bc.views.user import userSignIn

from django.utils import unittest
from django.utils.unittest import TestLoader, TextTestRunner
from cStringIO import StringIO

class UserSignInFormUnitTests(TestCase):

	def setUp(self):
		pass

	def testLoginWithoutSignUp(self):
		"""
		Test that you can't login without first signing up
		"""
		try:
			if User.objects.get(username="newuser"):
				User.objects.get(username="newuser").delete()
		except:
			pass

		post_data = {'username': 'newuser', 'password':'pw'}
		
		response = Client().post('/login', {'username': 'newuser', 'password':'pw'})
		request = response.request

		form = UserSignInForm(data=request.POST)

		self.assertTrue(form.is_valid())

		self.assertEquals(400, response.status_code)

	def testLoginWithSignUp(self):
		"""
		Test that you can login after signing up
		"""
		# create user first
		try:
			if User.objects.get(username="newuser"):
				User.objects.get(username="newuser").delete()
		except:
			pass

		form_data = {'username': 'newuser', 'email': 'new@email.com', 'password1':'pw1', 'password2': 'pw1'}
		form = UserSignUpForm(data=form_data)

		self.assertTrue(form.is_valid())

		form.save()

		self.assertTrue(User.objects.get(username="newuser") in User.objects.all())

		u = User.objects.get(username="newuser")
		self.assertEquals(u.username, "newuser")
		self.assertEquals(u.email, "new@email.com")

		# login that user
		post_data = {'username': 'newuser', 'password':'pw'}

		response = Client().post('/login', post_data)
		self.assertEquals(200, response.status_code)
