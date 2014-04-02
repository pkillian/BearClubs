# Contributing Guidelines

## Setting up ElasticSearch in your Local Environment

On Mac OS X...
brew install elasticsearch

On Ubuntu...
apt-get install elasticsearch

Then start via:
elasticsearch -f -D es.config=<path to YAML config>

Example:
elasticsearch -f -D es.config=/usr/local/Cellar/elasticsearch/0.90.0/config/elasticsearch.yml
