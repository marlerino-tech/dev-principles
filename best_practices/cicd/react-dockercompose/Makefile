# Build configuration
# -------------------

PROJECT_NAME := react-template
PROJECT_VERSION := 0.1.0
DOCKER_USERNAME := begenfmg
GIT_REVISION = `git rev-parse HEAD`

# Introspection targets
# ---------------------

.PHONY: help
help: header targets

.PHONY: header
header:
	@echo "\033[34mEnvironment\033[0m"
	@echo "\033[34m---------------------------------------------------------------\033[0m"
	@printf "\033[33m%-23s\033[0m" "PROJECT_NAME"
	@printf "\033[35m%s\033[0m" $(PROJECT_NAME)
	@echo ""
	@printf "\033[33m%-23s\033[0m" "PROJECT_VERSION"
	@printf "\033[35m%s\033[0m" $(PROJECT_VERSION)
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
	sudo npm install

.PHONY: start
start: ## Starts the dev server
	sudo npm run dev

.PHONY: build
build:  ## Build production version
	sudo npm run build

# Check, lint and format targets
# ------------------------------
.PHONY: lint
lint: ## Run linter
	sudo npm run lint

.PHONY: format
format: ## Run code formatter
	sudo npm run lint:fix
	sudo npm run format

.PHONE: check-types
check-types: ## Check types
	sudo npm run type-check

.PHONE: setup-precommit
setup-precommit: ## Install all hooks
	pre-commit install

.PHONE: check-precommit
check-precommit: ## Check
	pre-commit run --all-files

# Docker and Docker-compose
# -------------
docker-setup-prod: ## Create all needs docker stuff
	docker network ls | grep -q react-template-net || docker network create react-template-net

docker-setup-test: ## Create all needs docker stuff
	docker network ls | grep -q react-template-test || docker network create react-template-test


docker-build-prod: ## Build prod image
	docker build -t $(DOCKER_USERNAME)/$(PROJECT_NAME):latest -t $(DOCKER_USERNAME)/$(PROJECT_NAME):$(PROJECT_VERSION) .

docker-build-test: ## Build test image
	docker build -t $(DOCKER_USERNAME)/$(PROJECT_NAME):test -t $(DOCKER_USERNAME)/$(PROJECT_NAME):$(PROJECT_VERSION)-test .

docker-push: ## Push prod images
	docker push $(DOCKER_USERNAME)/$(PROJECT_NAME):latest
	docker push $(DOCKER_USERNAME)/$(PROJECT_NAME):$(PROJECT_VERSION)

dc-pull: ## Pull actual images
	docker compose pull

dc-down: ## Stop prod docker-compose
	docker-compose down

dc-up: ## Start prod docker-compose
	docker-compose up -d

dc-start-prod: docker-setup-prod dc-pull dc-down dc-up ## Start prod docker-compose

dc-start-test:
	docker compose -f ./docker-compose.test.yaml down
	make docker-setup-test
	make docker-build-test # можно использовать docker-compose -f ./docker-compose.test.yaml pull
	docker compose -f ./docker-compose.test.yaml up -d

dc-rm-test:
	docker compose -f ./docker-compose.test.yaml rm -s -v -f


dc-ps: ## Ps docker-compose
	docker compose ps

dc-logs: ## Show docker-compose logs
	docker compose logs -f

dc-logs-test: ## Show docker-compose logs
	docker compose -f ./docker-compose.test.yaml logs -f


docker-clear-all: ## Clear all system cache
	docker system prune -a

docker-clear-images: ## Clear all image cache
	docker image prune -a
