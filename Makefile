.PHONY: deploy install install-dev lint test test-all type-check

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
