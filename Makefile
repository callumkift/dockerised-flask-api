.PHONY: build-docker create-requirements create-requirements-dev deploy install install-dev lint test test-all type-check

build-docker:
	echo 'not implemented yet'

create-requirements:
	pipenv lock -r > requirements.txt

create-requirements-dev:
	pipenv lock -r --dev > requirements.txt

deploy:
	echo 'not implemented yet'

install:
	pipenv install

install-dev:
	pipenv install --dev

lint:
	pipenv run python3 -m flake8 src

test:
	pipenv run python3 -m pytest src

test-all: lint type-check test

type-check:
	pipenv run python3 -m mypy src
