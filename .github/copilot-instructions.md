# Copilot Instructions for this Repository 🚀

> Note: I couldn't find any application source files in the repository (only a `venv/` directory). This file is a starter template—please add or adjust the sections below to reflect project specifics.

## Purpose
Help AI coding agents (Copilot-style) become immediately productive in this repository by documenting the high-level architecture, developer workflows, conventions, and key files to inspect.

---

## Quick Start (what an agent should do first) 🔍
1. Check for source directories at the repository root (`src/`, `app/`, `services/`, `packages/`). If none exist, open the project README or ask a maintainer.
2. Inspect `pyproject.toml`, `setup.cfg`, `requirements.txt`, or `package.json` for build/test commands and dependencies.
3. Run the test suite (`pytest`, `npm test`, or project-specific command) in a disposable environment and report failures.
4. Look for CI config files (`.github/workflows/**`, `azure-pipelines.yml`, etc.) to discover important checks and environment variables.

---

## Architecture & Big Picture (how to discover it) 🏗️
- Look for top-level directories and their README files to learn major components (e.g., `api/`, `worker/`, `ui/`, `lib/`).
- Inspect `docker-compose.yml` or `Dockerfile` to understand services and ports.
- For Python: check for `src/` package layout and `__main__.py` entry points (if present). For JS/TS: check `src/index.js` or `src/server.ts`.
- Map data flows by tracing where models/schemas are defined (e.g., `models/`, `schemas/`) and where they are consumed (controllers, handlers, tasks).

---

## Developer Workflows & Commands 🔧
- Tests: prefer `pytest` for Python projects and `npm test`/`pnpm test` for JS projects. Use `-k` to run focused tests.
- Type checks: run `mypy` / `pyright` / `tsc` if configured.
- Linting/formatting: check for `pre-commit`, `flake8`, `eslint`, `black`, or `prettier` in repo.
- Local services: inspect `docker-compose.yml` or `Makefile` for `make up`, `make start` or `docker-compose up` commands.

Include exact commands here once you add them to the repo (replace these placeholders):
- Run tests: `pytest -q`
- Run type checks: `mypy .`
- Start app locally: `python -m src` or `npm run dev`

---

## Project-specific Conventions & Patterns 🔁
(Replace or extend these examples with concrete project patterns.)
- Module layout: `src/<package>/...` with tests in `tests/` mirror structure.
- Error handling: prefer returning `Result`-like objects or raising HTTP exceptions from controllers (document specific pattern files).
- Config: environment-driven (`.env` + `os.environ`) with `settings.py` or `config.js` centralizing env var usage.

---

## Integration Points & External Dependencies 🔗
- Identify external services in `settings` files (e.g., Redis, Postgres, S3, third-party APIs). Document which env vars control credentials.
- Check CI workflows for secrets and environment setup steps.

---

## How to Propose & Make Changes (agent etiquette) ✍️
- Create a short, focused PR that modifies one logical area.
- Run & attach failing local tests when proposing behavior-changing edits.
- Add or update unit tests for new behavior; include examples in the test that capture the bug or desired feature.

---

## What *not* to do
- Don't make broad refactors across unrelated modules without tests or maintainer sign-off.
- Don't change CI configuration without validating it in a forked branch and explaining the impact.

---

## Maintenance Checklist for Humans (what to add next) ✅
- Add concrete commands to "Developer Workflows" (test, lint, start, build).
- Document the concrete package layout and critical files (e.g., `src/api/**`, `src/worker/**`).
- List required environment variables and how to obtain/create them for local dev.
- Provide links to architecture docs or ADRs (Architecture Decision Records) if available.

---

If you'd like, I can:
- Try to auto-detect project files again and populate the placeholders with exact commands.
- Create a checklist PR that adds missing README details into `README.md` or this file.

Please tell me which you'd prefer. 👋
