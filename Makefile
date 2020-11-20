#!make
	
define USAGE
Commands:
    clean                       Remove all generated files           
    clean-pyc                   Remove compiled bytecode of source files
    clean-build                 Remove built packages
    format                      Formats the code
    generate-changelog          Generates the Changelog.md file
    install                     Install pipenv, dependencies and package with editable mode
    install-dev                 Install pipenv, development dependencies and package with editable mode
    install-pipenv              Install pipenv to manage Python dependencies
    lint                        Run linter
    test                        Run tests and validate project
    update-patch-version        Increase current patch version
    update-minor-version        Increase current minor version
    update-major-version        Increase current major version
    validate                    Validate with linter and formatter
    validate-formatting         Validates if the formating is correct
endef

export USAGE

TEST := -test

help:
	@echo "$$USAGE"

build:
	@pipenv run python setup.py sdist bdist_wheel

install: install-pipenv
	@pipenv install 
	@pipenv run pip install -e .

install-dev: install-pipenv	
	@pipenv install 
	@pipenv install --dev
	@pipenv run pip install -e .

install-pipenv:
	@pip install pipenv

test: validate
	@pipenv run python -m pytest -vv

generate-changelog:
	@git-changelog . -s angular -o CHANGELOG.md

format: 
	@pipenv run isort -rc .
	@pipenv run black .

validate: validate-formating lint

validate-formating: 
	@pipenv run black --check --diff .

lint:
	@pipenv run flake8 --count	

clean: clean-pyc clean-build

clean-pyc:
	@find . -name '*.pyc' -exec rm -f {} +
	@find . -name '*.pyo' -exec rm -f {} +
	@find . -name '*~' -exec rm -f {} +
	@find . -name '__pycache__' -exec rm -fr {} +
	@find . -name '.pytest_cache' -exec rm -fr {} +

clean-build:
	@rm -rf dist build .eggs checkarg.egg-info

update-patch-version:
	@pipenv run bump2version patch setup.py

update-minor-version:
	@pipenv run bump2version minor setup.py

update-major-version:
	@pipenv run bump2version major setup.py
