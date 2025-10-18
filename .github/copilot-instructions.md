<!-- .github/copilot-instructions.md -->
# Guidance for AI coding agents working on this repository

This repository is a minimal Python package used for examples and tests. The instructions below capture the small-but-important conventions and workflows agents should follow when authoring, editing, or testing code here.

## Big picture
- Project contains a small package located in the `src/` directory (this `src` is a Python package, not the conventional "source root" layout). Key files:
  - `src/features.py` — core functions (e.g. `add`, `sub`).
  - `src/__init__.py` — exposes package exports (`__all__ = ['add','sub']`).
  - `tests/test_features.py` — pytest tests importing `src.features`.
- Packaging uses setuptools configured in `pyproject.toml`. `pyproject.toml` uses `setuptools.build_meta` and packages are discovered with `where = ["."]` and `include = ["src*"]`, which packages the `src` directory as the top-level package name `src`.

## Import / package conventions (critical)
- The package is named `src` (literal). Tests import with `from src.features import add, sub` so do not change import paths to a different package name.
- When adding public API surface, update `src/__init__.py` and keep `__all__` in sync.
- Do not assume a `ci_cd` import package — the repository name and the installed package name differ here.

## Tests and developer workflows
- Tests are run with pytest. From the project root run:

  ```powershell
  pytest -q
  ```

- Run a single test or function for fast feedback (example):

  ```powershell
  pytest tests/test_features.py::test_add -q
  ```

- To install runtime/test deps locally:

  ```powershell
  pip install -r requirements.txt
  ```

- To install the package in editable mode (so imports behave the same as in tests):

  ```powershell
  pip install -e .
  ```

## Patterns and code style in this repo
- Code is plain Python (no type hints, no dataclasses, no logging). Keep edits consistent with this simple style unless adding a broader refactor.
- Functions are small and pure (e.g. `add(a,b)` returns `a + b`). Prefer small, well-tested changes.
- Tests import concrete module paths (not via relative imports). When renaming modules, update tests accordingly.

## Packaging and CI notes
- Packaging is configured via `pyproject.toml` + setuptools. Because `build` is not listed as a dev dependency here, only use packaging commands if you also add `build` / `wheel` to `requirements-dev` or install them locally. Example (optional):

  ```powershell
  pip install build wheel
  python -m build
  ```

- There are no CI workflows in the repository. If you add GitHub Actions, ensure the test job sets the working directory to the repo root and uses Python to run `pytest`.

## Integration and external dependencies
- The only declared dependency is `pytest` (see `requirements.txt`). There are no external services or network integrations to mock.

## Agent-specific tips (do these when editing code)
- Run tests locally before submitting changes. The test suite is the single source of truth for behavior.
- Respect the `src` package name and existing imports — changing package layout will break tests and packaging.
- When adding functions intended to be public, add them to `src/__init__.py` and update `__all__`.
- Keep edits minimal and add or update tests in `tests/` for any functional change; mirror the existing simple test style.

## Files to inspect for context
- `pyproject.toml` — packaging config.
- `requirements.txt` — runtime/test deps.
- `src/features.py` and `src/__init__.py` — core logic and exports.
- `tests/test_features.py` — canonical test examples.

If anything in this file is unclear or you want the agent guidance to cover additional workflows (formatting, linting, or CI templates), tell me what to add and I will iterate.
