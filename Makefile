.PHONY: lint
lint:
	ruff check --exit-zero .

.PHONY: format
format:
	ruff check --fix .
	ruff format .

.PHONY: pre-commit
pre-commit:
	pre-commit run --all-files
