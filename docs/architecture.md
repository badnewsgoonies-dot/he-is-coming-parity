# Parity Architecture

## Modules
- engine/: deterministic combat and timeline rules
- systems/: map and inventory state models
- content/: loaders and schema validation hooks
- modes/: Kingmaker and Friend Battle rule layers
- parity/: harness + scoreboard for gap tracking

## Data Flow (High-Level)
1) Seeded RNG initializes the run state.
2) Map/timeline advance with each node action.
3) Combat resolves with ordered triggers and status effects.
4) Results update run state and parity metrics.

## Parity Workflow
- Every gap is a test.
- Every test must be tied to evidence.
- Scoreboard tracks coverage and remaining deltas.
