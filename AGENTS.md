# Repository Guidelines

## Project Structure & Module Organization
The repository has two main parts. The thesis sources live at the root: `main.tex` assembles the document, `tex/capitulos/` stores chapter files, `tex/pretextuais/` holds front matter, `tex/config/` contains the ABNTeX class and style files, `figuras/` stores images, and `referencias.bib` is the bibliography database. The experimental code lives in `codigo/`: `src/` contains data, model, and training modules; `pipelines/flows/` and `pipelines/tasks/` define Prefect orchestration; `configs/` holds Hydra YAMLs; `tests/` contains pytest suites; `scripts/` and `analysis/` support operations and reporting; `data/` stores station spreadsheets.

## Build, Test, and Development Commands
Use a local LaTeX toolchain at the repository root, for example `latexmk -pdf main.tex`; if `latexmk` is unavailable, run `pdflatex main.tex`, `bibtex main`, then `pdflatex main.tex` twice. For the Python pipeline, `make -C codigo start-services` starts MLflow and Prefect, `make -C codigo start-worker` registers deployments and starts the local worker, `make -C codigo dry-run` launches the smoke deployment, and `make -C codigo quick-run-lstm-direct` runs the single debug configuration currently wired in the `Makefile`. Use `pytest codigo/tests -q` for tests and `make -C codigo clean` to remove runtime caches and logs.

## Coding Style & Naming Conventions
Python code follows PEP 8 conventions: 4-space indentation, `snake_case` for modules and functions, `PascalCase` for classes such as `DirectLSTMLightningModule`, and type hints when they clarify interfaces. Keep YAML config names lowercase and descriptive, for example `quick_run_lstm_direct.yaml`. LaTeX chapter files use numeric prefixes like `cap_04_metodologia.tex`; figure filenames are lowercase with hyphens. No formatter or linter config is committed here, so avoid large cosmetic rewrites and keep imports grouped consistently.

## Testing Guidelines
Tests are pytest-based and live in `codigo/tests/`. Name new files `test_*.py` and prefer focused smoke or regression tests around data leakage, dataset shapes, and model forward passes. No coverage threshold is enforced in this checkout, but any change in `codigo/src/` or `codigo/pipelines/` should include tests or a short justification in the PR.

## Commit & Pull Request Guidelines
This checkout does not include `.git` history, so follow a simple imperative commit style with an optional scope, such as `codigo: fix walk-forward split edge case` or `tex: update metodologia references`. Pull requests should state which area changed, list config or data assumptions, link the related task, and include screenshots when plots, MLflow outputs, or generated PDF pages change. Avoid committing generated artifacts such as `.logs/`, `.pids/`, `mlartifacts/`, or temporary analysis outputs unless they are the intended deliverable.
