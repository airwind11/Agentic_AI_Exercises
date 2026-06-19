# Setup Instructions (uv workflow)

Run these once, in order, inside `Agentic_AI_exercises`:

```powershell
# 1. Initialize the project (creates pyproject.toml)
uv init --no-readme

# 2. Add the two packages this project needs
uv add anthropic python-dotenv

# 3. Create your .env file (copy .env.example, then paste your real key in)
copy .env.example .env

# 4. Verify everything works end to end
uv run python check_setup.py
```

If step 4 prints "✅ Setup confirmed working", you're ready to start the exercises.

## Day-to-day pattern

Every time you run a script in this project, use:
```powershell
uv run python <script_name>.py
```

`uv run` automatically uses the right Python version and the right virtual environment —
no manual activation needed, and no dependence on Windows PATH.

## Adding new packages later

If a future exercise needs a new package:
```powershell
uv add <package-name>
```
This updates `pyproject.toml` and `uv.lock` automatically.
