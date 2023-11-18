.DEFAULT_GOAL: help

help:
	@echo "Available commands:"
	@echo
	@fgrep -h "##" $(MAKEFILE_LIST) | fgrep -v fgrep | sed -e 's/\\$$//' | sed -e 's/##//'

build: ## Build the docker images
	docker compose build

dev:  ## Start the API, DB, client and cap generator in development mode.
	docker compose up -d && docker compose logs -f

prod: ## Start the API in prod mode
	docker run --name summarizer -e PORT=8765 -e DATABASE_URL=sqlite://sqlite.db -p 5003:8765 ghcr.io/daniel-ibarrola/summarizer/summarizer:latest

test:  ## Run all tests
	docker compose exec web python -m pytest

test-coverage: ## Run tests with coverage
	docker compose exec web python -m pytest --cov="."

lint: ## Lint the code
	docker compose exec web flake8 src/

format-check:  ## Check code formatting
	docker compose exec web black src/ --check

format-diff: ## Check diff of code formatting
	docker compose exec web black src/ --diff

format: ## Format the code
	docker compose exec web black src/

sort-imports: ## Sort imports in code files:
	docker compose exec web isort src/
