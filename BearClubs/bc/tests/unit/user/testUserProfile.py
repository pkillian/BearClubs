from cStringIO import StringIO

from django.test import TestCase
from django.utils import unittest

from BearClubs.bc.models import User

class UserProfileTests(TestCase):

    def setUp(self):
        #User.objects.all().delete()
        pass

    def testSuccessfulProfileLoad(self):
        return True;


# If this file is invoked as a Python script, run the tests in this module
if __name__ == "__main__":
    # Add a verbose argument
    sys.argv = [sys.argv[0]] + ["-v"] + sys.argv[1:]
    unittest.main()
