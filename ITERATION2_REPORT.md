Iteration 2 Report  
*4.2.14*  

# Difficulties
One difficulty faced in Iteration 2 was the setting up of dependencies in order to get search working. The search team decided to go with ElasticSearch for BearClub's search engine, which requires its own server running. Team members that were not in the search team had trouble setting up all the dependencies related to search which resulted in a broken unit tests and the inoperability of `manage.py` commands. We managed to solve this difficulty by having the search team clearly document the steps required to setup the ElasticSearch engine and it's dependencies.

# Features
Most features planned for Iteration 2 were implemented.

# Tests
We utilized the Django unittest class for all of our unit testing needs. 

We added unit and end-to-end testing of Haystack, a django search API that connected to our ElasticSearch engine.

# Coverage Report

Our coverage report, courtesy of `coverage.py`, is available at `/ITERATION2_COVERAGE.txt` and `/htmlcov/BearClubs...` in our repository.
