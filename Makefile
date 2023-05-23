.PHONY: start
start:
	uvicorn src.main:app --reload --port 8000
.PHONY: format
format:
	black .
	isort .