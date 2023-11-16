.DEFAULT_GOAL: help

help:
	@echo "Available commands:"
	@echo
	@fgrep -h "##" $(MAKEFILE_LIST) | fgrep -v fgrep | sed -e 's/\\$$//' | sed -e 's/##//'

build: ## Build the docker images
	docker compose build

dev:  ## Start the API, DB, client and cap generator in development mode.
	docker compose up -d && docker compose logs -f

test:  ## Run all tests
	docker compose exec web python -m pytest
