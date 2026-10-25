# VELQIRIS — The Agent That Can Explain Why

Evidence-first agent prototype for the Open Agent Hackathon 2026, Track 02.

## Verification status

This release proves the local orchestration and the Meterless H-MEM integration. A live Zetaris receipt is still required before the project can truthfully claim a complete sponsor-integrated run.

- **Verified locally:** 21 unit tests covering fixture ingestion, MAD filtering, tool schema, fail-closed behavior, SHA-256 integrity hashing, H-MEM provenance, hierarchical capture, hybrid retrieval, persistence, and tamper-evident trust-ledger verification.
- **Meterless integrated:** a local-first implementation of the official H-MEM contract subset used by this workflow: canonical memories with lineage, `working`/`long_term` layers, hybrid retrieval with trace reasons, and an append-only hash-chained trust ledger.
- **Implemented but not yet evidenced live:** the Zetaris REST adapter and an OpenAI-compatible model adapter.
- **Not a digital signature:** the SHA-256 value is an integrity digest. There is no private-key signature or signer identity in the current prototype.
- **Release gate:** do not describe the end-to-end run as live until a real Zetaris query produces a redacted receipt.

The CLI distinguishes live execution from simulation. Live mode fails closed when credentials or an exact model ID are absent; fixture data is available only with `--dry-run`.

## Intended workflow

1. Query multi-venue market rows through the Zetaris REST adapter.
2. Compute a robust consensus and isolate price outliers with Median Absolute Deviation (MAD).
3. Capture the query observation and derived finding in Meterless H-MEM.
4. Retrieve context with multi-signal ranking and explicit trace metadata.
5. Ask a configured model to explain the result using the retrieved evidence.
6. Save an evidence record with a SHA-256 integrity digest and H-MEM trust-ledger head.

The included fixture uses synthetic market rows. It is suitable for local orchestration tests, not for claims about live venues, measured Zetaris latency, Meterless usage, model quality, or provider cost.

## Run the verified offline simulation

```bash
python3 tests/run_all_tests.py
python3 agent/cli.py --dry-run
```

Expected behavior:

- test output reports 21 passing local tests;
- CLI output is visibly labelled `OFFLINE SIMULATION`;
- no external model call is claimed;
- estimated provider cost remains zero;
- the evidence record labels the source and model modes.

## Configure a live validation run

Use only credentials and identifiers issued for the current event environment:

```bash
export ZETARIS_REST_URL="https://your-current-zetaris-endpoint"
export ZETARIS_API_KEY="..."
export ZETARIS_ORG_ID="..."
export MODEL_BASE_URL="https://your-current-model-endpoint/v1"
export MODEL_API_KEY="..."
export NEMOTRON_MODEL="exact-current-model-id"

python3 agent/cli.py --query "SELECT * FROM your_verified_source"
```

Do not publish live-integration claims until the run produces redacted evidence showing the source, timestamp, request/result status, measured client-side elapsed time, exact model ID, and non-simulated execution modes.

## Sponsor-integration matrix

| Component | Current code | Evidence required before claiming integration |
|---|---|---|
| Zetaris | REST request adapter with bearer token, organization ID and unique request ID | Successful live query against an identified source, redacted receipt/result, and measured timing |
| Meterless | H-MEM core profile implemented and exercised locally | Evidence record contains engine name, official spec URL, stored/retrieved IDs, retrieval strategy, ledger-entry count, and ledger-head SHA-256 |
| NVIDIA Nemotron | Generic OpenAI-compatible chat adapter | Successful call using an exact currently available Nemotron model ID and a redacted response receipt |
| Cursor | Development-tool references only | Development evidence if Cursor use is claimed |

## Evidence terminology

- **Integrity hash:** SHA-256 digest used to detect a changed payload.
- **Digital signature:** requires a private key and verifiable signer identity; not implemented here.
- **H-MEM trust-ledger hash:** a hash-chain integrity control for local memory mutations; it is not a signature.
- **Local cost estimate:** project-local arithmetic, not Meterless or model-provider billing telemetry.
- **Offline test:** verifies code behavior against fixtures/mocks; does not prove external integration.

## Repository structure

```text
open_agent_2026/
├── agent/
│   ├── cli.py
│   ├── config.py
│   ├── evidence_explainer.py
│   ├── llm.py
│   ├── meterless_governor.py
│   ├── meterless_hmem.py
│   └── zetaris_client.py
├── tests/
├── DEMO_VIDEO_SCRIPT.md
├── PREEXISTING_TECHNOLOGY.md
├── VERIFICATION_STATUS.md
└── LICENSE
```

## Competition disclosure

The base prototype files predate the event page's current build-window start of 22 October 2026. They are disclosed as pre-existing product code. The H-MEM integration, evidence hardening, fail-closed release gates and expanded tests were completed during the current build window.

## Submission artifacts

- [Narrated demo — 3:31 MP4](artifacts/VELQIRIS_Open_Agent_2026_Demo.mp4)
- [Pitch deck — PPTX](artifacts/VELQIRIS_Open_Agent_2026_Pitch_Deck.pptx)
- [Generated offline evidence record](evidence/offline-evidence.json)
- [Reproducible release evidence](RELEASE_EVIDENCE.md)
- [Pre-existing technology disclosure](PREEXISTING_TECHNOLOGY.md)

The demo and deck preserve the same release gate as the code: Meterless H-MEM is exercised locally; the Zetaris fixture is explicitly offline until a live receipt is available.

## Meterless implementation profile

H-MEM is an implementation specification, not a hosted service dependency. This project implements the operational subset used by VELQIRIS directly in Python, following the [official Meterless H-MEM specification](https://github.com/Meterless/Meterless/tree/main/engines/hmem):

- canonical memory records with `source`, confidence, domains, entities, relationships and `derivedFrom` lineage;
- hierarchical `short_term`, `working`, and `long_term` layers;
- hybrid retrieval using keyword, tag, entity, domain, layer, recency and confidence signals;
- retrieval trace metadata with the reason and score for every selected memory;
- append-only, SHA-256 hash-chained trust ledger with complete-chain verification.

Dreaming, sleep-cycle and conflict-resolution services are intentionally outside this hackathon profile and are not claimed.

## License

Apache License 2.0. See `LICENSE`.
