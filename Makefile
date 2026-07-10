install:
	uv sync

brain-games:
	uv run brain-games

build:
	uv build

package-install:
	uv tool install dist/*.whl

package-reinstall:
	uv tool install --force dist/*.whl

lint:
	uv run ruff check brain_games

test:
	uv run pytest

.PHONY: install build lint check test
