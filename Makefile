.PHONY: install format lint test test-watch

all: install

install:
	curl -sSL https://install.python-poetry.org | python3 -
	poetry install
	poetry run pre-commit install

format:
	poetry run pre-commit run --all-files

lint:
	poetry run pylint chess/ tests/

test:
	poetry run pytest --cov=chess

test-watch:
	poetry run ptw
