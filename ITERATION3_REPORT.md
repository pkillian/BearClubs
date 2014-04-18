Iteration 3 Report  
*4.18.14*  

# Difficulties
For the club team, the main difficulties we had were in deciding how to display the promoting member options. We decided to create a separate manage page that only admins can see to deal with promoting/demoting members. Since we moved the list of members and their admin options to the new manage page, we opted to show whether the logged-in user is a member or admin of the club or not on the club profile page after the club details.

For the event team, difficulties we had were with deciding how to restrict who can create events. We wanted only admins to be able to create events. Thus, we decided to only list organizations that the logged-in user is an admin for in the add event dialog. This way, if the logged-in user is not an admin for any club, they cannot select an organization, causing them to not be able to submit the form for lack of required organization.

The User team ran into a few difficulties like coordinating our efforts with the event team; this was only a minor setback as we had to wait for their event profile updates to be committed before adding our subscription functionality. We also ran into a bit of a hiccup when deciding if a user should be able to subscribe to a Club/Organization at all. Conceptually, only members of a club should need to be subscribed to all the club's information, so we decided to forgoe our original plan of supporting both member and non-member subscribers.

The UI team ran into little difficulty other than implementing Selenium testing. Selenium tests depend on a WebDriver (Firefox, Chrome, PhantomJS, etc.) and we ran into a bit of a speedbump while trying to convert our tests from a Firefox WebDriver to a PhantomJS WebDriver. In the end, we decided it was costing us too much time and left these tests implemented on Firefox's WebDriver for now. If testing speed becomes too much of an issue, we will reinvest the time and implement them on PhantomJS instead.

# Features
All features planned for Iteration 3 were implemented. The club team also implemented the additional feature of demoting club admins to regular members.

# Tests
We utilized the Django unittest class for all of our unit testing needs. We also utilized Django's test client for performing end-to-end (functional/implementation) tests, and the Selenium WebDriver for our UI testing in combination with Firefox and PhantomJS browsers.

# Coverage Report

Our coverage report, courtesy of `coverage.py`, is available at `/ITERATION3_COVERAGE.txt` and `/htmlcov/BearClubs...` in our repository.
