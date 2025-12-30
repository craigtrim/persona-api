install:
	poetry check
	poetry lock
	poetry update
	poetry install
	poetry run pip freeze > requirements.txt

test:
	poetry run pytest --disable-pytest-warnings

build:
	make install
#	make test
	poetry build

linters:
	poetry run pre-commit run --all-files
	poetry run ruff check persona_api

run:
	poetry run uvicorn persona_api:app --reload --port 8000

gen-facet-data:
	poetry run python scripts/gen_facet_data.py

all:
	make build
	make linters
	poetry run python -m pip install --upgrade pip
