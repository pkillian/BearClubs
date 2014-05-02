Iteration 4 Report  
*5.2.14*  

# Difficulties
In general, we had difficulties coming up with a coherent UI style for the event, user, and club profiles. We were going back and forth about how to display the information in a way that makes logical sense and looks pleasant. In the end, we came up with a style that displayed the data in a more meaningful way.

For the club team, the main difficulties were in getting the css/less correctly without affecting other pages. The other challenge was in deciding how to restrict an admin from demoting the only/last admin of the club. In the end, we decided to still display the demote button but show a message telling the admin that they can't demote the only admin of the club.

For the event team, the main difficulties were keeping the style consistent with the other profile pages. Now the profile displays the users name on the subscribed users list on the right as soon as the user clicks the subcscribe button.

The CalNet team had a variety of learning curves to adapt to, but the trickiest of all was attempting to test the CalNet authentication workflow. The CAS system prohibits automated logins, and it's seemingly impossible to spoof the proper request in order to test our views / static methods in our model.

# Features

## Additional features implemented:
 - Club Profile page displays members of the club on the right. 
 - Event profile page displays suscribed members to an event on the right. 

# Tests

We utilized the Django unittest class for all of our unit testing needs. We also utilized Django's test client for performing end-to-end (functional/implementation) tests, and the Selenium WebDriver for our UI testing in combination with Firefox and PhantomJS browsers.

Testing the CalNet login authentication is extremely tricky; it's impossible to automate due to the security features implemented by CAS, and it's also seemingly impossible to spoof a request and give our method's placeholder data without stripping their functionality.

# Coverage Report

Our coverage report, courtesy of `coverage.py`, is available at `/ITERATION4_COVERAGE.txt` and `/htmlcov/BearClubs...` in our repository.
