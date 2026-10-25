# VELQIRIS — The Agent That Can Explain Why

Evidence-first market-consensus agent for the Open Agent Hackathon 2026, Track 02.

VELQIRIS executes a declared market-integrity scenario in Zetaris, applies Median Absolute Deviation (MAD) filtering, captures the observation and finding in Meterless H-MEM, retrieves them with an inspectable ranking trace, and emits redaction-safe evidence receipts.

## Verified release status

- **Zetaris live:** the official local Docker bundle 2.4.3 passed its own verifier **9/9**. The verified route is `UI -> API -> driver -> Spark`.
- **Live SQL proof:** `SELECT 7 AS seven` returned one row; a four-row market scenario also executed live in Zetaris and returned four rows. The scenario rows are declared synthetic. No production exchange-feed claim is made.
- **Meterless live:** the vendored official H-MEM reference at upstream commit `1742dec56a66e58eef9dda2d2b865823758ca8cd` stored and retrieved both evidence memories, writing four append-only ledger events to local persistent storage.
- **Meterless conformance:** the official H-MEM conformance suite passed **13/13**.
- **Project tests:** **24/24** Python tests pass.
- **Public repository:** <https://github.com/genesiscode2026/velqiris-open-agent-2026>
- **Integrity terminology:** SHA-256 values are integrity digests, not digital signatures.
- **Model boundary:** no external model was invoked in the live integration receipt. NVIDIA Nemotron is an optional in-kind prize integration and is not claimed here.

The live receipt measures client-side durations of approximately 5.6 seconds for the connectivity query and 7.4 seconds for the four-row scenario on this first local Apple Silicon run. These are evidence timestamps, not a performance benchmark or a latency claim.

## Verified workflow

1. Log in to the official local Zetaris bundle with a short-lived session.
2. Execute Lightning SQL with a fresh `X-Request-ID`.
3. Normalize returned rows without fabricating fallback data.
4. Compute post-filter MAD consensus and reject the anomalous venue.
5. Store the query observation and derived consensus in the official Meterless H-MEM reference engine.
6. Retrieve both memories with hybrid ranking and preserve the trace.
7. Persist the H-MEM state and append-only ledger locally.
8. Publish redaction-safe receipts with SHA-256 digests; never persist credentials or session tokens.

## Evidence

- [`evidence/zetaris-platform-verification.json`](evidence/zetaris-platform-verification.json): official Zetaris verifier, 9/9.
- [`evidence/zetaris-live-receipt.json`](evidence/zetaris-live-receipt.json): live query IDs, rows, timings, result hashes, and claim boundary.
- [`evidence/meterless-hmem-live-receipt.json`](evidence/meterless-hmem-live-receipt.json): official H-MEM runtime, retrieval scores, ledger count, and ledger digest.
- [`evidence/meterless-hmem-conformance.json`](evidence/meterless-hmem-conformance.json): official suite, 13/13.
- [`evidence/meterless-hmem-runtime/`](evidence/meterless-hmem-runtime/): persisted state and append-only ledger.
- [`evidence/offline-evidence.json`](evidence/offline-evidence.json): explicitly labelled offline regression artifact.

## Reproduce the public checks

```bash
python3 tests/run_all_tests.py
python3 agent/cli.py --dry-run --output evidence/offline-evidence.json
npm ci --prefix vendor/meterless-hmem-reference
HMEM_IMPL="$PWD/vendor/meterless-hmem-reference/src/index.ts" \
  vendor/meterless-hmem-reference/node_modules/.bin/tsx \
  vendor/meterless-hmem-conformance/runner.ts
```

Expected results: Python **24/24**, Meterless H-MEM **13/13**.

Reproducing the live Zetaris receipt additionally requires the official event bundle, Docker Desktop, the registry entitlement, and a local `.env` supplied by Zetaris:

```bash
python3 scripts/capture_live_integrations.py \
  --zetaris-env /path/to/zetaris-platform/.env \
  --receipt evidence/zetaris-live-receipt.json \
  --meterless-input evidence/meterless-hmem-input.json

vendor/meterless-hmem-reference/node_modules/.bin/tsx \
  scripts/meterless_official_bridge.ts \
  evidence/meterless-hmem-input.json \
  evidence/meterless-hmem-live-receipt.json \
  evidence/meterless-hmem-runtime
```

## Sponsor integration

| Sponsor | Integration | Verified evidence |
|---|---|---|
| Zetaris | Official local bundle; session login; Lightning SQL through UI, API, driver and Spark; fresh request IDs | 9/9 verifier plus two successful live queries |
| Meterless | Official H-MEM reference engine, local persistence, hybrid retrieval and append-only trust ledger | 13/13 conformance plus runtime receipt and ledger |

The project-local `MeterlessGovernor` is only local prompt and cost arithmetic. It is not provider billing telemetry and is not used as proof of Meterless integration.

## Offline mode and fail-closed behavior

Fixture data is available only with `--dry-run`, is labelled `OFFLINE_SIMULATION`, and never proves external integration. Live Zetaris mode accepts either:

- a bearer token plus organization ID; or
- the official local bundle's administrator session credentials.

If neither credential mode is configured, live execution fails closed and returns no synthetic rows.

## Repository structure

```text
├── agent/                          Python workflow and adapters
├── scripts/                        Live receipt and Meterless bridge tools
├── vendor/
│   ├── meterless-hmem-reference/  Official Apache-2.0 reference engine
│   └── meterless-hmem-conformance/ Official conformance harness and vectors
├── tests/                          24 deterministic regression tests
├── evidence/                       Live and offline redaction-safe receipts
├── artifacts/                      Final MP4 and PPTX
└── PREEXISTING_TECHNOLOGY.md       Build-window disclosure
```

## Pre-existing technology disclosure

The VELQIRIS brand, initial Python adapters, fixture workflow, MAD logic, project-local governor and original tests predate the official 22 October 2026 build-window start. The fail-closed hardening, local-session Zetaris adapter, live Zetaris execution, official Meterless H-MEM bridge, conformance evidence, receipts, expanded 24-test suite, documentation and release artifacts were completed during the current build window. See [`PREEXISTING_TECHNOLOGY.md`](PREEXISTING_TECHNOLOGY.md).

## License

Project code: Apache License 2.0. Vendored Meterless H-MEM files retain their upstream Apache-2.0 license and provenance in `vendor/meterless-hmem-reference/UPSTREAM.md`.
