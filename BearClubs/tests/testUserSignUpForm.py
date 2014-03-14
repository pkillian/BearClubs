from django.test import TestCase
from BearClubs.bc.forms import UserSignUpForm
from BearClubs.bc.models import User

from django.utils import unittest
from django.utils.unittest import TestLoader, TextTestRunner
from cStringIO import StringIO

class UserSignUpFormUnitTests(TestCase):

	def setUp(self):
		#User.objects.all().delete()
		pass

	def testNewUser(self):
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

	def testDuplicateUsername(self):
		"""
		Test that creating a user with an existing username errors
		"""
		try:
			if User.objects.get(username="newuser"):
				User.objects.get(username="newuser").delete()
		except:
			pass

		u = User(username="newuser", email="new@email.com", password='pw1')
		u.save()

		form_data = {'username': 'newuser', 'email': 'new2@email.com', 'password1':'pw2', 'password2': 'pw2'}
		form = UserSignUpForm(data=form_data)

		self.assertFalse(form.is_valid())

		#check errors
		self.assertEqual(['username'], form.errors.keys())
		self.assertTrue('A user with that username already exists.' in form.errors.get('username'))

	def testEmptyUsername(self):
		"""
		Test that you can't create user with empty username; must fill out username field
		"""
		form_data = {'username': '', 'email': 'new2@email.com', 'password1':'pw1', 'password2': 'pw1'}
		form = UserSignUpForm(data=form_data)

		self.assertFalse(form.is_valid())

		self.assertEqual(['username'], form.errors.keys())
		self.assertTrue('This field is required.' in form.errors.get('username'))

	def testEmptyEmail(self):
		"""
		Test that you can't create user with empty email; must fill out email field
		"""
		try:
			if User.objects.get(username="newuser"):
				User.objects.get(username="newuser").delete()
		except:
			pass

		form_data = {'username': 'newuser', 'email': '', 'password1':'pw1', 'password2': 'pw1'}
		form = UserSignUpForm(data=form_data)

		self.assertFalse(form.is_valid())

		self.assertEqual(['email'], form.errors.keys())
		self.assertTrue('This field is required.' in form.errors.get('email'))

	def testEmptyPassword1(self):
		"""
		Test that you can't create user with empty password; must fill out password field
		"""
		try:
			if User.objects.get(username="newuser"):
				User.objects.get(username="newuser").delete()
		except:
			pass

		form_data = {'username': 'newuser', 'email': 'new2@email.com', 'password1':'', 'password2': 'pw1'}
		form = UserSignUpForm(data=form_data)

		self.assertFalse(form.is_valid())

		self.assertEqual(['password1'], form.errors.keys())
		self.assertTrue('This field is required.' in form.errors.get('password1'))

	def testEmptyPassword2(self):
		"""
		Test that you can't create user with empty confirm password; must fill out confirm password field
		"""
		try:
			if User.objects.get(username="newuser"):
				User.objects.get(username="newuser").delete()
		except:
			pass

		form_data = {'username': 'newuser', 'email': 'new2@email.com', 'password1':'pw1', 'password2': ''}
		form = UserSignUpForm(data=form_data)

		self.assertFalse(form.is_valid())

		self.assertEqual(['password2'], form.errors.keys())
		self.assertTrue('This field is required.' in form.errors.get('password2'))

	def testInvalidEmail(self):
		"""
		Test that email must be valid email that needs to include the '@' sign; if not, error
		"""
		try:
			if User.objects.get(username="newuser"):
				User.objects.get(username="newuser").delete()
		except:
			pass
		form_data = {'username': 'newuser', 'email': 'emailtest', 'password1':'pw1', 'password2': 'pw1'}
		form = UserSignUpForm(data=form_data)

		self.assertFalse(form.is_valid())

		self.assertEqual(['email'], form.errors.keys())
		self.assertTrue('Enter a valid email address.' in form.errors.get('email'))

	def testInvalidEmail2(self):
		"""
		Test that email must be valid email that needs to include a domain after "@" sign; if not, error
		"""
		try:
			if User.objects.get(username="newuser"):
				User.objects.get(username="newuser").delete()
		except:
			pass
		form_data = {'username': 'newuser', 'email': 'emailtest@', 'password1':'pw1', 'password2': 'pw1'}
		form = UserSignUpForm(data=form_data)

		self.assertFalse(form.is_valid())

		self.assertEqual(['email'], form.errors.keys())
		self.assertTrue('Enter a valid email address.' in form.errors.get('email'))

	def testUnmatchedPasswords(self):
		"""
		Tests that password (password1) and confirm password (password2) should error if not the same
		"""
		try:
			if User.objects.get(username="newuser"):
				User.objects.get(username="newuser").delete()
		except:
			pass
		form_data = {'username': 'newuser', 'email': 'new2@email.com', 'password1':'pw1', 'password2': 'pw2'}
		form = UserSignUpForm(data=form_data)

		self.assertFalse(form.is_valid())

		self.assertEqual(['password2'], form.errors.keys())
		self.assertTrue("The two password fields didn't match." in form.errors.get('password2'))
	
	
	# Other cases:
	# - multiple errors in one form
	# - length of fields; over 128? charcters
	# - valid numbers and characters; no spaces, !, /, etc.
	# - adding many users


# If this file is invoked as a Python script, run the tests in this module
if __name__ == "__main__":
	# Add a verbose argument
	sys.argv = [sys.argv[0]] + ["-v"] + sys.argv[1:]
	unittest.main()
