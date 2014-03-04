# A simple-minded makefile that just calls the one in the outer source
# directory.

.PHONY: default clean
.PHONY: all_tests unit_tests func_tests grunt grunt_quick
.PHONY: start_local deploy_heroku_stage deploy_heroku_prod
.PHONY: heroku_logs_stage heroku_logs_prod

default:
	$(MAKE) -C .. default

clean:
	$(MAKE) -C .. clean

all_tests:
	$(MAKE) -C .. all_tests

unit_tests:
	$(MAKE) -C .. unit_tests

func_tests:
	$(MAKE) -C .. func_tests

grunt:
	$(MAKE) -C .. grunt

grunt_quick:
	$(MAKE) -C .. grunt_quick

start_local:
	$(MAKE) -C .. start_local

deploy_heroku_stage:
	$(MAKE) -C .. deploy_heroku_stage

deploy_heroku_prod:
	$(MAKE) -C .. deploy_heroku_prod

heroku_logs_stage:
	$(MAKE) -C .. heroku_logs_stage

heroku_logs_prod:
	$(MAKE) -C .. heroku_logs_prod

