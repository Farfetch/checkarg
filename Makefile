#!make
	
define USAGE
Commands:
    clean                       Remove all generated files           
    clean-pyc                   Remove compiled bytecode of source files
    format                      Formats the code
    generate-changelog          Generates the Changelog.md file
    install                     Install pipenv, dependencies and package with editable mode
    install-dev                 Install pipenv, development dependencies and package with editable mode
    install-pipenv              Install pipenv to manage Python dependencies
    lint                        Run linter
	test                        Run tests, linter and formatter
    validate-formatting         Validates if the formating is correct
endef

export USAGE

TEST := -test

help:
	@echo "$$USAGE"

install: install-pipenv
	@pipenv install 
	@pipenv run pip install -e .

install-dev: install-pipenv	
	@pipenv install 
	@pipenv install --dev
	@pipenv run pip install -e .

install-pipenv:
	@pip install pipenv

test: validate-formating lint
	@pipenv run python -m pytest -vv

generate-changelog:
	@git-changelog . -s angular -o CHANGELOG.md

validate-formating: 
	@pipenv run black --check --diff .

format: 
	@pipenv run isort -rc .
	@pipenv run black .

lint:
	@pipenv run flake8 --count	

clean: clean-pyc

clean-pyc:
	@find . -name '*.pyc' -exec rm -f {} +
	@find . -name '*.pyo' -exec rm -f {} +
	@find . -name '*~' -exec rm -f {} +
	@find . -name '__pycache__' -exec rm -fr {} +


