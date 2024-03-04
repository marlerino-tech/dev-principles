# Build configuration
# -------------------

APP_NAME := "example-project"
APP_VERSION := "1.0.0"
GIT_REVISION = `git rev-parse HEAD`

# Introspection targets
# ---------------------

.PHONY: help
help: header targets

.PHONY: header
header:
	@echo "\033[34mEnvironment\033[0m"
	@echo "\033[34m---------------------------------------------------------------\033[0m"
	@printf "\033[33m%-23s\033[0m" "APP_NAME"
	@printf "\033[35m%s\033[0m" $(APP_NAME)
	@echo ""
	@printf "\033[33m%-23s\033[0m" "APP_VERSION"
	@printf "\033[35m%s\033[0m" $(APP_VERSION)
	@echo ""
	@printf "\033[33m%-23s\033[0m" "GIT_REVISION"
	@printf "\033[35m%s\033[0m" $(GIT_REVISION)
	@echo "\n"

.PHONY: targets
targets:
	@echo "\033[34mDevelopment Targets\033[0m"
	@echo "\033[34m---------------------------------------------------------------\033[0m"
	@perl -nle'print $& if m{^[a-zA-Z_-]+:.*?## .*$$}' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-22s\033[0m %s\n", $$1, $$2}'

# Development targets
# -------------

.PHONY: sync
sync: ## Install dependencies
	pipenv sync

.PHONY: start
start: ## Starts the server
	uvicorn core.server:app --reload --host 127.0.0.1 --port 8888

.PHONY: start_deploy
start_deploy: ## Starts the server
	gunicorn core.server:app --workers $(WORKERS) --worker-class uvicorn.workers.UvicornWorker --bind 0.0.0.0:$(PORT)

docker_start:
	docker compose down
	docker compose build
	docker compose up -d

docker_up:
	docker compose up -d

docker_down:
	docker compose down

docker_ps:
	docker compose ps

docker_clear_all:
	docker system prune -a

docker_clear_images:
	docker image prune -a

# Check, lint and format targets
# ------------------------------

.PHONY: check
check: check-format lint

.PHONY: check-format
check-format: ## Dry-run code formatter
	pipenv run black ./ --check
	pipenv run isort ./ --profile black --check

.PHONY: lint
lint: ## Run linter
	pipenv run pylint ./api ./app ./core

.PHONY: format
format: ## Run code formatter
	pipenv run black ./
	pipenv run isort ./ --profile black