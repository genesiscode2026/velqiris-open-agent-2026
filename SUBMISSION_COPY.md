# HackOS submission copy

## Project name

VELQIRIS — The Agent That Can Explain Why

## One-line description

Evidence-first market-consensus agent that joins governed market and venue telemetry in Zetaris, isolates outliers with MAD, and preserves the reasoning context in Meterless H-MEM.

## Project description

VELQIRIS helps reviewers understand not only what a market consensus is, but why it is defensible. The verified workflow executes a live Zetaris SQL JOIN across two declared logical relations: `market_ticks` (venue, pair, bid, ask, volume) and `venue_telemetry` (venue, latency, health). It normalizes the four returned rows, computes a Median Absolute Deviation consensus, rejects the anomalous venue, stores the observation and finding in the official Meterless H-MEM reference engine, retrieves both with inspectable hybrid-ranking scores, and persists an append-only trust ledger.

The sponsor path is verified: Zetaris's official verifier passed 9/9 through UI, API, driver and Spark; the JOIN returned 4/4 rows in an observed 8.395 seconds; Meterless stored and retrieved two memories with four ledger events; its official conformance suite passed 13/13; and the Python project suite passes 30/30. The standalone Audit Viewer at `artifacts/index.html` renders the receipt and ledger without external JavaScript.

Both logical relations are intentionally synthetic and declared in the SQL itself. They prove real Zetaris JOIN execution and deterministic VELQIRIS behavior, not independent external-source federation or production exchange feeds. The 8.395-second timing is one observation, not a benchmark. No provider-cost, external-model, or digital-signature claim is made; SHA-256 is used only as an integrity digest.

## Sponsor integration

### Zetaris

`agent/zetaris_client.py` supports both bearer-key deployments and the official local bundle's short-lived login session. The verified local path sends a fresh `X-Request-ID` to `/api/proxy/query/sql/start`. Missing live credentials fail closed and never return fixture rows.

Evidence: `evidence/zetaris-platform-verification.json` and `evidence/zetaris-live-receipt.json`.

### Meterless

The Apache-2.0 official Meterless H-MEM reference implementation is vendored with its upstream commit and license. `scripts/meterless_official_bridge.ts` stores the live Zetaris observation and the VELQIRIS consensus, retrieves both with the official hybrid ranker, and persists `state.json` plus `ledger.jsonl`.

Evidence: `evidence/meterless-hmem-live-receipt.json`, `evidence/meterless-hmem-runtime/`, and `evidence/meterless-hmem-conformance.json`.

## Verification summary

- Zetaris verifier: 9/9.
- Meterless H-MEM conformance: 13/13.
- Python tests: 30/30.
- Live Zetaris rows: 1 connectivity row and 4 declared scenario rows.
- Meterless runtime: 2 stored memories, 2 retrieved memories, 4 ledger events.
- Audit Viewer: `artifacts/index.html`.
- Public repository: https://github.com/genesiscode2026/velqiris-open-agent-2026

## Pre-existing technology disclosure

Pre-existing: VELQIRIS brand, initial adapters, fixture workflow, MAD logic, local prompt/cost governor, and original tests. New during the official build window: fail-closed hardening, local-session Zetaris support, live Zetaris execution, official Meterless H-MEM bridge, conformance evidence, redaction-safe receipts, expanded 30-test suite, Audit Viewer, documentation, deck, and demo. Full disclosure: `PREEXISTING_TECHNOLOGY.md`.
