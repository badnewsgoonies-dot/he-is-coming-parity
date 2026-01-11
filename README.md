# He Is Coming Parity Build

This repository is the working codebase for a full-parity replication effort.

Goals:
- Implement deterministic core systems (combat, timeline, triggers).
- Build data-driven content pipelines (items, enemies, regions).
- Reach mode parity (Kingmaker + Friend Battle).
- Track parity gaps with automated tests and a scoreboard.

Structure:
- src/he_is_coming/: core engine, content, modes, parity harness
- schemas/: JSON schemas for content definitions
- tests/: determinism and parity tests
- docs/: architecture and evidence index

Quick start:
- Install dev deps: `python -m pip install -r requirements-dev.txt`
- Run tests: `bash scripts/run_tests.sh`
