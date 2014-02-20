#
# A number of make targets to simpligy testing and setup tasks
#

# Default target: run all the tests
.PHONY: all_tests
all_tests ::

# Run the unit tests
.PHONY: unit_tests
unit_tests: 
	@echo "\n=======  Running unit tests =========\n"
	python manage.py test

all_tests :: unit_tests

# Run the functional tests
# The functional tests are discovered by scanning files that start with test... for unittest.TestCase subclasses
.PHONY: func_tests
func_tests:
	@echo "\n======= Running functional tests ======\n"
	python -m unittest discover -p 'test[A-Z]*.py' -v $(TESTARGS)

all_tests :: func_tests

###
### HEROKU DEPLOYMENT
###
### Read README for some deployment details
###
start_local: 
	foreman start -f Procfile.dev

HEROKU_STAGE_APP=bearclubs-stage
HEROKU_PROD_APP=bearclubs-prod

deploy_heroku_stage:
	git push heroku-stage HEAD:master

deploy_heroku_prod:
	git push heroku-prod master

heroku_logs_stage:
	heroku logs -t --app $(HEROKU_STAGE_APP)

heroku_logs_prod:
	heroku logs -t --app $(HEROKU_PROD_APP)

