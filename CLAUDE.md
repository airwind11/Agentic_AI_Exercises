# Agentic AI Hands-on Exercises

Certification course project. This repo contains Python exercises that call the
Anthropic Messages API directly (separate from Claude Code's own subscription billing).

## Important billing context
- Claude Code (this IDE session) runs on a Pro subscription — flat monthly rate.
- Code in this repo that calls `anthropic.Anthropic()` uses a SEPARATE API key
  (Console account, pay-per-token, small spend limit set).
- Never suggest setting ANTHROPIC_API_KEY as a global/system environment variable.
  It must only live in the local `.env` file, loaded via python-dotenv.

## Conventions
- Each exercise lives in its own numbered folder under `cert_python/`
  (e.g. `cert_python/1-agentic-architecture/1-1-agentic-loops/`)
- Default model: `claude-haiku-4-5-20251001` — cheapest option, fine for most early
  exercises (loop mechanics, basic tool use, simple API plumbing).
- If an exercise involves multi-step reasoning, planning, or judging output quality
  (and Haiku's responses seem off/weak), suggest switching that specific exercise to
  `claude-sonnet-4-6` rather than silently debugging — note this explicitly when it happens,
  so it's clear whether a bug is in the code or just model capability.
- Keep `max_tokens` modest (e.g. 1000) in exercises unless the task needs more.

## Environment / tooling
- This project uses `uv` (not pip/venv directly) for Python and package management.
- Always run scripts as: `uv run python <script>.py`
- To add a new package: `uv add <package-name>` (never suggest `pip install` directly).
- Project dependencies live in `pyproject.toml` / `uv.lock`, not `requirements.txt`.
