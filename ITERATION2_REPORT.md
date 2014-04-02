Iteration 2 Report  
*4.2.14*  

# Difficulties
One difficulty faced in Iteration 2 was the setting up of dependencies in order to get search working. The search team decided to go with ElasticSearch for BearClub's search engine, which requires its own server running. Team members that were not in the search team had trouble setting up all the dependencies related to search which resulted in a broken unit tests and the inoperability of `manage.py`commands. We managed to solve this difficulty by having the search team clearly document the steps required to setup the ElasticSearch engine and it's dependencies.

Another difficulty faced in Iteration 2 was implementing the ability to add Events. Since each event is associated with an organization, there was a dependency between the Event team and the Organization team. The Organization team was responsible for implementing promotion of users to admin and the ability for users to join a club. Ideally, a user can only add an event for an Organization if he or she is an admin from that organization. Furthermore, the Events team faced another hurdle when trying to figure out how to parse Date Time objects in the Add Event Form. At first, we used a widget - django-datetime-widget - to help create a clean UI that allowed users to easily enter a date and time for their event. However, when it came to testing, the Events team found that unit testing widgets is very buggy in Django, and thus we could not unit-test properly. Because of this, we decided to not go the widget route and instead created a specific format for the users input. We hope to figure out a better UI for this in future iterations, but this works for now.

# Features
All features planned for Iteration 2 were implemented.

# Tests
We utilized the Django unittest class for all of our unit testing needs. We also utilized Django's test client for performing end-to-end (functional/implementation) tests.

We added unit and end-to-end testing of Haystack (a Django search API that connected to our ElasticSearch engine), unit and end-to-end testing of the user dashboards and profiles, and end-to-end testing of the add event workflow.

We also added unit-tests for full functionality of adding events. We have functional tests for events as well.

# Coverage Report

Our coverage report, courtesy of `coverage.py`, is available at `/ITERATION2_COVERAGE.txt` and `/htmlcov/BearClubs...` in our repository.
