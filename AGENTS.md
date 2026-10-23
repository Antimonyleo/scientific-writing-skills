# Repository guidance

- Maintain three independently usable skills under `skills/`; preserve their names unless explicitly requested.
- Keep entrypoints concise and put substantial conditional procedures in linked references. Read only what the current task needs.
- Preserve scientific meaning, numerical facts, citation keys, and the user's requested edit depth. Never invent evidence or completed actions.
- Verify changing agency, venue, and software facts against primary sources. Keep dated research in `docs/research.md`; runtime instructions should consult current governing rules.
- Use synthetic or public artifacts for examples and evaluations. Do not commit personal manuscripts, proposals, reviewer correspondence, credentials, or machine-specific paths.
- Keep core workflows independent of paid APIs, optional companion skills, and harness-specific tools.
- Run `python3 scripts/validate.py` after package changes. Run relevant behavioral scenarios in `evals/scenarios.md` after substantive instruction changes and update `docs/validation.md` with the observed scope and limitations.
- Do not describe a structural check as proof of improved scientific reasoning or automatic skill loading in another host.
