.PHONY: install format lint test test-watch

all: install

install:
	/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
	curl -sSL https://install.python-poetry.org | python3 -
	poetry install
	poetry run pre-commit install

pyenv:
	brew install pyenv
	pyenv install

format:
	poetry run pre-commit run --all-files

lint:
	poetry run pylint chess/

test:
	poetry run pytest --cov=chess

test-watch:
	poetry run ptw

run-pre-commit:
	pre-commit run --all-files

run-solution:
	poetry run python chess/solution.py > test.txt
