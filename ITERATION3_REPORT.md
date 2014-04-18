Iteration 3 Report  
*4.18.14*  

# Difficulties
For the club team, the main diffulties we had were in deciding how to display the promoting member options. We decided to create a separate manage page that only admins can see to deal with promoting/demoting members. Since we moved the list of members and their admin options to the new manage page, we opted to show whether the logged-in user is a member or admin of the club or not on the club profile page after the club details.

For the event team, difficulties we had were with deciding how to restrict who can create events. We wanted only admins to be able to create events. Thus, we decided to only list organizations that the logged-in user is an admin for in the add event dialog. This way, if the logged-in user is not an admin for any club, they cannot select an organization, causing them to not be able to submit the form for lack of required organization.

# Features
All features planned for Iteration 3 were implemented. The club team also implemented the additional feature of demoting club admins to regular members.

# Tests
We utilized the Django unittest class for all of our unit testing needs. We also utilized Django's test client for performing end-to-end (functional/implementation) tests, and the Selenium WebDriver for our UI testing in combination with Firefox and PhantomJS browsers.

# Coverage Report

Our coverage report, courtesy of `coverage.py`, is available at `/ITERATION3_COVERAGE.txt` and `/htmlcov/BearClubs...` in our repository.
