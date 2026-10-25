# HackOS submission copy

## Project name

VELQIRIS — The Agent That Can Explain Why

## One-line description

Evidence-first market-consensus agent that executes governed SQL in Zetaris, isolates outliers with MAD, and preserves the reasoning context in Meterless H-MEM.

## Project description

VELQIRIS helps execution reviewers understand not only what a multi-source consensus is, but why it is defensible. The verified workflow executes a declared four-venue market scenario in the official Zetaris local platform, normalizes the returned rows, computes a post-filter consensus with Median Absolute Deviation, rejects the anomalous venue, stores the observation and finding in Meterless H-MEM, retrieves both with inspectable hybrid-ranking scores, and persists an append-only trust ledger.

The sponsor path is verified. Zetaris's official verifier passed 9/9, including a query routed through UI, API, driver and Spark. A separate connectivity query and the four-row scenario both executed live and produced redaction-safe receipts. The official Meterless H-MEM reference engine stored and retrieved the evidence, and its official conformance suite passed 13/13. The Python project suite passes 24/24.

The four market rows are intentionally synthetic and declared in the SQL itself. They prove real Zetaris execution and deterministic VELQIRIS behavior, not connectivity to production exchange feeds. No single-digit-latency, provider-cost, external-model, or digital-signature claim is made. SHA-256 is used only as an integrity digest.

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
- Python tests: 24/24.
- Live Zetaris rows: 1 connectivity row and 4 declared scenario rows.
- Meterless runtime: 2 stored memories, 2 retrieved memories, 4 ledger events.
- Public repository: https://github.com/genesiscode2026/velqiris-open-agent-2026

## Pre-existing technology disclosure

Pre-existing: VELQIRIS brand, initial adapters, fixture workflow, MAD logic, local prompt/cost governor, and original tests. New during the official build window: fail-closed hardening, local-session Zetaris support, live Zetaris execution, official Meterless H-MEM bridge, conformance evidence, redaction-safe receipts, expanded 24-test suite, documentation, deck, and demo. Full disclosure: `PREEXISTING_TECHNOLOGY.md`.
