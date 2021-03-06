Iteration 1 Report  
*3.14.14*  

# Difficulties

There were 2 main difficulties that our team has faced so far through Iteration 1.  The first difficulty was coordinating tasks between our team. There were certain dependencies that our team needed to rely on in order to function. For instance, the sign in and sign up team would be touching the same model, so it was imperative that we lay down the foundation of the model so neither team would have to depend on the other. Another instance this was making sure that signed in users had the privilege of adding a new club. This required coordination between the club team and the sign in team because the sign in team had to add checks to ensure that this worked. The next difficulty was testing our code. Towards the end, the sign in team ran into issues testing their login functionality since we used Django’s built-in authentication process for this. By doing so, there were a couple quirks/kinks that we could not iron out in time for iteration 1. After this, the issue with testing was ensuring that we thought of every possible edge case to cover. This took a while because there were couple guidelines that we needed to agree to as a team – max password length, max username length, minimum length for both, etc.

# Features

For the most part, we believe we implemented every feature as planned. In our design doc for Iteration 1 we made sure that we wanted 3 basic features to be implemented: sign in, sign up, and club directory. For iteration 1, we created a basic template in which a new user could either sign up or sign in. From there, the user can then view directories of the clubs listed on BearClubs or add a new club. We believe that this went as planned.

# Tests

We utilized the Django unittest class for all of our unit testing needs. We prepared extensive testing of the sign up and sign in process. We realize that User Experience is very important, and we wanted to make sure that the sign up and sign in flows were both intuitive and simple to use. Because of this, we did some extensive testing in the sign up flow to ensure that the User model would not break given invalid input. The tests we wrote for the sign up flow essentially cover every possible test case that a user could input. For instance, signing in with duplicate usernames, signing with blank passwords/emails/usernames, and submitting an invalid email address. The sign in tests were a bit trickier since we were using Django’s built in authentication system. By doing so, it was a little tricky in terms of testing because our team wasn’t well acquainted with a lot of the errors we were running into while testing the auth system. Our tests here deviated as we could only get one test functional. However, we believe that since we’re using a built-in system, the system should be stable and error-prone for the most part. Finally, we tested the club system. We tested adding clubs via the Django Club Form we built. In addition, we tested that the models accepted valid inputs only and did not crash if given invalid inputs. We did not test the views for the clubs because its very minimal. 

# Coverage Report

Our coverage report, courtesy of `coverage.py`, is at `/htmlcov/BearClubs...` in our repository.

