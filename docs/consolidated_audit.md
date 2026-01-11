# He Is Coming - Consolidated Gameplay Audit (v1)

## Scope
This audit consolidates gameplay mechanics, systems, modes, and official statements to guide a DLC-quality replication plan.

## Evidence (Primary Sources)
- artifacts/he_is_coming_clean_v2/synthesis.md (longplay + overview)
- artifacts/he_is_coming_extra_v1/synthesis.md (additional creators + difficulty contexts)
- artifacts/he_is_coming_modes_v1/synthesis.md (Kingmaker + Friend Battle modes)
- artifacts/he_is_coming_kingmaker_v2/synthesis.md (Kingmaker scoring deep dive)
- artifacts/he_is_coming_kingmaker_v3/synthesis.md (Kingmaker win-condition variant)
- artifacts/he_is_coming_research/steam_announcements_summary.md (Steam announcements/patch notes)
- artifacts/he_is_coming_research/pages/https_store_steampowered_com_app_2824490_He_is_Coming.txt (official store text)

## Executive Summary
He Is Coming is a roguelite auto-battler with grid exploration and a strict day/night timeline. Players assemble a build from limited inventory slots, with items triggering in a fixed order and conditional statuses (Wounded, Exposed, Freeze, Thorns, Poison, Acid, Stun, Riptide). The run is paced by boss cadence every three days. Meta-progression is driven by a compendium-style grid unlocks system.

The multiplayer ecosystem is split into Kingmaker (async ladder/king runs) and Friend Battle (real-time 1v1 with shared seed). Both modes require dedicated UI elements, bundle selection, and opponent visibility.

## Core Loop (Single-Player)
- **Explore:** Grid-based map with fog-of-war; movement advances time.
- **Loot:** Treasure/merchant/forge/golem nodes provide items or upgrades.
- **Auto-battle:** Turn-based, automated combat driven by stats and item triggers.
- **Build:** Items trigger sequentially by slot; item tags and set bonuses create synergies.
- **Boss cadence:** Boss appears at fixed timeline intervals (officially every three days).
- **Progression:** Boss wins expand inventory capacity for that run; compendium unlocks expand item pool across runs.

## Key Systems
### Map & Time
- Grid movement, fog-of-war, POIs (merchants, chests, forges, campfires, golems, waypoints).
- Day/night timeline; night increases danger and reduces visibility.
- Boss forecast on timeline; skull marker indicates final encounter.

### Combat & Stats
- Automated, turn-based combat.
- Stats: Health, Attack, Armor, Speed; Armor absorbs damage first and replenishes after battles.
- Speed drives initiative and multi-strike effects.
- Status/keywords: Wounded, Exposed, Freeze, Thorns, Poison, Acid, Stun, Riptide.

### Items & Triggers
- Limited slots; items trigger in slot order.
- Trigger types: Battle start, On hit, End of turn, Wounded, Exposed.
- Weapon edges via Forge (e.g., blunt/bleeding/featherweight variants).
- Golem merges identical items into golden tier.
- Fairy transforms an item into another of same rarity.
- Cauldron combines food items into a stronger result.
- Banish removes an item from the pool for the remainder of a run.

### Progression & Meta
- Compendium grid unlocks: challenges unlock adjacent nodes, expanding the item pool.
- Regions/biomes: Woodland, Swampland, and additional regions (e.g., Scorched Hill, Abandoned Quarry, Glyph Ruins).
- Difficulty: Very Hard introduces additional item/boss variants.

## Modes
### Kingmaker (Async Ladder)
- Entry via Multiplayer menu; select champion/skins and choose 3 biome item bundles.
- Async ladder: runs culminate in a duel vs the current champion/king.
- Rank tracked by crown icon; winning increases rank and can replace the king.
- Unique UI: dual progress tracks, crown score, and opponent indicators.
- Crowns are earned per victory (+1 crown reward card). Crown total appears in HUD and on a top progress bar.
- Crown milestones appear at fixed thresholds (observed 5/9/14/19/24), while other runs show shorter crown tracks (4 or 10 slots), suggesting mode-length variants.
- Tiebreak behavior appears tied to horizontal position on the crown track; a TRB marker appears next to some opponent ranks but meaning is unclear.
- Additional variant: some sessions show a 3-crown target and a tug-of-war crown indicator between sun/moon endpoints.

### Friend Battle (Real-Time 1v1)
- Private lobby with join code; both players select 3 bundles.
- Same-seed runs for fair build parity; players explore independently.
- Combat phases sync when both players are ready; “waiting for opponent” gate.
- Opponent visibility: map marker, item/stats inspection, and post-battle summaries.
- Win conditions: win combat rounds, accumulate stars, or outlast opponent at final skull.

## Official Claims (Steam)
- 30+ bosses in the pool; boss every 3 days.
- 350+ items and 100+ challenges (compendium unlocks).
- Kingmaker async mode plus real-time Friend Battle.

## DLC-Quality Replication Requirements
### Must-Match Systems
- Deterministic combat with slot-ordered triggers and conditional status effects.
- Day/night timeline and boss cadence; fog-of-war with night visibility reduction.
- Golem merge, Forge edges, and Compendium unlock grid.
- Kingmaker async ladder and Friend Battle real-time 1v1 flow.

### Recommended Additions
- Banish, Fairy transform, Cauldron combining, Horse carriage fast travel.
- Region-specific enemies/loot and difficulty-tier gating.
- Clear post-battle summary screens and opponent build visibility.

## Open Questions / Risks
- Exact Kingmaker scoring math across variants (3/4/10-slot vs milestone track) and TRB meaning.
- Precise boss pool composition and late-game encounter scripts.
- Full compendium grid topology and unlock dependencies.
- Exact star scoring and end-of-match conditions in Friend Battle.

## Evidence Appendix
See artifacts/he_is_coming_research/steam_announcements_summary.md for patch notes and mode changes.
